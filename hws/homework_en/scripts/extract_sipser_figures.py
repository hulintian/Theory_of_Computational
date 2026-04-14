#!/usr/bin/env python3

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import fitz


@dataclass(frozen=True)
class FigureSpec:
    page: int
    clip: tuple[float, float, float, float]
    output_name: str


DEFAULT_PDF_NAME = (
    "Introduction to the Theory of Computation, Third International Edition "
    "(Michael Sipser) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
)


FIGURES: dict[str, FigureSpec] = {
    "0.9": FigureSpec(
        page=50,
        clip=(155, 140, 325, 260),
        output_name="exercise_0_9_graph.png",
    ),
    "7.39": FigureSpec(
        page=350,
        clip=(125, 200, 425, 305),
        output_name="exercise_7_39_figure.png",
    ),
}


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    default_pdf = repo_root.parent / DEFAULT_PDF_NAME
    default_outdir = repo_root / "chapters" / "assets"

    parser = argparse.ArgumentParser(
        description="Extract selected exercise figures from the Sipser English PDF."
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        default=default_pdf,
        help=f"Path to the source PDF. Default: {default_pdf}",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=default_outdir,
        help=f"Directory for exported PNG files. Default: {default_outdir}",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=2.5,
        help="Rasterization scale passed to PyMuPDF. Default: 2.5",
    )
    parser.add_argument(
        "--figures",
        nargs="+",
        choices=sorted(FIGURES),
        default=sorted(FIGURES),
        help="Figure ids to export. Default: all known figures.",
    )
    return parser.parse_args()


def export_figure(doc: fitz.Document, outdir: Path, figure_id: str, scale: float) -> Path:
    spec = FIGURES[figure_id]
    page = doc[spec.page - 1]
    clip = fitz.Rect(*spec.clip)
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip, alpha=False)
    outpath = outdir / spec.output_name
    pix.save(str(outpath))
    return outpath


def main() -> int:
    args = parse_args()
    pdf_path = args.pdf.expanduser().resolve()
    outdir = args.outdir.expanduser().resolve()

    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    outdir.mkdir(parents=True, exist_ok=True)

    with fitz.open(str(pdf_path)) as doc:
        for figure_id in args.figures:
            outpath = export_figure(doc, outdir, figure_id, args.scale)
            print(f"{figure_id}: {outpath}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
