#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


EXERCISE_SUBSECTION_RE = re.compile(r"^\\subsection\*\{\d+(?:\.\d+)+\}")
INPUT_RE = re.compile(r"(\\input\{)(chapters/[^}]+)(\})")

SOLUTION_COMMAND_PREFIXES = (
    r"\subsubsection*{",
    r"\paragraph{",
    r"\begin{proof}",
    r"\begin{enumerate}",
    r"\begin{itemize}",
    r"\begin{center}",
    r"\begin{tikzpicture}",
    r"\begin{myalgo}",
    r"\begin{algorithmic}",
    r"\medskip",
    r"\noindent",
    r"\[",
    "$$",
)

TEXTUAL_SOLUTION_PREFIXES = (
    "解答",
    "答案",
    "案：",
    "案:",
    "证明。",
    "证明如下",
    "解答如下",
)

LIKELY_SOLUTION_TEXT_PREFIXES = (
    "设",
    "构造",
    "记",
    "给定",
    "输入",
)


def looks_like_solution_start(line: str) -> bool:
    return line.startswith(SOLUTION_COMMAND_PREFIXES) or line.startswith(TEXTUAL_SOLUTION_PREFIXES)


def next_significant_line(lines: list[str], start: int) -> str:
    for idx in range(start, len(lines)):
        stripped = lines[idx].strip()
        if stripped and not stripped.startswith("%"):
            return stripped
    return ""


def extract_question_block(block: list[str]) -> list[str]:
    kept = [block[0]]
    in_figure = False
    saw_figure = False

    for idx in range(1, len(block)):
        line = block[idx]
        stripped = line.strip()

        if in_figure:
            kept.append(line)
            if stripped.startswith(r"\end{figure}"):
                in_figure = False
                saw_figure = True
            continue

        if not stripped or stripped.startswith("%"):
            kept.append(line)
            continue

        if stripped.startswith(r"\begin{figure}"):
            in_figure = True
            kept.append(line)
            continue

        if stripped.startswith(r"\subsection*{"):
            break

        if looks_like_solution_start(stripped):
            break

        if saw_figure and stripped.startswith(LIKELY_SOLUTION_TEXT_PREFIXES):
            upcoming = next_significant_line(block, idx + 1)
            if looks_like_solution_start(upcoming):
                break

        kept.append(line)

    if kept and kept[-1].strip():
        kept.append("\n")
    return kept


def strip_chapter_to_questions(content: str) -> str:
    lines = content.splitlines(keepends=True)
    subsection_indices = [idx for idx, line in enumerate(lines) if EXERCISE_SUBSECTION_RE.match(line)]
    if not subsection_indices:
        return content

    pieces: list[str] = []
    first = subsection_indices[0]
    pieces.extend(lines[:first])

    bounds = subsection_indices + [len(lines)]
    for start, end in zip(bounds, bounds[1:]):
        pieces.extend(extract_question_block(lines[start:end]))

    return "".join(pieces)


def write_questions_sources(root: Path, output_dir: Path) -> None:
    structure_src = root / "structure.tex"
    structure_dst = output_dir / "structure_questions.tex"
    structure_dst.parent.mkdir(parents=True, exist_ok=True)

    output_lines: list[str] = []
    for line in structure_src.read_text(encoding="utf-8").splitlines(keepends=True):
        match = INPUT_RE.search(line)
        if not match:
            output_lines.append(line)
            continue

        input_target = match.group(2)
        source_file = root / f"{input_target}.tex"
        dest_file = output_dir / f"{input_target}.tex"
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        stripped = strip_chapter_to_questions(source_file.read_text(encoding="utf-8"))
        dest_file.write_text(stripped, encoding="utf-8")

        input_path = dest_file.with_suffix("").relative_to(root).as_posix()
        output_lines.append(f"{match.group(1)}{input_path}{match.group(3)}\n")

    structure_dst.write_text("".join(output_lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate question-only TeX sources.")
    parser.add_argument("--root", default=".", help="LaTeX project root.")
    parser.add_argument("--output-dir", required=True, help="Directory for generated sources.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = (root / args.output_dir).resolve()
    write_questions_sources(root, output_dir)


if __name__ == "__main__":
    main()
