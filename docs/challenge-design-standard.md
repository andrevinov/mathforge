# Mathforge Challenge Design Standard

## Purpose

This document defines how Mathforge modules and challenges are planned,
materialized, tested, and revised. It supplements `AGENTS.md`; if the two ever
conflict, `AGENTS.md` is authoritative.

The central idea is progressive deliberate practice. A module may eventually
contain difficult integrated problems, but the student reaches them through a
sequence of small conceptual increments.

## 1. The unit of progression

The unit of progression is not a file, formula, or chapter. It is one observable
mathematical capability implemented in code.

A challenge should normally introduce exactly one main new concept. A very
small group of concepts may be introduced together only when separating them
would create an artificial exercise or make either concept unintelligible. The
module plan should state why the group is inseparable.

Every challenge has two layers:

- **new material:** the single conceptual increment being introduced;
- **retrieval material:** concepts already studied that must be recognized and
  used again.

Retrieval material should grow over time, but it must not obscure the new
learning objective in early challenges.

## 2. The difficulty staircase

Challenges within a module should follow a Kumon-like staircase. The difference
between neighboring challenges should be small enough to diagnose precisely,
but large enough to require new thought.

Use the difficulty levels from `AGENTS.md` as a long-range shape:

1. **Mechanical:** implement a definition directly.
2. **Basic application:** use it in a small, concrete situation.
3. **Interpretation:** recognize which concept applies.
4. **Composition:** combine multiple ideas from the current module.
5. **Cross-topic:** combine the module with previously mastered mathematics.
6. **Open problem:** choose the mathematical technique without being told.

These are not one-challenge stages. A module may need several challenges at one
level, and the plan may insert a smaller intermediate step whenever student work
reveals a gap.

Difficulty should accumulate through:

- one additional rule or constraint;
- a less convenient representation;
- a larger domain where brute force stops being viable;
- one new mathematical object;
- composition with a previously mastered capability;
- a requirement to justify correctness, error, or complexity;
- removal of an explicit hint about which technique applies.

Difficulty should not come from unrelated boilerplate, frameworks, obscure
syntax, unnecessarily long stories, or hidden requirements.

## 3. Choosing problem contexts

Prefer challenges that resemble actual programming problems. Useful contexts
include:

- validating rules or configurations;
- processing and summarizing data;
- scheduling tasks or allocating resources;
- searching a state space;
- simulating uncertain systems;
- measuring reliability or risk;
- implementing game mechanics;
- routing through a network;
- ranking or recommending alternatives;
- testing whether an algorithm behaves as claimed.

The context must serve the mathematics. Do not add databases, APIs, user
interfaces, frameworks, or architecture unless they are part of the actual
learning objective.

A narrowly mathematical exercise is appropriate when:

- the concept is too small to recognize inside a realistic system;
- a direct implementation is needed before application;
- a misconception needs an isolated counterexample;
- exhaustive testing requires a tiny domain;
- a future realistic problem would otherwise introduce several new ideas at
  once.

A story is optional. If used, it should clarify the input, rules, or desired
behavior rather than conceal them.

## 4. Module problem plans

### When the plan is created

Create a module's `PROBLEMS.md` when the student announces that study of the
module is beginning. Create it before materializing the first challenge.

The plan describes a probable sequence. It is not a promise that every listed
challenge will be used, and it is not permission to create every challenge
directory in advance.

### Required plan contents

The plan begins with:

- the module name and purpose;
- prerequisites from earlier modules;
- a `Curriculum Sources` section naming relevant local books and chapters;
- the module's major mathematical milestones;
- the capabilities that would demonstrate module mastery;
- future fields that depend on the module.

Each proposed problem contains:

