# homework_cn Writing Style

Use this reference when filling or revising solutions in `homework_cn/chapters`, especially when the user asks for detailed explanation, proof style, or "解释" paragraphs.

## Overall Voice

- Write in Chinese mathematical prose: direct, explanatory, and complete enough that the grader can check each implication.
- Prefer a proof that first states the object being constructed, then explains correctness, then states the complexity or closure consequence.
- Do not leave a key step as "显然" if it carries the problem's main idea; replace it with one or two concrete sentences.
- Keep screenshots, labels, and existing `answerred` blocks. Add structure inside the answer, not outside the problem.

## Explanation Note Pattern

Many chapters use a final note:

```tex
\begin{answernote}
\paragraph{解释.}
...
\end{answernote}
```

Use this when the main proof may be technically correct but the intuition is worth preserving. The note should:

- Name the core idea in ordinary language.
- Explain why the construction/proof tactic is natural.
- Avoid adding new obligations not already proved in the main answer.
- Stay shorter than the proof unless the user explicitly asks for a detailed conceptual discussion.

Do not replace the proof with the note. The proof must still contain the formal construction, equivalence, or complexity bound.

## Chapter-by-Chapter Style

### Chapter 0

- Basic math, relations, graphs, and elementary proofs.
- Short `\paragraph{解答.}` answers are common, often followed by `answernote` with an intuitive restatement.
- For counterexamples or mistakes, identify the exact illegal step and state the rule being violated.

### Chapter 1

- Automata and regular languages. Long multipart problems use `\subsubsection*{(a) ...}` per part.
- TikZ automata are common for DFA/NFA construction; accompany diagrams with a short invariant such as what each state records.
- For closure/equivalence proofs, use "构造 -> 说明接受条件 -> 结论".

### Chapter 2

- CFG/PDA/CFL proofs. Typical answers define a grammar or automaton, then prove language equality.
- Closure proofs should name the old grammars, rename variables if needed, construct a new grammar, and explain why the language is exactly the desired operation.
- Non-CFL proofs should state the pumping/Ogden setup, choose a string, split into cases, and close with a contradiction.
- Final `answernote` paragraphs often summarize the construction idea, e.g. "在 CFG 上拼装" or "把不等条件拆成几个 CFL".

### Chapter 3

- Turing machine construction and recognizability/enumerability.
- Use stepwise machine descriptions with numbered actions or short paragraphs.
- Always mention halting when proving decidability; for recognizers, distinguish "accepts", "rejects", and "may loop".
- Explanation notes often highlight the operational hazard, such as one branch looping and blocking an enumeration.

### Chapter 4

- Decidability and computability characterizations.
- Proofs often use double implications: introduce the equivalence, prove `正向` and `反向`, then summarize.
- When using computation histories, say what is checked and why the check is finite/mechanical.
- For recognizer constructions from witnesses, emphasize enumeration plus a decidable verifier.

### Chapter 5

- Undecidability, reductions, Rice-style arguments, and recognizability.
- Standard shape: assume a decider/recognizer for the target, build a solver for a known hard problem, prove the iff, then conclude contradiction.
- For reductions from PCP or machine languages, explicitly define the encoded object and prove both directions.
- Use `\paragraph{若 ...}` / `\paragraph{反向 ...}` blocks for two-direction correctness.
- Explanation notes should say what information the target problem secretly contains.

### Chapter 6

- Turing reductions, oracles, self-reference, and Kolmogorov complexity.
- For oracle reductions, define the oracle language and show exactly what query is asked.
- For diagonal/self-reference proofs, name the constructed machine and analyze its behavior on its own description.
- `myalgo` is appropriate for short algorithmic constructions.

### Chapter 7

- Time complexity, P/NP, reductions, and NP-completeness.
- For membership in P/NP, give the algorithm or verifier and a concrete polynomial bound.
- For NP-hardness, state the source problem, describe the mapping, prove both directions, and bound the construction size.
- Long reductions should be broken into named paragraphs: membership, construction, correctness, size/complexity, conclusion.
- When analyzing algorithms, include the quantity being measured, such as number of variables, clauses, vertices, edges, or formula length.

### Chapter 8

- Space complexity, PSPACE, NL, and regular-expression succinctness.
- Space proofs must say what is stored, how many bits or tape cells it costs, and why large objects such as game trees, configuration graphs, products, or intermediate strings are not stored explicitly.
- For PSPACE membership, use depth-first search or Savitch-style reachability and stress that exponential time is allowed if only polynomial space is used.
- For L/NL membership, list the current state, counters, head positions, and nondeterministic guesses; each should be bounded by `O(\log n)` bits.
- For log-space reductions, say the output may be polynomial size but the work tape only keeps counters and scans the input.
- For construction lower bounds such as 8.24, use "choose parameters -> define expressions -> prove size bound -> prove agreement below threshold -> exhibit first separating string".

### Chapter 9

- Hierarchy, succinct regular expressions, and circuits.
- For hierarchy theorems, name the constructible bound, apply the theorem, compare asymptotic functions explicitly, then conclude strict containment.
- For expression/circuit construction, list subparts in `enumerate` and keep each construction short but justified.
- For circuit-size proofs, separate the requested size bound cases into paragraphs such as `(a)` and `(b)`.

### Chapter 10

- Randomized computation, pseudoprimality, branching programs, and advanced complexity classes.
- Proofs are concise but should include the defining test or computational model before applying it.
- For modular arithmetic examples, show the selected base, gcd condition, congruence calculation, and final conclusion.
- For branching programs, describe the layer invariant, transitions, accepting/rejecting nodes, and node-count bound.

## Complexity Explanation Checklist

When a problem asks for time or space complexity, include:

1. The input-size parameter.
2. The algorithmic object being simulated or searched.
3. The exact information stored at one time.
4. The size of each stored item.
5. The number of stack/recursion/nesting levels if any.
6. A final asymptotic bound and class conclusion.

For space complexity, explicitly say when time can be exponential but space remains small.

## 8.24-Style Construction Checklist

For problems that construct small expressions with a large first disagreement:

1. Pick a unary alphabet if allowed.
2. Choose moduli whose product is exponential, usually the first `n` primes.
3. Build one expression that accepts all lengths except multiples of each chosen modulus.
4. Prove the expression size is polynomial using a bound on the moduli.
5. Prove every length below the product is accepted because it misses at least one modulus.
6. Show the product length is rejected by one expression and accepted by the other.
7. State the resulting exponential lower bound on the first distinguishing string.
