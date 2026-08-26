# Mathforge Book Catalog

## Purpose

This catalog routes curriculum planning and challenge design through the books
stored in this repository. It is not a replacement for reading the relevant
chapter. It records enough metadata to answer four questions quickly:

1. Which source should guide the topic order?
2. Which source contains useful problem families?
3. Which source can validate definitions or edge cases?
4. Which source contains hints or solutions and therefore requires extra care?

The required research order is:

> identify the next learning step → consult this catalog → inspect local books →
> adapt an original programming challenge → use the internet for remaining gaps

All chapter references below were checked against the PDFs currently stored in
`books/`.

## Source-use policy

- Books guide curriculum and inspire challenges; they do not override student
  evidence or Mathforge's one-step progression.
- Extract a problem's mathematical structure, not its wording.
- Do not copy distinctive narratives, diagrams, datasets, or long subquestion
  sequences.
- Mark solution-bearing sources and do not leak their derivations.
- Use chapter-level references in provisional plans when an exact exercise
  citation would reveal the solution path.
- Record material sources in each module's `PROBLEMS.md`.
- Consult current primary internet sources directly when a challenge depends on
  current facts or specifications.

## Quick routing table

| Source | Primary curriculum use | Problem-source value | Hints or solutions | PDF text search |
| --- | --- | --- | --- | --- |
| *Discrete Mathematics: An Open Introduction* | foundations, counting, logic, graphs | High | Selected hints and solutions | Good |
| *Proofs: A Long-Form Mathematics Textbook* | proof, logic, sets, functions, relations | High | No solution section identified | Good |
| *A Practical Theory of Programming* | specification, functions, invariants, program reasoning | High, but notation is specialized | Exercise chapter; no separate manual identified | Good |
| *Concrete Mathematics* | recurrences, sums, number theory, combinatorics, asymptotics | High and advanced | Answer appendix | Good, with imperfect OCR characters |
| *Problems on Algorithms* | algorithm design, analysis, correctness, data structures | Very high | Hints and solutions in each chapter | Good |
| *Probability and Random Processes* | probability and stochastic-process sequence | High and advanced | Problems; no separate answer source identified | Image-only scan |
| *Graph Theory with Applications* | graph-theory sequence and classical applications | High | Exercises and a hints appendix | Image-only scan |
| *Linear Algebra* | full linear-algebra sequence and applications | High | Separate answer volume available | Good |
| *Linear Algebra — Answers to Exercises* | answer validation only | Not a primary problem source | Full companion answer volume | Good |
| *Evaluating Large Language Models in Scientific Discovery* | scientific-evaluation methodology | Low for core mathematics; useful for later research projects | Not applicable | Good |

## Recommended routing by curriculum area

### Mathematical foundations and Module 01

Use, in order:

1. Oscar Levin for a gentle sequence through statements, sets, and functions.
2. Jay Cummings for deeper treatment of logic, proof, functions, and relations.
3. Eric Hehner for the bridge from predicates and functions to specifications,
   program behavior, and invariants.

### Combinatorics and discrete techniques

Use Oscar Levin first for introductory counting and recurrence structure. Use
*Concrete Mathematics* for deeper recurrence, summation, number-theoretic,
generating-function, probability, and asymptotic techniques. Use *Problems on
Algorithms* when the concept should become an algorithmic design problem.

### Algorithms and data structures

Use *Problems on Algorithms* as the principal problem repository and sequence
guide. Use Eric Hehner for correctness, specifications, time, space,
termination, recursion, and abstract data structures. Use *Concrete Mathematics*
for recurrence and asymptotic tools required by the analysis.

### Probability and stochastic processes

Use Grimmett and Stirzaker as the main long-range sequence. Use Oscar Levin and
*Concrete Mathematics* for gentler discrete-probability entries and
combinatorial examples.

### Graphs and networks

Use Oscar Levin for an introductory entry and Bondy and Murty for the main
classical graph-theory progression, exercises, and applications.

### Linear algebra

Use Jim Hefferon's textbook as the primary curriculum and problem source. Use
the separate answers volume only after independent analysis, for validation and
test-authoring checks.

## Catalog entries

### Discrete Mathematics: An Open Introduction