```markdown
## NN — Working problem title

**Status:** Planned

**Problem idea:** A short description of the programming problem or context.

**New concept:** The single main mathematical increment.

**Reinforces:** Previously studied concepts exercised again.

**Prerequisites:** What the student must understand or be able to implement
before attempting this problem.

**Why this step is next:** Why it is exactly one step above prior work.

**Likely variants:** One or two natural changes or extensions.

**Reuse:** Whether the problem is standalone, modifies a previous solution, or
imports a previously completed component.

**Source basis:** The local books, chapters, external sources, or original
synthesis that materially shaped the problem. Withhold an exact exercise number
when it would disclose the solution path.
```

The plan must not contain:

- the final derivation;
- the decisive formula when discovering it is part of the exercise;
- the complete algorithm;
- pseudocode that effectively solves the problem;
- implementation code;
- test cases designed to disclose the solution strategy.

### Plan status and revision

Recommended problem statuses are:

- `Planned`;
- `Active`;
- `Completed`;
- `Revised`;
- `Skipped`.

After each completed challenge, review the plan. Student evidence may justify:

- inserting a smaller prerequisite challenge;
- selecting one of the planned variants;
- repeating the same concept in a new context;
- increasing the next challenge's integration level;
- removing a redundant challenge;
- changing reuse into a standalone problem, or the reverse.

Planning ahead must never override difficulty regulation.

## 5. Variant design

Whenever a challenge is designed, immediately identify one or two variants.
Variants make deliberate practice cumulative and reduce the temptation to jump
to an unrelated exercise.

Useful variant types include:

- **constraint variant:** add or change one rule;
- **representation variant:** express the same structure differently;
- **scale variant:** make exhaustive enumeration impractical;
- **inverse variant:** reconstruct inputs or parameters from outputs;
- **streaming variant:** process values without storing the entire input;
- **weighted variant:** replace uniform cases with unequal weights;
- **uncertainty variant:** replace exact data with samples or estimates;
- **composition variant:** combine the mechanism with earlier mathematics;
- **engine extension:** reuse or modify the previous implementation;
- **domain transfer:** apply the same mathematical structure to a new realistic
  setting without naming the technique.

A variant should normally change one meaningful dimension. If it changes
several dimensions, reserve it for a composition challenge, Boss Challenge, or
later milestone.

## 6. Materializing a challenge

Do not create a challenge folder merely because it appears in `PROBLEMS.md`.
Materialize it only when the student explicitly requests the first or next
problem in the active module.

Create exactly one directory at a time:

```text
modules/
└── NN-module-name/
    ├── PROBLEMS.md
    └── problems/
        └── NN-problem-name/
            ├── README.md
            ├── tests/
            │   └── test_solution.py
            └── solution.py
```

At creation time:

- `README.md` contains the complete behavioral specification;
- `tests/test_solution.py` contains the comprehensive test suite;
- `solution.py` is completely empty and belongs to the student;
- `PROBLEMS.md` marks the problem as `Active`;
- no future problem directory is created.

If the repository later develops packaging needs that require a minimal file
instead of a literally empty one, change the convention explicitly before using
it. Do not silently place implementation hints or stubs in `solution.py`.

## 7. Challenge README standard

The README explains the software behavior in detail while withholding the
mathematical solution.

### Required sections

```markdown
# Problem title

## Context

The real or fictional situation, when useful.

## Problem

The exact behavior the student must implement.

## Mathematical Goal

The concept being exercised, named but not derived.

## Constraints

Allowed tools, prohibited shortcuts, complexity expectations, mutation rules,
numeric requirements, and input-validity assumptions.

## Interface

Required functions or classes, signatures, inputs, outputs, and documented
exceptions.

## Examples

A few examples that clarify the contract without revealing the general
solution.

## Completion Criteria

The observable and explanatory requirements for completion.
```

Add a `Prerequisites` section when the challenge depends on material that the
student may need to review. It should identify concepts to research, not explain
how those concepts solve the challenge.

### Required clarity

The README must make these matters unambiguous whenever relevant:

