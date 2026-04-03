# Homework Problem Taxonomy and Solution Standards

This note classifies the exercises appearing in [main.pdf](/home/hlt/Coures_Master_S2/Theory_of_Computational/hws/homework/main.pdf) by their primary proof method.

Principle: each exercise is assigned one primary family, even if a few mixed problems use more than one technique.

## Family 1: Direct Proof and Elementary Verification

Exercises: 0.4, 0.10, 3.10, 4.6, 5.13, 7.1, 7.2, 7.5, 8.3, 10.2.

Use this family when the problem asks for a short argument, a direct calculation, a combinatorial count, a degree argument, a growth comparison, a satisfiability check, or a concrete verification.

Standard:
1. State exactly what must be shown.
2. Expand the relevant definition immediately.
3. Carry out the computation or argument in the simplest possible order.
4. If the claim is existential, exhibit the object explicitly.
5. If the claim is universal, handle an arbitrary element or arbitrary input.
6. End with a sentence that matches the original claim verbatim in substance.

Common failure modes:
- Skipping the definition and arguing only by intuition.
- Giving the correct answer without the key justification.
- Mixing examples with proofs of a universal statement.

## Family 2: Error Diagnosis and Counterexample

Exercises: 0.11, 0.13, 1.15, 1.30, 3.6, 5.17.

Use this family when the problem asks where a proof fails, why a construction is invalid, or why a proposed shortcut does not work.

Standard:
1. Quote or restate the exact step where the argument first becomes invalid.
2. Name the hidden assumption that fails.
3. Explain why that assumption is false in this setting.
4. If appropriate, give a minimal counterexample.
5. Conclude by stating precisely why the proof or construction does not establish the claim.

Common failure modes:
- Saying only “this step is wrong” without explaining why.
- Pointing to a later consequence instead of the first invalid step.
- Giving a counterexample without tying it back to the logical failure.

## Family 3: Model Construction

Exercises: 0.7, 1.4, 1.5, 1.6, 1.7, 1.13, 1.42, 2.4, 2.6, 2.10, 2.33, 3.8, 6.22, 8.13, 9.7, 9.12, 10.4, 10.13.

Use this family when the task is to build a DFA, NFA, CFG, PDA, TM, regular expression, circuit, branching program, relation, or some other formal object.

Standard:
1. State the target object and the language or property it must realize.
2. Explain the invariant behind the construction before listing transitions or rules.
3. Present the object completely and unambiguously.
4. Prove correctness in two directions:
   accepted or generated implies desired property;
   desired property implies accepted or generated.
5. If the problem asks for a size bound, justify the number of states, rules, or gates explicitly.

Common failure modes:
- Presenting a construction without its governing idea.
- Omitting one transition, rule, or boundary case.
- Arguing only that the construction “seems right” instead of proving correctness.

## Family 4: Model Conversion and Normalization

Exercises: 0.9, 1.11, 1.17, 1.19, 2.14, 9.8.

Use this family when the task is to translate one formal representation into another equivalent one, or to normalize a representation.

Standard:
1. Name the source object and the target formalism.
2. State the conversion rule or theorem being used.
3. Apply the conversion step by step, preserving equivalence at each stage.
4. Verify that the target object satisfies the required normal-form conditions.
5. Conclude with an explicit equivalence statement.

Common failure modes:
- Applying a conversion theorem without checking its hypotheses.
- Producing the target form without proving equivalence.
- Forgetting special cases such as $\varepsilon$, empty language, or unreachable states.

## Family 5: Language and Grammar Analysis

Exercises: 1.53, 2.8, 2.18, 2.22, 2.24.

Use this family when the core task is to understand what a grammar or language really describes, to prove ambiguity or unambiguity, to characterize a structural property, or to prove a grammar correct.

Standard:
1. Identify the hidden structural invariant of the language or grammar.
2. State the proposed characterization precisely.
3. Prove “every generated string has the property.”
4. Prove “every string with the property can be generated,” usually by induction on length or structure.
5. If ambiguity is involved, exhibit two distinct derivations or parse trees for one string.
6. If unambiguity is claimed, show why the first production choice is forced.

Common failure modes:
- Describing the language informally but never proving the description.
- Showing only one derivation when two are required.
- Forgetting to prove the converse direction.

## Family 6: Closure, Simulation, and Structural Equivalence

Exercises: 1.14, 1.32, 1.34, 1.35, 1.36, 2.16, 2.19, 2.32, 3.12, 3.15, 3.18, 3.20, 4.23, 6.3, 6.7, 7.7, 8.1.

Use this family when the problem asks whether a language class is closed under an operation, whether two machine models are equivalent, or whether one computation can simulate another.

