# homework_cn Layout Notes

## Entry Files

- `homework_cn/main.tex` is the document entry point.
- The document class is `ctexart` with `UTF8`, `a4paper`, and `9pt`.
- `main.tex` loads:
  - `common/packages`
  - `common/layout.tex`
  - `structure`

## Chapter Wiring

- `homework_cn/structure.tex` prints the table of contents, then inputs:
  - `chapters/chapter0`
  - `chapters/chapter1`
  - ...
  - `chapters/chapter10`
- Each chapter file is therefore edited directly; there is no per-problem include layer.

## Build System

- `homework_cn/Makefile` uses `xelatex`.
- `make -C homework_cn`:
  - creates `build/`
  - runs `xelatex -output-directory=build main`
  - copies `build/main.pdf` back to `homework_cn/main.pdf`
- `homework_cn/latexmkrc` also targets XeLaTeX and keeps aux/output files in `build/`.

## Shared TeX Setup

- `homework_cn/common/packages.tex` provides the common packages.
- Important available packages and tools:
  - math: `amsmath`, `amssymb`, `mathtools`, `bm`, `bigints`
  - layout/tables: `booktabs`, `longtable`, `tabularx`, `caption`
  - figures: `graphicx`, `subfigure`, `float`
  - lists and structure: `enumitem`, `titlesec`, `titletoc`
  - logic/algorithms/code: `ntheorem`, `algorithmicx`, `algpseudocode`, `listings`
  - drawing: `tikz` with `positioning`, `automata`, `arrows.meta`, `matrix`, `fit`, `backgrounds`
- Custom environments:
  - `proof` prints `证明.` and ends with a square.
  - `myalgo` creates a boxed algorithm header.
- `homework_cn/common/layout.tex` sets:
  - 2.5 cm margins on all sides
  - one-and-a-half line spacing
  - paragraph indent of `2em`

## Chapter Style

- Each chapter starts with:
  - `\section*{Chapter N}`
  - `\addcontentsline{toc}{section}{Chapter N}`
- Each problem uses an unnumbered subsection:
  - `\subsection*{0.4}`
  - `\subsection*{7.9}`
- Chapters usually end with `\clearpage`.

## Problem-Level Conventions

- The problem statement is usually an inserted screenshot under `chapters/imgs/...`.
- Solutions normally appear immediately after the figure block.
- Existing heading styles vary by problem:
  - `\paragraph{解答.}`
  - `\subsubsection*{解答}`
  - `\subsubsection*{证明}`
- Some older problems contain a trailing `\paragraph{案：}` placeholder or short summary line. Treat it as editable content, not as a hard structure requirement.

## Editing Playbook

- Search for the exact subsection string rather than inferring from chapter numbers alone.
- Edit only the target subsection span:
  - from `\subsection*{target}` inclusive
  - to the next `\subsection*{...}` or `\clearpage`
- Preserve the problem image and labels unless the task explicitly includes image work.
- Match the local style of nearby solved problems in the same chapter before introducing a different structure.
- If the user's text is rough, rewrite it into complete mathematical Chinese and proper LaTeX rather than pasting raw prose verbatim.
- Use displayed math for derivations, `enumerate` for subparts, and `proof` or a short closing square when the solution is proof-shaped.