- accepted input domain;
- return types and data representation;
- whether order matters;
- how duplicates are treated;
- behavior for empty and boundary inputs;
- invalid-input behavior;
- whether inputs may be mutated;
- exact versus approximate numeric behavior;
- reproducibility requirements;
- relevant performance limits.

### Forbidden solution disclosure

Unless the student explicitly requests the corresponding hint level, do not
include:

- the full derivation;
- the formula whose discovery is the central lesson;
- the algorithm or exact sequence of operations;
- pseudocode;
- implementation fragments;
- a worked example that generalizes directly into the complete solution.

The Agent may teach prerequisite mathematics separately. Such teaching should
use examples distinct from the active problem when practical and should stop
short of mapping every conceptual step onto the implementation.

## 8. Test design standard

Tests are part of the curriculum and form an executable statement of the
problem contract. They must be written before the student implementation.

### Coverage model

For each challenge, build a test inventory covering:

1. interface existence and basic types;
2. direct examples from the README;
3. the smallest meaningful inputs;
4. empty, singleton, and boundary cases when valid;
5. each branch of specified behavior;
6. invalid or pathological inputs when relevant;
7. mathematical invariants;
8. interactions among features;
9. numeric accuracy and stability when relevant;
10. performance constraints only when they are part of the lesson.

### Exhaustiveness

“Exhaustive” depends on the domain:

- For a small finite domain, enumerate every valid input or state.
- For a partitioned domain, cover every equivalence class and every boundary.
- For a large or infinite domain, combine representative examples with
  invariant checks and deterministic generated cases.
- For a probabilistic implementation, use fixed seeds, controlled random
  sources, statistical bounds justified by the contract, or exact checks on the
  deterministic mechanism beneath the sampling.

Never write a flaky test. A probabilistic test that merely “usually passes” is
not acceptable.

### Invariants

Prefer invariants that expose the mathematics. Depending on the challenge, they
may include:

- counts are nonnegative integers;
- probabilities are nonnegative and sum to one;
- partitions are disjoint and complete;
- an operation preserves size, order, symmetry, or another defined property;
- two independently derived forms agree;
- results remain unchanged under a valid permutation or relabeling;
- a conserved quantity remains constant;
- an approximation stays within a justified error bound;
- increasing the domain changes results according to a proven relationship.

Do not assert an invariant that the student has not learned unless the README
states it as part of the contract.

### Testing the contract, not one implementation

Tests should accept any correct implementation that satisfies the stated
constraints. Do not require private helper names, a specific loop structure, or
an incidental internal representation.

When an implementation technique is prohibited because it hides the
mathematics, enforce that constraint only with a robust check. If robust
automatic enforcement would be brittle, make it an explicit review item rather
than pretending the test suite can prove it.

Because `solution.py` starts empty, tests should fail clearly when the required
interface is absent. Prefer importing the module and reporting a meaningful
missing-interface failure over an obscure test-collection crash.

## 9. Reusing earlier implementations

Reuse is encouraged when it makes the mathematical progression visible. A
later challenge may import a completed engine, extend its behavior, or modify
its model.

Use reuse when:

- the earlier component has been completed and reviewed;
- rebuilding it would add no mathematical practice;
- the dependency makes the new conceptual increment clearer;
- the tests can state the dependency explicitly;
- the earlier challenge remains an intact historical record.

Avoid reuse when it would:

- make the active challenge fail for reasons unrelated to its learning goal;
- require premature packaging or infrastructure;
- couple many challenge directories together;
- hide mathematics that should be implemented again;
- turn a twenty-line mathematical exercise into an architecture task.

The module plan must identify reuse before the challenge is materialized.

## 10. Book-first research and source provenance

The local collection in `books/` is the primary source for curriculum structure
and challenge inspiration. Its routing index is
[`books/CATALOG.md`](../books/CATALOG.md), and module-level source gaps are
tracked in [`books/MODULE_COVERAGE.md`](../books/MODULE_COVERAGE.md).

### Research cycle