Standard:
1. State the closure or simulation claim in exact formal terms.
2. Start with arbitrary objects from the given class.
3. Construct a new object that performs the required operation or simulation.
4. Prove correctness by tracing what happens on an arbitrary input.
5. If the claim is negative, give a counterexample and verify both sides carefully.

Common failure modes:
- Proving the construction only on examples.
- Confusing syntactic combination with semantic correctness.
- For negative closure claims, giving an example without proving it really is a counterexample.

## Family 7: Decidability and Recognizability

Exercises: 4.3, 4.4, 4.10, 4.15, 4.17, 4.27, 5.2, 5.24(a), 5.33, 6.14.

Use this family when the goal is to design a decider, recognizer, co-recognizer, or oracle procedure.

Standard:
1. Define the language precisely.
2. Present the algorithm at the right level of abstraction.
3. Prove termination.
4. Prove correctness in both directions.
5. If recognizability rather than decidability is the target, say explicitly which cases may run forever.
6. If an oracle is used, isolate exactly what query the oracle answers.

Common failure modes:
- Giving a procedure that works informally but may not halt.
- Proving soundness but not completeness.
- Using a theorem without explaining why its input instance can be built effectively.

## Family 8: Impossibility, Non-Membership, and Diagonal Lower Bounds

Exercises: 1.40, 1.52, 2.26, 2.44, 2.45, 4.12, 5.5, 6.10, 6.17.

Use this family when the target is a negative statement such as nonregularity, non-context-freeness, non-DCFL, nonseparability, or impossibility of a certain reduction.

Standard:
1. Choose the right negative method before writing:
   pumping lemma;
   closure plus known hard language;
   diagonalization;
   counting;
   contradiction from an assumed reduction.
2. State the assumption being contradicted.
3. Build the witness or diagonal object carefully.
4. Show exactly where the contradiction appears.
5. Conclude with the negative statement in full.

Common failure modes:
- Choosing a weak witness that does not force a contradiction.
- Forgetting to use all hypotheses of the negative method.
- Treating “not proved” as if it meant “false.”

## Family 9: Reductions, Hardness, and Completeness

Exercises: 5.9, 5.21, 5.22, 5.24(b), 5.28, 7.23, 7.27, 7.28, 7.29, 7.30, 7.32, 7.34, 7.39, 8.20, 8.21, 8.28.

Use this family when the problem asks you to show undecidability, NP-completeness, NL-completeness, PSPACE-completeness, or hardness by a reduction.

Standard:
1. State the source problem and the target problem.
2. Explain why the source problem is already known to be hard.
3. Define the reduction map explicitly.
4. Prove the map is computable in the required resource bound.
5. Prove equivalence:
   yes-instance of source iff yes-instance of target.
6. For completeness, also prove target membership in the class.
7. Conclude with the exact hardness or completeness statement.

Common failure modes:
- Picking the wrong reduction direction.
- Describing the reduction informally but not defining it on arbitrary inputs.
- Proving only one direction of the iff statement.
- Forgetting the easy membership half of a completeness proof.

## Family 10: Complexity Upper Bounds, Algorithms, and Separations

Exercises: 6.4, 6.12, 7.9, 7.10, 7.14, 7.17, 7.36, 7.40, 7.42, 8.6, 8.10, 8.24, 8.30, 8.33, 9.2, 9.9, 9.16, 9.19, 9.23, 9.25, 10.7, 10.8, 10.10, 10.19.

Use this family when the goal is to place a problem in a complexity class, derive a time or space upper bound, prove a hierarchy or separation statement, or show an implication between classes.

Standard:
1. State the exact resource claim.
2. Choose the proof mechanism explicitly:
   algorithm design;
   dynamic programming;
   simulation;
   theorem application;
   oracle or diagonal argument;
   amplification.
3. Describe the algorithm or simulation cleanly.
4. Bound the time, space, size, or probability error step by step.
5. Justify every class inclusion used.
6. If the claim is a separation, identify the theorem or contradiction that forces strictness.

Common failure modes:
- Proving correctness without proving the resource bound.
- Writing the asymptotic bound but not deriving it.
- Invoking a hierarchy or oracle theorem without checking its conditions.

## Mixed Exercises

Some exercises genuinely combine two families.

- 1.17 mixes construction and conversion.
- 2.24 mixes language analysis, determinism testing, and PDA construction.
- 5.24 mixes recognizability and undecidability.
- 7.23 mixes construction and hardness.

In such cases, write the solution in stages and let each stage use the standard of its own family.

## Recommended Writing Order

For almost every problem in this homework set, the cleanest mathematician-style order is:

1. Restate the claim precisely.
2. Name the main method before using it.
3. Carry out the proof in a linear sequence of justified steps.
4. Separate construction from correctness proof.
5. End with a one-sentence conclusion that exactly answers the exercise.