- **Author:** Oscar Levin
- **Edition:** Third edition, fifth printing, 2021
- **File:** [`discrete_math_oscar_levin.pdf`](discrete_math_oscar_levin.pdf)
- **Type:** Open introductory textbook
- **License noted in the PDF:** Creative Commons Attribution-ShareAlike 4.0
- **Searchability:** Good text layer
- **Difficulty:** Introductory undergraduate
- **Primary roles:** Curriculum source, problem source, reference source
- **Solution warning:** Includes Appendix A, selected hints, and Appendix B,
  selected solutions

**Major sequence.** Introduction and preliminaries; mathematical statements;
predicates and quantifiers; sets; functions; counting; binomial coefficients;
permutations and combinations; inclusion-exclusion; sequences; recurrences;
induction; symbolic logic and proofs; graph theory; additional discrete topics.

**Best Mathforge uses.** Modules 01 and 02; introductory probability; early
proof habits; finite-state and counting challenges; introductory graph models.
Its progression is especially useful for deciding which foundations should
precede combinatorics.

**Notable chapter routing.** Sections 0.2–0.4 cover statements, sets, and
functions; Chapter 1 covers counting; Chapter 2 covers sequences, recurrences,
and induction; Chapter 3 covers symbolic logic and proofs; Chapter 4 begins
graph theory.

### Proofs: A Long-Form Mathematics Textbook

- **Author:** Jay Cummings
- **PDF metadata:** Math 108 Course Notes, Spring 2020
- **File:** [`proofs_mathematics.pdf`](proofs_mathematics.pdf)
- **Type:** Proof-oriented textbook and course notes
- **Searchability:** Good text layer
- **Difficulty:** Introductory proof course
- **Primary roles:** Curriculum source, problem source, reference source
- **Solution warning:** No dedicated solution section was identified in this PDF

**Major sequence.** Intuitive proofs and the pigeonhole principle; direct proof;
sets; induction; logic; contrapositive; contradiction; functions; cardinality;
relations; introductory group theory.

**Best Mathforge uses.** Counterexamples, invariants, proof explanations, sets,
quantifier reasoning, function properties, equivalence relations, and oral-review
questions after implementation. The exercise sets are useful when a programming
challenge needs a precise mathematical micro-problem first.

**Notable chapter routing.** Chapter 3 covers sets, including power sets and
Cartesian products; Chapter 5 covers statements, truth tables, quantifiers, and
negations; Chapter 8 covers functions, composition, and invertibility; Chapter 9
covers equivalence relations.

### A Practical Theory of Programming

- **Author:** Eric Hehner
- **File:** [`a_pratical_theory_of_programming.pdf`](a_pratical_theory_of_programming.pdf)
- **Type:** Programming theory and formal-methods textbook
- **Searchability:** Good text layer, with some imperfect extracted symbols
- **Difficulty:** Intermediate to advanced; uses a distinctive formal notation
- **Primary roles:** Curriculum source, problem source, reference source
- **Solution warning:** Contains a large exercise chapter and reference laws; no
  separate solution manual was identified

**Major sequence.** Binary theory and proof rules; basic data structures; set,
string, and list theories; functions and quantifiers; program specifications and
refinement; time, space, and termination; linear and binary search; programming
language constructs; assertions and backtracking; recursive definitions; stack,
queue, and tree theories; concurrency; interaction and communication.

**Best Mathforge uses.** Translating mathematical predicates into program
specifications; preconditions and postconditions; invariants; termination;
search; time and space reasoning; reusable data-structure engines; later
concurrency and interaction challenges.

**Caution.** Adapt the underlying idea into ordinary Python and Mathforge
notation. Do not make mastery of the book's specialized formal language a hidden
prerequisite unless a future module explicitly chooses to study it.

### Concrete Mathematics: A Foundation for Computer Science

- **Authors:** Ronald L. Graham, Donald E. Knuth, and Oren Patashnik
- **Edition:** Second edition, 1994
- **File:** [`Concrete Mathematics`](<Concrete Mathematics A Foundation for Computer Science~tqw~_darksiderg.pdf>)
- **Type:** Advanced mathematics-for-computer-science textbook
- **Searchability:** Searchable text with imperfect character extraction
- **Difficulty:** Intermediate to advanced undergraduate
- **Primary roles:** Curriculum source, problem source, reference source
- **Solution warning:** Appendix A contains answers to exercises

