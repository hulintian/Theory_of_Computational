---
name: fill-homework-tex
description: For the Theory of Computation LaTeX homework project in this repository, use this skill when the user gives a target problem number such as 7.9 and plain-text solution content, and wants that content rewritten into project-style LaTeX and inserted into the correct subsection under homework_cn/chapters/*.tex, followed by a compile check.
---

# Fill Homework TeX

Use this skill for the `homework_cn` project when the user wants you to take a raw answer and place it into the right homework problem as LaTeX.

## Read First

1. Read [references/homework-cn-layout.md](references/homework-cn-layout.md).
2. If the task asks for explanation quality, proof-writing style, or a solution is more than a short computation, read [references/homework-cn-writing-style.md](references/homework-cn-writing-style.md).
3. Locate the target problem with an exact search for `\subsection*{<problem-number>}` inside `homework_cn/chapters`.
4. Read the full target subsection and one nearby solved problem in the same chapter before editing.

## Workflow

1. Identify the target chapter file from the exact subsection match.
2. Preserve the existing problem statement assets, especially screenshots in `chapters/imgs/`.
3. Convert the user's solution text into concise, correct LaTeX that matches the surrounding file's style.
4. Insert the solution into the target subsection.
5. Compile the project with `make -C homework_cn`.
6. If compilation fails, fix only the issues caused by your edit and recompile.

## Editing Rules

- Edit only the target chapter file unless a real package or layout dependency is required.
- Do not renumber sections or change `structure.tex` unless the problem does not exist yet and the user asked to add a new chapter include.
- Prefer replacing an empty placeholder such as `\paragraph{案：}` or a blank stub instead of appending a second answer block.
- If the problem already has a real solution, improve or replace it in place rather than duplicating it.
- Keep figure environments, labels, and image paths intact unless the user explicitly wants them changed.
- Reuse the local heading style already present nearby:
  - `\paragraph{解答.}` for short or medium answers.
  - `\subsubsection*{解答}` or `\subsubsection*{证明}` for longer structured solutions.
- When the nearby chapter uses `answernote`, use it for a final conceptual `\paragraph{解释.}` that explains why the construction or proof idea works; keep the main proof complete before the note.
- Use project-native math environments such as `\[` `\]`, `align*`, `enumerate`, `proof`, and `myalgo` when appropriate.
- Prefer existing packages and conventions over adding new macros.
- For multi-part answers, prefer `enumerate` with `label=(\alph*)` and an explicit `leftmargin`.
- Keep the prose in Chinese unless the surrounding subsection is clearly written in another style.

## Insertion Heuristics

- If the subsection currently contains only the problem image, place the answer directly after the final related figure.
- If there is a placeholder summary marker such as `\paragraph{案：}`, replace or expand that block if it is empty or clearly incomplete.
- If there is already a finished derivation plus a trailing short summary marker, keep the derivation and update the summary only when it adds value.
- The subsection boundary is the text from its `\subsection*{...}` line up to the next `\subsection*{...}` or `\clearpage`.

## Validation

- Run `make -C homework_cn` after the edit.
- Treat warnings as follow-up work only if they are introduced by your change or block output generation.
- In your response, report the edited file, the target problem number, and whether compilation succeeded.

## When To Stop And Ask

- The user did not provide a problem number.
- The exact subsection cannot be found.
- The user wants a diagram or asset that cannot be inferred from text alone and no existing image is available.