For module planning and challenge design:

1. **Locate the learning step.** Determine the active milestone, mastered
   prerequisites, and single next conceptual increment before selecting a
   source.
2. **Route through the catalog.** Use `books/CATALOG.md` to identify primary,
   secondary, and solution-bearing sources relevant to the step, and check
   `books/MODULE_COVERAGE.md` for known limitations.
3. **Inspect local books.** Review relevant tables of contents, prerequisite
   order, exposition, examples, exercises, hints, applications, and edge cases.
4. **Compare sources when useful.** A second author may expose a missing
   prerequisite, a gentler ordering, or a more revealing problem family.
5. **Extract structure, not wording.** Identify the mathematical object,
   constraint, misconception, or progression embodied by a useful exercise.
6. **Adapt to programming.** Create an original problem with an explicit
   software contract, realistic context when useful, exhaustive tests where
   feasible, and exactly one main conceptual increment.
7. **Design variants.** Produce one or two nearby extensions before searching
   for an unrelated problem.
8. **Use the internet as a second source tier.** Search externally only when the
   books lack adequate coverage, realistic context, variants, pathological
   cases, datasets, or current official information.
9. **Record provenance.** Update the module source map and the planned problem's
   `Source basis` field.

The cycle begins with curriculum position rather than a book. A book's chapter
order is evidence about prerequisites, not permission to override the student's
demonstrated needs or Mathforge's one-step progression.

### Source roles

Use local sources in distinct roles:

- **curriculum source:** guides topic selection, prerequisites, and ordering;
- **problem source:** contributes the structure of an exercise or family of
  exercises;
- **reference source:** validates definitions, derivations, invariants, or edge
  cases;
- **solution source:** validates the Agent's reasoning or tests after independent
  analysis.

A source may fill several roles. Solution-bearing sources must be clearly marked
in the catalog and module plan.

### Adaptation and copyright

Do not copy a problem statement verbatim or reproduce distinctive narrative,
datasets, diagrams, or a long sequence of subquestions. Preserve the useful
mathematical structure, then rewrite the task as an original English programming
challenge with Mathforge's interface, constraints, variants, and tests.

Follow these rules:

- respect each source's copyright and license;
- use only short quotations when a quotation is genuinely necessary;
- cite a source when a definition, dataset, or distinctive construction is
  materially retained;
- do not reproduce a book's solution, derivation, or pseudocode;
- do not let a citation in the active README reveal the solution path;
- withhold exact exercise numbers until completion when necessary;
- prefer chapter- or topic-level references in a provisional `PROBLEMS.md`;
- add a more precise retrospective citation after completion when it is safe and
  useful.

If external internet research is needed, prefer primary and authoritative
sources. Recency is irrelevant for timeless mathematics but mandatory when the
problem depends on a current specification, dataset, law, API, or real-world
fact.

## 11. Challenge lifecycle

The normal lifecycle is:

1. The student begins a module.
2. The Agent identifies the curriculum position and consults the catalog and
   relevant local books.
3. The Agent creates or updates `PROBLEMS.md`, including its source map.
4. The student requests the first or next problem.
5. The Agent selects and, if necessary, adjusts exactly one planned step.
6. The Agent records likely variants and source provenance for later use.
7. The Agent creates the problem README, comprehensive tests, and empty
   `solution.py`.
8. The student researches the mathematics and implements the solution.
9. The Agent responds to requests using the graduated hint policy.
10. Tests are run and failures are treated as evidence about understanding.
11. After tests pass, the Agent reviews mathematical and software correctness.
12. The student explains the model, correctness, assumptions, complexity, and
    applications when the concept is important.
13. The problem is marked `Completed`, the module plan is revised, and the work
    is committed in a small historical step.
14. Only then is the next challenge selected.

At every stage, the objective is not merely to obtain passing code. It is to
make the mathematical mechanism recognizable, implementable, testable, and
reusable by the student.