**Major sequence.** Recurrent problems; sums; integer functions; number theory;
binomial coefficients; special numbers; generating functions; discrete
probability; asymptotic methods.

**Best Mathforge uses.** Recurrence-driven challenges; exact summation;
floor-and-ceiling algorithms; number theory; combinatorial identities;
generating functions; hashing and discrete probability; analysis of algorithms.

**Notable chapter routing.** Chapter 1 begins with recurrence through Tower of
Hanoi, planar lines, and Josephus; Chapters 2–4 develop sums, integer functions,
and number theory; Chapters 5–7 develop binomial and generating-function tools;
Chapter 8 covers discrete probability and hashing; Chapter 9 covers asymptotics.

### Problems on Algorithms

- **Authors:** Ian Parberry and William Gasarch
- **Edition:** Second edition, July 2002
- **File:** [`problems_on_algorithms.pdf`](problems_on_algorithms.pdf)
- **Type:** Problem collection for algorithm design, analysis, and verification
- **Searchability:** Good text layer
- **Difficulty:** Undergraduate through beginning graduate
- **Primary roles:** Principal algorithm problem source, curriculum source,
  reference source, solution source
- **Solution warning:** Most chapters contain explicit hints, solutions, and
  comments

**Major sequence.** Mathematical induction; asymptotic notation; recurrence
relations; correctness proofs; algorithm analysis; divide and conquer; dynamic
programming; greedy algorithms; exhaustive search and backtracking; data
structures; NP-completeness; sorting, lower bounds, graph algorithms, maximum
flow, and matrix reductions.

**Best Mathforge uses.** The dedicated algorithmic modules and algorithmic
variants inside mathematical modules. Its organization by design technique is
particularly valuable for building families of progressively modified
challenges.

**Adaptation rule.** Because the book is explicitly a problem repository and
contains solutions, independently identify the concept before reading a
solution, substantially rewrite every selected structure, and avoid exact
exercise citations in active challenge READMEs.

### Probability and Random Processes

- **Authors:** Geoffrey R. Grimmett and David R. Stirzaker
- **Edition:** Third edition, Oxford University Press, 2001
- **File:** [`Probability and Random Processes`](<[Geoffrey_R._Grimmett,_David_R._Stirzaker]_Probabi(BookZZ.org).pdf>)
- **Type:** Comprehensive probability and stochastic-process textbook
- **Searchability:** Image-only scan; visual inspection is required
- **Difficulty:** Intermediate to advanced undergraduate
- **Primary roles:** Long-range curriculum source, problem source, reference
  source
- **Solution warning:** Contains chapter problems; no separate answer source was
  identified in the repository

**Major sequence.** Events and probabilities; random variables and their
distributions; discrete random variables; continuous random variables;
generating functions and applications; Markov chains; convergence of random
variables; random processes; stationary processes; renewals; queues; martingales;
diffusion processes; appendices on foundations, simulation, and tables.

**Best Mathforge uses.** The deep probability sequence, random variables,
limit behavior, Monte Carlo prerequisites, stochastic processes, Markov chains,
queues, martingales, and diffusion. Its ordering is a primary reference for
long-term dependency planning, but the opening Mathforge challenges should be
smaller and more computationally explicit.

### Graph Theory with Applications

- **Authors:** J. A. Bondy and U. S. R. Murty
- **Publication:** North-Holland, 1976
- **File:** [`Graph_Theory_Bondy_Murty.pdf`](Graph_Theory_Bondy_Murty.pdf)
- **Type:** Classical graph-theory textbook
- **Searchability:** Image-only scan; visual inspection is required
- **Difficulty:** Intermediate undergraduate
- **Primary roles:** Curriculum source, problem source, reference source
- **Solution warning:** Contains exercises and an appendix of hints; no complete
  solution source was identified

**Major sequence.** Graphs and subgraphs; trees; connectivity; Euler tours and
Hamilton cycles; matchings; edge colorings; independent sets and cliques; vertex
colorings; planar graphs; directed graphs; networks; cycle and bond spaces.

**Best Mathforge uses.** The main graph-theory module sequence, classical
counterexamples, structural invariants, routing and network problems, matching,
coloring, planarity, directed-state models, and flow-related preparation.

**Adaptation note.** Many exercises are stated as pure graph problems. Preserve
the graph structure while introducing a programming interface and a realistic
domain only when the context clarifies rather than obscures the graph.

### Linear Algebra

- **Author:** Jim Hefferon
- **Edition:** Fourth edition, PDF dated April 2020
- **File:** [`linear_algebra.pdf`](linear_algebra.pdf)
- **Type:** Open developmental textbook
- **Searchability:** Good text layer
- **Difficulty:** Undergraduate; assumes some calculus but develops proof
  maturity gradually
- **Primary roles:** Principal linear-algebra curriculum source, problem source,
  reference source
- **Solution warning:** A separate answers volume is stored alongside it

**Major sequence.** Linear systems and Gaussian reduction; linear geometry;
reduced echelon form; vector spaces; linear independence; basis and dimension;
linear maps; matrix operations; change of basis; projection; determinants;
similarity; diagonalization; eigenvalues and eigenvectors; Jordan form.

**Best Mathforge uses.** Manual matrix and vector implementations; numerical
thinking around elimination; transformations; geometry; Markov chains;
least-squares ideas; computer graphics; stable populations; PageRank; linear
recurrences.

**Notable application topics.** Accuracy of computations, network analysis,
voting paradoxes, line of best fit, geometry of linear maps, Markov chains,
computer graphics, stable populations, PageRank, and coupled oscillators.

### Linear Algebra — Answers to Exercises

- **Author:** Jim Hefferon
- **File:** [`linear_algebra_answers.pdf`](linear_algebra_answers.pdf)
- **Type:** Companion answer volume
- **Searchability:** Good text layer
- **Difficulty:** Matches the main textbook
- **Primary role:** Solution source for validation only
- **Solution warning:** This entire volume contains answers

**Use policy.** Do not use this volume as the first source for designing a
challenge. Form the problem, mathematical expectation, and tests independently;
then consult the relevant answer only when validation is useful. Never copy its
derivation into a challenge or hint without an explicit student request for a
full solution after serious effort.

### Evaluating Large Language Models in Scientific Discovery

- **Authors:** Zhangde Song and many collaborators
- **Version:** arXiv:2512.15567v1, December 17, 2025
- **File:** [`2512.15567v1.pdf`](2512.15567v1.pdf)
- **Type:** Research paper
- **Searchability:** Good text layer
- **Difficulty:** Research-level and multidisciplinary
- **Primary roles:** Reference source for evaluation design and later integrated
  research projects
- **Solution warning:** Not applicable

**Scope.** Introduces a scenario-grounded framework for evaluating large
language models on scientific-discovery tasks across multiple scientific
domains, including project-level hypothesis, simulation or experiment design,
and result interpretation.

**Best Mathforge uses.** It is not a primary source for the core mathematical
sequence. It may inform later challenge-evaluation methodology, scientific
workflow simulations, benchmark design, experimental reasoning, and Mega Boss
Challenges involving AI-assisted research.

## Catalog maintenance

When a book is added, removed, or replaced:

1. verify its title, author, edition, and file format;
2. inspect its table of contents rather than inferring scope from the filename;
3. identify whether it contains hints or solutions;
4. record its searchability and any special access limitation;
5. map it to curriculum areas and source roles;
6. update affected module source maps.

Do not rename externally titled works merely to normalize their language. File
renaming may be considered separately when it improves maintainability and does
not break references.

## Current curriculum source gaps

The local collection gives especially strong coverage of discrete mathematics,
proof, programming theory, algorithms, combinatorics, probability, random
processes, graph theory, and linear algebra. It does not yet provide a dedicated
primary textbook for every field in the complete roadmap.

The most important current gaps are:

- geometry and trigonometry;
- abstract algebra;
- automata, formal languages, and computability;
- calculus, differential equations, and mathematical analysis;
- numerical analysis and scientific computing;
- mathematical statistics and experimental design;
- Bayesian inference and causal inference;
- network science;
- optimization and operations research;
- decision theory, game theory, MDPs, and bandits;
- dynamical systems and control theory;
- information theory;
- concurrency and distributed or reactive systems beyond Hehner's introductory
  treatment.

A source gap does not remove a module from the roadmap. Before planning such a
module, first recheck the catalog for newly added books, then select current,
authoritative external sources according to the book-first research policy.
