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
| *Calculus and Analytic Geometry* | introductory calculus, trigonometry, analytic geometry, vector calculus | Very high | Answers appendix | Image-only scan |
| *Advanced Calculus* | rigorous multivariable calculus and mathematical analysis | High and advanced | Exercises; no answer section identified | Good OCR text layer |
| *Differential Equations and Dynamical Systems* | nonlinear ODEs and dynamical systems | High and advanced | Exercises; separate manual mentioned but not stored | Good OCR text layer |
| *Numerical Methods in Scientific Computing* | numerical PDEs, modeling, iterative solvers, scientific computing | High and applied | Exercises and projects; no answer source identified | Good, with recoverable PDF warnings |
| *Mathematical Statistics* | estimation, testing, regression, ANOVA, nonparametrics, bootstrap | Very high | Exercises; separate solutions book mentioned but not stored | Good |
| *Elementary Decision Theory* | utility, Bayesian decisions, statistical decisions, sequential procedures | High | Partial exercise answers and derivations | Image-only encrypted scan |
| *Optimization Techniques in Operations Research* | mathematical programming, OR, scheduling, introductory games | Very high and applied | Solved examples and answer-bearing exercises | Good |
| *A Course in Game Theory* | strategic, extensive, repeated, Bayesian, and coalitional games | Very high and advanced | Challenging exercises; instructor solutions are not stored | Good |
| *Advanced Bayesian Monte Carlo Methods for Inference and Control* | advanced MCMC, inverse problems, Bayesian control | Specialized and research-level | Original research, proofs, and algorithms | Good |
| *Advanced Markov Chain Monte Carlo Methods: Learning from Past Samples* | MCMC foundations, adaptive and population methods, importance weighting | Very high and advanced | Exercises in every chapter; no answer source identified | Good |
| *Distributed Systems: Theory and Applications* | distributed algorithms, consensus, communication, consistency | High and applied | Exercises; no answer source identified | Good |
| *Bandit Algorithms for Website Optimization* | practical bandit introduction, simulation, and online experimentation | High and applied | Exercises and implementation examples; no answer source identified | Good |
| *Bandit Algorithms* | rigorous multi-armed bandits and sequential decision-making | Very high and advanced | Exercises and proofs; no answer source identified | Good |
| *Information Theory: A Tutorial Introduction* | intuitive first contact with information, entropy, and channel limits | Low for problems; high for orientation | No exercises or solutions | Good |
| *Introduction to Information Theory* | introductory source coding, channels, capacity, and error correction | High | Problems; no answer section identified | Searchable OCR with imperfections |
| *Elements of Information Theory* | comprehensive information-theory curriculum and advanced applications | Very high and advanced | Extensive problems; no answer section identified | Good |
| *A Mathematical Introduction to Control Theory* | classical and modern control, PID, state space, and Kalman filtering | Very high and applied | Selected exercise solutions | Good |
| *Mathematical Control Theory: An Introduction* | rigorous linear, nonlinear, optimal, and infinite-dimensional control | High and advanced | Exercises; no solution section identified | Searchable OCR with imperfections |
| *A First Course in Causal Inference* | potential outcomes, experiments, observational studies, and causal estimation | Very high | Homework throughout; instructor solutions are not stored | Good |
| *The Mathematics of Causal Inference in Statistics* | concise conceptual bridge from association to causation | Low for problems; high for orientation | No exercises or solutions | Searchable text with imperfect characters |
| *The Mathematics of Causal Inference* | structural causal models, graphical identification, and do-calculus | Low for problems; high for advanced orientation | No exercises or solutions | Good |
| *Automata Theory and Formal Languages* | automata, grammars, parsing, computability, and decidability | Very high | Exercises, including some worked solutions | Good |
| *Bayesian Inference in Statistical Analysis* | Bayesian foundations, priors, hierarchical models, and multivariate inference | High as an applied reference | Worked derivations and examples; no exercise section identified | Searchable OCR with imperfections |
| *Algebraic Structures of Symmetric Domains* | advanced algebraic groups, Jordan structures, Lie theory, and symmetric domains | High only after substantial prerequisites | Exercises; no solution section identified | Searchable OCR with imperfections |
| *Symmetry Approach to Integrability and Non-Associative Algebraic Structures* | integrable ODEs and PDEs, conservation laws, Hamiltonian operators, and non-associative algebras | Specialized and research-level | Selected exercises and open problems; no answer source identified | Good |

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

### Automata, formal languages, and semantics

Use Pettorossi as the principal source for grammars, regular languages, finite
automata, pushdown automata, context-free languages, parsing, Turing machines,
and decidability. Use Hehner alongside it for program semantics, recursive
execution, specifications, and the connection between formal descriptions and
program behavior. Use Parberry and Gasarch when reductions, complexity, or
concrete algorithm design should reappear.

### Abstract algebra and advanced symmetry

Cummings and *Concrete Mathematics* still provide only introductory group and
modular examples. Satake is useful much later for algebraic groups, Jordan
algebras and triple systems, Lie algebras, and symmetric spaces, but assumes a
sound background in Lie-group theory. Sokolov provides a different advanced
bridge from non-associative algebras and symmetry to integrable differential
equations, conservation laws, and Hamiltonian structure. Neither source
provides the gradual first course in groups, rings, fields, finite fields, and
homomorphisms required by Module 15. A dedicated introductory
abstract-algebra source is still needed.

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

### Calculus, analysis, differential equations, and scientific computing

Use Thomas and Finney as the main entry for trigonometry, analytic geometry,
single-variable calculus, series, multivariable calculus, and vector calculus.
Use Loomis and Sternberg only after that foundation, for rigorous analysis,
normed-space calculus, manifolds, integration, and advanced applications. Use
Perko for the qualitative theory of nonlinear ordinary differential equations
and dynamical systems. Use van Kan, Segal, and Vermolen for numerical modeling,
partial differential equations, discretization, iterative solvers, and
validation of scientific computations. Use Sokolov only as a far-later
research extension into integrable ODEs and PDEs, infinitesimal symmetries,
conservation laws, and Hamiltonian operators.

### Statistics, Bayesian computation, and decision theory

Use Pestman as the principal mathematical-statistics source. Use Chernoff and
Moses for the connection among utility, uncertainty, Bayesian strategies,
testing, estimation, and sequential decisions. Use Box and Tiao after the first
probability and likelihood milestones for noninformative priors, nuisance
parameters, Normal-theory inference, robustness, hierarchical designs,
multivariate models, and transformation of data. Sell's thesis is a later,
research-level source for MCMC, posterior-predictive applications, Bayesian
inverse problems, parallel sampling, and Bayesian control. Liang, Liu, and
Carroll provide the more systematic advanced-MCMC textbook sequence, including
Gibbs and Metropolis-Hastings methods, population methods, dynamic importance
weighting, stochastic-approximation Monte Carlo, and adaptive proposals.

### Monte Carlo and computational sampling

Use Grimmett and Stirzaker for probability, simulation, and the first Monte
Carlo pass. Use Liang, Liu, and Carroll Chapter 1 for Monte Carlo integration,
importance sampling, acceptance-rejection generation, and basic MCMC, then
Chapters 2–8 for advanced MCMC. Use Sell later for research-level Bayesian
sampling and inverse problems. The local collection still lacks a systematic
source for control variates, antithetic variables, stratified sampling,
rare-event estimation, sequential Monte Carlo, and particle filtering. The
word “sequential” in some adaptive-MCMC method names must not be treated as
coverage of the standard particle-based Sequential Monte Carlo curriculum.

### Optimization and operations research

Use Gupta as the principal applied source for linear and integer programming,
duality, sensitivity, transportation, assignment, dynamic programming,
nonlinear optimization, scheduling, and introductory zero-sum games. Combine it
with the algorithm and graph books when implementation, correctness, and
complexity need more depth.

### Game theory

Use Osborne and Rubinstein as the principal source for strategic games, Nash
equilibrium, mixed and correlated equilibrium, extensive games, repeated games,
imperfect information, Bayesian games, bargaining, implementation, and
coalitional games. Use Gupta first when a small zero-sum matrix game provides a
gentler computational entry, and use Chernoff and Moses for the bridge from
uncertainty and utility to games. Osborne and Rubinstein's exercises are often
deliberately difficult, so adapt their mathematical structure into Mathforge's
smaller conceptual steps.

### Multi-armed bandits and online decision-making

Use John Myles White as the practical first pass through exploration versus
exploitation, epsilon-greedy policies, softmax, UCB, simulation-based
evaluation, nonstationarity, and contextual extensions. Use Lattimore and
Szepesvári as the principal rigorous source for regret, concentration bounds,
stochastic and adversarial bandits, contextual and linear bandits, Thompson
sampling, pure exploration, and the bridge to Markov decision processes. The
second book assumes substantially more probability, linear algebra, analysis,
and proof maturity and should therefore guide later milestones rather than the
module's first exercises.

### Information theory

Use Stone's short tutorial for conceptual orientation and intuitive language.
Use Mansuripur as the introductory curricular bridge from probability to source
coding, mutual information, channels, capacity, error-correcting codes, and
rate distortion. Use Cover and Thomas as the principal rigorous and advanced
source for proofs, deeper problem families, continuous information measures,
information-theoretic statistics, universal coding, Kolmogorov complexity, and
network information theory. Do not begin with the advanced text when one of the
shorter sources can isolate the same first concept more cleanly.

### Control theory

Use Engelberg as the principal entry through transfer functions, feedback,
stability, frequency response, root locus, compensation, PID control, state
space, controllability, observability, discrete-time control, and Kalman
filtering. Use Zabczyk later for the rigorous structure of linear and nonlinear
systems, Lyapunov methods, optimal control, Bellman equations, the maximum
principle, and infinite-dimensional systems. Both texts rely heavily on
prerequisite calculus, differential equations, complex variables, and linear
algebra; their software examples must not replace manual implementation of the
mathematics in Mathforge challenges.

### Causal inference

Use Pearl's 2007 paper as a short conceptual entry into the distinction between
association and causation and into the need for causal notation. Use Ding as
the principal long-range textbook for potential outcomes, randomized
experiments, observational studies, estimation, sensitivity analysis,
instrumental variables, and mediation. Use Pearl's 2013 paper as the structural
and graphical complement for structural causal models, d-separation,
interventions, identifiability, do-calculus, mediation, transportability, and
missing data. The two frameworks should be connected explicitly rather than
taught as rival vocabularies.

### Concurrency and distributed systems

Use Hehner first for the mathematical semantics of concurrency and interaction.
Use Ghosh and Ghosh for distributed communication, event ordering, global state,
mutual exclusion, consensus, gossip, consistency, and distributed algorithms.

## Catalog entries

### Discrete Mathematics: An Open Introduction

- **Author:** Oscar Levin
- **Edition:** Third edition, fifth printing, 2021
- **File:** [`discrete_mathematics_open_introduction.pdf`](discrete_mathematics_open_introduction.pdf)
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
- **File:** [`proofs_long_form_mathematics_textbook.pdf`](proofs_long_form_mathematics_textbook.pdf)
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
- **File:** [`a_practical_theory_of_programming.pdf`](a_practical_theory_of_programming.pdf)
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
- **File:** [`concrete_mathematics.pdf`](concrete_mathematics.pdf)
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
- **File:** [`probability_and_random_processes.pdf`](probability_and_random_processes.pdf)
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
- **File:** [`graph_theory_with_applications.pdf`](graph_theory_with_applications.pdf)
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
- **File:** [`evaluating_llms_in_scientific_discovery.pdf`](evaluating_llms_in_scientific_discovery.pdf)
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

### Calculus and Analytic Geometry

- **Authors:** George B. Thomas, Jr. and Ross L. Finney, with Maurice D. Weir
- **Edition:** Ninth edition, 1996; reprinted with corrections, 1998
- **File:** [`calculus_and_analytic_geometry.pdf`](calculus_and_analytic_geometry.pdf)
- **Type:** Comprehensive introductory calculus textbook
- **Searchability:** Image-only scan; visual inspection is required
- **Difficulty:** Introductory undergraduate
- **Primary roles:** Principal calculus curriculum source, problem source,
  reference source
- **Solution warning:** Contains an answers appendix

**Major sequence.** Functions and trigonometry; limits and continuity;
derivatives and their applications; integration and applications; transcendental
functions; integration techniques; infinite series; conic sections and polar
coordinates; vectors and analytic geometry; motion in space; multivariable
derivatives; multiple integrals; vector fields.

**Best Mathforge uses.** Modules 23 and 28–31; coordinate and motion problems;
numerical differentiation and integration baselines; optimization; series and
approximation; multivariable models; vector-calculus simulations.

### Advanced Calculus

- **Authors:** Lynn H. Loomis and Shlomo Sternberg
- **Edition:** Revised edition, 1990; originally published in 1968
- **File:** [`advanced_calculus.pdf`](advanced_calculus.pdf)
- **Type:** Rigorous advanced-calculus and introductory-analysis textbook
- **Searchability:** Good OCR text layer, with occasional character errors
- **Difficulty:** Advanced undergraduate to beginning graduate
- **Primary roles:** Advanced curriculum source, proof source, problem source,
  reference source
- **Solution warning:** Contains extensive exercises; no answer section was
  identified in this PDF

**Major sequence.** Logic and sets; finite-dimensional vector spaces;
differential calculus on normed spaces; compactness and completeness; scalar
products; ordinary differential equations; multilinear algebra; integration on
Euclidean spaces; manifolds; exterior calculus; Fourier and Sturm–Liouville
ideas; differential geometry; potential theory; classical mechanics.

**Best Mathforge uses.** Modules 25 and 30–32; rigorous convergence and
continuity; fixed-point reasoning; multivariable calculus; differential
equations; advanced integration; later optional extensions involving manifolds,
tensors, Fourier methods, and mechanics. It is not the opening calculus text.

### Differential Equations and Dynamical Systems

- **Author:** Lawrence Perko
- **Edition:** Third edition, 2001
- **File:** [`differential_equations_and_dynamical_systems.pdf`](differential_equations_and_dynamical_systems.pdf)
- **Type:** Applied-mathematics textbook in the Springer TAM series
- **Searchability:** Searchable OCR with imperfect spacing
- **Difficulty:** Advanced undergraduate to beginning graduate
- **Primary roles:** Principal dynamical-systems source, advanced ODE source,
  problem source, reference source
- **Solution warning:** The book mentions a separate solution manual, but that
  manual is not stored in the repository

**Major sequence.** Linear systems; local theory of nonlinear systems;
existence, uniqueness, and dependence on initial data; flows and dynamical
systems; stable manifolds; phase-plane analysis; limit sets and periodic orbits;
global theory; bifurcation; structural stability; higher-dimensional behavior.

**Best Mathforge uses.** Modules 31 and 62; phase portraits; equilibrium and
stability experiments; nonlinear state evolution; bifurcation and sensitivity;
distinguishing genuine dynamics from numerical artifacts. It assumes prior
exposure to elementary differential equations.

### Numerical Methods in Scientific Computing

- **Authors:** Jos van Kan, Guus Segal, and Fred Vermolen
- **Edition:** Second edition, 2014; TU Delft OPEN edition, 2023
- **File:** [`numerical_methods_in_scientific_computing.pdf`](numerical_methods_in_scientific_computing.pdf)
- **Type:** Open scientific-computing and numerical-PDE textbook
- **License noted in the PDF:** Creative Commons Attribution 4.0
- **Searchability:** Good text layer; the PDF requires recoverable cross-reference
  reconstruction by some tools
- **Difficulty:** Intermediate to advanced applied mathematics
- **Primary roles:** Scientific-computing curriculum source, numerical-methods
  source, project source, reference source
- **Solution warning:** Contains exercises and projects; no answer source was
  identified in the repository

**Major sequence.** Mathematical modeling and conservation laws; partial
differential equations; finite differences; finite volumes; minimization and
variational formulations; finite elements; Galerkin methods; large linear
systems; preconditioning and Krylov methods; multigrid; nonlinear equations;
heat, wave, and transport equations; stability, accuracy, and validation.

**Best Mathforge uses.** Modules 26, 31, 32, and 42; sparse linear solvers;
discretization; convergence and stability experiments; explicit error budgets;
scientific model verification; later Boss Challenges involving physical systems.

### Mathematical Statistics

- **Author:** Wiebe R. Pestman
- **Edition:** Second revised edition, 2009
- **File:** [`mathematical_statistics.pdf`](mathematical_statistics.pdf)
- **Type:** Rigorous mathematical-statistics textbook
- **Searchability:** Good text layer
- **Difficulty:** Intermediate undergraduate; calculus and linear algebra are
  prerequisites for the proofs
- **Primary roles:** Principal statistics curriculum source, problem source,
  proof source, reference source
- **Solution warning:** Contains about 250 exercises. A separate detailed
  solutions book is mentioned but is not stored in the repository

**Major sequence.** Probability and a short measure-theory introduction;
estimation; Bayesian estimation; likelihood, information, and sufficiency;
hypothesis testing; normal regression; analysis of variance; nonparametric
statistics; stochastic methods in statistics; smoothing, robustness, density
estimation, and bootstrap; multivariate statistics.

**Best Mathforge uses.** Modules 08 and 33–40; estimators and likelihood;
confidence and testing; regression diagnostics; ANOVA; bootstrap; robust and
nonparametric variants; multivariate statistical computations.

### Elementary Decision Theory

- **Authors:** Herman Chernoff and Lincoln E. Moses
- **Publication:** John Wiley & Sons, 1959; second printing, 1967
- **File:** [`elementary_decision_theory.pdf`](elementary_decision_theory.pdf)
- **Type:** Introductory decision-theory and statistics textbook
- **Searchability:** Image-only encrypted scan; visual inspection is required
- **Difficulty:** Introductory to intermediate undergraduate
- **Primary roles:** Principal decision-theory curriculum source, problem
  source, reference source
- **Solution warning:** Contains a partial list of exercise answers and an
  appendix of derivations

**Major sequence.** Data processing and descriptive measures; probability and
random variables; utility and expectation; uncertainty about the state of
nature; Bayes strategies; classical statistics; statistical models; hypothesis
testing; estimation and confidence intervals; sequential analysis; appendices
on utility and game theory.

**Best Mathforge uses.** Modules 05, 08, 36–39, and 58; utility elicitation;
Bayes risk; decisions under uncertainty; comparison of Bayesian and classical
procedures; sequential decision problems.

### Optimization Techniques in Operations Research

- **Author:** C. B. Gupta
- **Edition:** Second edition, 2021
- **File:** [`optimization_techniques_in_operations_research.pdf`](optimization_techniques_in_operations_research.pdf)
- **Type:** Applied optimization and operations-research textbook
- **Searchability:** Good text layer
- **Difficulty:** Intermediate undergraduate
- **Primary roles:** Principal operations-research source, optimization source,
  problem source, reference source
- **Solution warning:** Contains many solved examples and answer-bearing
  exercises

**Major sequence.** Optimization modeling; linear and integer programming;
simplex methods; duality; sensitivity; transportation and assignment; travelling
salesman problems; dynamic programming; zero-sum games; unconstrained and
constrained optimization; convex and nonlinear programming; network scheduling;
goal programming; job sequencing.

**Best Mathforge uses.** Modules 20, 45, and 55–59; formulation of objectives
and constraints; LP and ILP engines; sensitivity; assignment and routing;
scheduling; dynamic programming; introductory strategic optimization.

### Advanced Bayesian Monte Carlo Methods for Inference and Control

- **Author:** Torben Sell
- **Publication:** University of Cambridge PhD thesis, February 2021
- **File:** [`advanced_bayesian_monte_carlo_methods.pdf`](advanced_bayesian_monte_carlo_methods.pdf)
- **Type:** Research thesis in Bayesian computational statistics
- **Searchability:** Good text layer
- **Difficulty:** Research-level
- **Primary roles:** Advanced reference source, algorithm source, integrated
  project source
- **Solution warning:** Not an exercise textbook; it contains original proofs,
  algorithms, and numerical experiments

**Major sequence.** Markov chain Monte Carlo; Langevin and Hamiltonian dynamics;
Gibbs and Metropolis–Hastings sampling; piecewise-deterministic Markov processes;
nondifferentiable posteriors; parallel localized inference; function-space and
neural-network priors; Bayesian inverse reinforcement learning and control.

**Best Mathforge uses.** Modules 41, 60, and 67; advanced MCMC variants;
sampling diagnostics and computational comparisons; Bayesian inverse problems;
parallel sampling; bridges among inference, control, MDPs, and reinforcement
learning. It supplements but does not replace an introductory Bayesian textbook.

### Distributed Systems: Theory and Applications

- **Authors:** Ratan K. Ghosh and Hiranmay Ghosh
- **Publication:** Wiley-IEEE Press, 2023
- **File:** [`distributed_systems_theory_and_applications.pdf`](distributed_systems_theory_and_applications.pdf)
- **Type:** Distributed-systems and distributed-algorithms textbook
- **Searchability:** Good text layer
- **Difficulty:** Intermediate to advanced computer science
- **Primary roles:** Principal distributed-systems source, algorithm source,
  problem source, reference source
- **Solution warning:** Contains exercises; no answer source was identified in
  the repository

**Major sequence.** Distributed architecture and communication; event ordering
and logical clocks; global states and termination; leader election; mutual
exclusion; Byzantine agreement and consensus; commit protocols; gossip and
publish-subscribe systems; peer-to-peer overlays; shared memory and consistency;
distributed data and knowledge; multi-agent systems.

**Best Mathforge uses.** Modules 43–47 and 66; partial orders over events;
distributed graph algorithms; safety and liveness; consensus; gossip diffusion;
consistency models; deterministic schedule simulations; concurrent Boss
Challenges.

### Bandit Algorithms for Website Optimization

- **Author:** John Myles White
- **Publication:** O'Reilly Media, first edition, December 2012; copyright 2013
- **File:** [`bandit_algorithms_for_website_optimization.pdf`](bandit_algorithms_for_website_optimization.pdf)
- **Type:** Short practical tutorial on multi-armed bandit algorithms
- **Searchability:** Good text layer
- **Difficulty:** Introductory to intermediate, programming-oriented
- **Primary roles:** Introductory curriculum source, applied problem source,
  simulation source
- **Solution warning:** Includes Python implementations and chapter exercises;
  no separate answer section was identified. Challenges must be independently
  adapted rather than copied from the book's code.

**Major sequence.** Exploration and exploitation; bandits as adaptive A/B
testing; epsilon-greedy policies; Monte Carlo evaluation; softmax and annealing;
UCB; practical complications including metrics, initialization, concurrent
experiments, nonstationarity, correlated arms, contextual bandits, and scale.

**Best Mathforge uses.** Module 61 as the applied entry point; Modules 03, 08,
09, 37, and 42 for streaming updates, experiment design, reproducible
simulation, metrics, and empirical algorithm comparison; Module 67 for adaptive
systems projects.

### Bandit Algorithms

- **Authors:** Tor Lattimore and Csaba Szepesvári
- **Publication:** Cambridge University Press, first published 2020
- **File:** [`bandit_algorithms.pdf`](bandit_algorithms.pdf)
- **Type:** Comprehensive graduate textbook on multi-armed bandit theory
- **Searchability:** Good text layer
- **Difficulty:** Advanced undergraduate to graduate; later parts are
  research-level
- **Primary roles:** Principal bandit curriculum source, proof source, problem
  source, advanced reference source
- **Solution warning:** Contains exercises, carefully worked proofs, and
  explicit algorithms; no answer manual was identified in the repository.

**Major sequence.** Probability, stochastic processes, Markov chains,
martingales, and concentration; stochastic finite-armed bandits and UCB;
adversarial bandits; information-theoretic lower bounds; contextual and linear
bandits; convex analysis and online optimization; combinatorial,
nonstationary, ranking, and pure-exploration problems; Bayesian bandits,
Gittins indices, and Thompson sampling; partial monitoring and learning in
Markov decision processes.

**Best Mathforge uses.** Module 61 as the principal rigorous source; Modules
21, 35, 37, 39, 55, 56, 58, and 60 for lower bounds, concentration, optimal
experimental design, Bayesian learning, convex and combinatorial optimization,
decision-making, and MDPs; Module 64 for a partial foundation in entropy,
optimal coding, and relative entropy; Module 67 for advanced integration.

### Information Theory: A Tutorial Introduction

- **Author:** James V. Stone
- **Publication:** arXiv:1802.05968v2, February 20, 2018
- **File:** [`information_theory_a_tutorial_introduction.pdf`](information_theory_a_tutorial_introduction.pdf)
- **Type:** Short tutorial paper
- **Searchability:** Good text layer
- **Difficulty:** Introductory and conceptual
- **Primary roles:** Orientation source, intuition source, terminology reference
- **Solution warning:** Contains no exercise or solution section

**Major sequence.** Bits and choices; surprisal; entropy; redundancy;
efficient coding; mutual information; noisy communication; channel capacity;
source and channel coding limits; annotated further reading.

**Best Mathforge uses.** Module 64 as a conceptual Level 0 entry before formal
derivations; Modules 04–06 for brief connections between probability,
expectation, and uncertainty. It is too short to anchor the module or serve as a
substantial challenge repository by itself.

### Introduction to Information Theory

- **Author:** Masud Mansuripur
- **Publication:** Prentice-Hall, 1987
- **File:** [`introduction_to_information_theory.pdf`](introduction_to_information_theory.pdf)
- **Type:** Introductory information-theory textbook
- **Searchability:** Searchable OCR with spacing and character imperfections
- **Difficulty:** Advanced undergraduate to beginning graduate
- **Primary roles:** Introductory curriculum source, problem source, reference
  source
- **Solution warning:** Contains problems after every chapter; no answer
  section was identified

**Major sequence.** Probability preliminaries; entropy and typical sequences;
fixed- and variable-length source coding; Huffman coding; universal source
coding; mutual information; discrete memoryless channels; channel capacity and
coding theorems; rate distortion; error-correcting and convolutional codes;
stationary sources, differential entropy, and the Arimoto–Blahut algorithm.

**Best Mathforge uses.** Module 64 as the main introductory textbook; Modules
02, 03, 05, 14, 35, and 53 for coding algorithms, probabilistic inequalities,
typical sequences, finite-field-flavored coding examples, convergence, and
stationary-source bridges; Module 67 for compression and communication systems.

### Elements of Information Theory

- **Authors:** Thomas M. Cover and Joy A. Thomas
- **Edition:** Second edition, John Wiley & Sons, 2006
- **File:** [`elements_of_information_theory.pdf`](elements_of_information_theory.pdf)
- **Type:** Comprehensive information-theory textbook
- **Searchability:** Good text layer
- **Difficulty:** Advanced undergraduate to graduate
- **Primary roles:** Principal information-theory curriculum source, proof
  source, advanced problem source, reference source
- **Solution warning:** Contains extensive chapter problems and worked proofs;
  no answer section was identified in the repository

**Major sequence.** Entropy, relative entropy, and mutual information;
asymptotic equipartition; entropy rates; compression and coding; channel
capacity and noisy-channel theorems; differential entropy and Gaussian
channels; rate distortion; information theory in statistics; maximum entropy;
universal coding; Kolmogorov complexity; network information theory; portfolio
theory; information inequalities.

**Best Mathforge uses.** Module 64 as the principal rigorous source; Modules
05, 33–37, 48, and 53 for divergence, continuous information measures,
concentration and asymptotics, statistical testing, Markov entropy rates, and
stationary processes; Module 67 for compression, communication, inference, and
networked-system projects.

### A Mathematical Introduction to Control Theory

- **Author:** Shlomo Engelberg
- **Edition:** Third edition, World Scientific, 2024
- **File:** [`a_mathematical_introduction_to_control_theory.pdf`](a_mathematical_introduction_to_control_theory.pdf)
- **Type:** Classical and modern control-theory textbook
- **Searchability:** Good text layer
- **Difficulty:** Intermediate to advanced undergraduate
- **Primary roles:** Principal introductory control curriculum source, applied
  problem source, implementation source, reference source
- **Solution warning:** The final chapter gives complete solutions to almost
  every odd-numbered exercise and several even-numbered exercises. The text
  also includes MATLAB and Python examples.

**Major sequence.** Laplace transforms and stability; transfer functions;
feedback and sensitivity; Routh–Hurwitz, Nyquist, Bode, and root-locus methods;
compensation and PID controllers; nonlinear-control examples; state-space
models; controllability, observability, observers, and pole placement;
discrete-time systems and the Kalman filter.

**Best Mathforge uses.** Module 63 as the principal applied sequence; Modules
27, 31, 49, and 62 for matrix dynamics, differential-equation models,
filtering, and nonlinear behavior; Module 67 for feedback-controlled
simulations. Solution-bearing exercises require special care when adapting
challenges.

### Mathematical Control Theory: An Introduction

- **Author:** Jerzy Zabczyk
- **Publication:** Birkhäuser, 1992; second printing with corrections, 1995;
  later Modern Birkhäuser Classics reprint
- **File:** [`mathematical_control_theory.pdf`](mathematical_control_theory.pdf)
- **Type:** Rigorous mathematical-control textbook
- **Searchability:** Searchable OCR with spacing and character imperfections
- **Difficulty:** Advanced undergraduate to graduate
- **Primary roles:** Advanced control curriculum source, proof source, problem
  source, reference source
- **Solution warning:** Contains exercises; no solution section was identified

**Major sequence.** Linear controllability, observability, stability,
stabilizability, realization, and constrained systems; nonlinear
controllability, observability, and Lyapunov stability; optimal control through
dynamic programming, Bellman equations, Riccati equations, impulse control,
and the maximum principle; infinite-dimensional linear systems and semigroup
methods.

**Best Mathforge uses.** Modules 31, 55, 58, 60, 62, and 63 for controlled
differential equations, optimization, Bellman reasoning, nonlinear stability,
controllability, and observability; Modules 25 and 67 for advanced
linear-operator and integrated-system work. It complements rather than
replaces Engelberg's more concrete opening sequence.

### A First Course in Causal Inference

- **Author:** Peng Ding
- **Publication:** arXiv:2305.18793v2, October 3, 2023
- **File:** [`a_first_course_in_causal_inference.pdf`](a_first_course_in_causal_inference.pdf)
- **Type:** Comprehensive causal-inference textbook manuscript
- **Searchability:** Good text layer
- **Difficulty:** Intermediate to advanced undergraduate and graduate
- **Primary roles:** Principal causal-inference curriculum source, problem
  source, statistical reference, applied-data source
- **Solution warning:** Contains homework in every chapter and R code and
  datasets. Solutions to most theory problems are available from the author to
  instructors but are not stored in the repository.

**Major sequence.** Association and the Yule–Simpson paradox; potential
outcomes; Fisherian and Neymanian analysis of randomized experiments;
stratification, rerandomization, regression adjustment, and matched designs;
observational identification; propensity scores, weighting, doubly robust
estimation, and matching; overlap and sensitivity analysis; regression
discontinuity; instrumental variables; principal stratification; mediation;
time-varying treatments and confounding.

**Best Mathforge uses.** Module 65 as the principal textbook; Module 37 for
randomization-based experimental design and analysis; Modules 35, 36, and 38
for asymptotics, estimation, regression, and diagnostics; Module 42 for
simulation-backed evaluation; Module 67 for policy and intervention projects.
R implementations must be translated into independently designed,
standard-library Python challenges that expose the mathematics.

### The Mathematics of Causal Inference in Statistics

- **Author:** Judea Pearl
- **Publication:** Technical and conference overview, October 8, 2007
- **File:** [`the_mathematics_of_causal_inference_in_statistics.pdf`](the_mathematics_of_causal_inference_in_statistics.pdf)
- **Type:** Short causal-inference overview paper
- **Searchability:** Searchable text with imperfect extracted characters
- **Difficulty:** Introductory to intermediate conceptual overview
- **Primary roles:** Orientation source, conceptual reference, framework bridge
- **Solution warning:** Contains no exercise or solution section

**Major sequence.** Associational versus causal questions; the limits of
probability notation; structural equations and path diagrams; interventions
and counterfactuals; confounding and back-door adjustment; the potential-
outcome language and its connection to structural models.

**Best Mathforge uses.** Module 65 as the shortest conceptual entry, especially
for learning to recognize when a programming or data problem asks an
interventional rather than associational question. It is not a sufficient
challenge repository by itself.

### The Mathematics of Causal Inference

- **Author:** Judea Pearl
- **Publication:** IMS 2013 Medallion Lecture and Joint Statistical Meetings
  proceedings paper, 2013
- **File:** [`the_mathematics_of_causal_inference.pdf`](the_mathematics_of_causal_inference.pdf)
- **Type:** Structural causal-inference survey paper
- **License noted by the repository copy:** Creative Commons Attribution 4.0
- **Searchability:** Good text layer
- **Difficulty:** Intermediate to advanced
- **Primary roles:** Structural-causal curriculum source, graphical reference,
  advanced orientation source
- **Solution warning:** Contains no exercise or solution section

**Major sequence.** Structural causal models and counterfactual semantics;
causal graphs and d-separation; interventions and identification; do-calculus;
back-door adjustment; mediation and direct and indirect effects;
transportability and meta-analysis; causal treatment of missing data.

**Best Mathforge uses.** Module 65 as the principal structural and graphical
complement to Ding; Modules 43–44 for directed-graph reasoning; Modules 37–38
for distinguishing adjustment from ordinary statistical conditioning; Module
67 for systems that must answer observational, interventional, and
counterfactual queries.

### Automata Theory and Formal Languages

- **Author:** Alberto Pettorossi
- **Edition:** Third edition, Aracne, 2011; first edition prepared in 2008
- **File:** [`automata_theory_and_formal_languages.pdf`](automata_theory_and_formal_languages.pdf)
- **Type:** Course notes and textbook on formal-language theory
- **Searchability:** Good text layer
- **Difficulty:** Intermediate undergraduate computer science
- **Primary roles:** Principal automata curriculum source, algorithm source,
  problem source, parsing reference
- **Solution warning:** Contains exercises, and some exercises are immediately
  followed by worked solutions or demonstrations; no separate answer manual was
  identified

**Major sequence.** Formal grammars and the Chomsky hierarchy; deterministic
and nondeterministic finite automata; regular grammars and expressions;
minimization and pumping lemmas; Moore and Mealy machines; pushdown automata
and context-free grammars; grammar normalization; CYK and Earley parsing;
linear-bounded automata; Turing machines; decidability, undecidability, and
noncomputable functions.

**Best Mathforge uses.** Module 22 as the principal formal-machines and
languages source; Modules 03, 18, 19, and 21 for state-machine implementation,
parsing, transformations, reductions, and computational limits; Module 66 for
reactive-state-machine bridges; Module 67 for parser, protocol, or interpreter
projects.

### Bayesian Inference in Statistical Analysis

- **Authors:** George E. P. Box and George C. Tiao
- **Publication:** Addison-Wesley, 1973
- **File:** [`bayesian_inference_in_statistical_analysis.pdf`](bayesian_inference_in_statistical_analysis.pdf)
- **Type:** Classical Bayesian statistical-inference textbook and monograph
- **Searchability:** Searchable OCR with spacing and character imperfections
- **Difficulty:** Intermediate to advanced; assumes familiarity with classical
  statistical inference
- **Primary roles:** Bayesian curriculum source, hierarchical-model reference,
  applied derivation source, statistical reference
- **Solution warning:** Contains extensive worked derivations and applied
  examples; no end-of-chapter exercise or answer section was identified

**Major sequence.** The nature of Bayesian inference; sufficient statistics,
nuisance parameters, decisions, and noninformative priors; Normal location and
scale inference; robustness to distributional assumptions; comparison of
variances; hierarchical, random-effect, mixed, and cross-classified models;
block designs; multivariate models; common regression coefficients; data
transformations and model criticism.

**Best Mathforge uses.** Module 39 as the main classical bridge from elementary
Bayesian updating to hierarchical statistical models; Modules 36–38 for
estimation, regression, variance components, and experimental designs; Module
58 for the decision-theory bridge. Its dated notation and limited modern
computational workflow should be supplemented by Pestman, Lattimore and
Szepesvári, Sell, and targeted current references.

### Algebraic Structures of Symmetric Domains

- **Author:** Ichiro Satake
- **Publication:** Iwanami Shoten and Princeton University Press, 1980;
  Publications of the Mathematical Society of Japan, volume 14
- **File:** [`algebraic_structures_of_symmetric_domains.pdf`](algebraic_structures_of_symmetric_domains.pdf)
- **Type:** Advanced research monograph and graduate lecture text
- **Searchability:** Searchable OCR with font and character imperfections
- **Difficulty:** Graduate to research-level; assumes Lie-group theory
- **Primary roles:** Advanced reference source, proof source, optional extension
  source
- **Solution warning:** Contains exercises; no solution section was identified

**Major sequence.** Linear algebraic groups; tori, unipotent, semisimple, and
reductive groups; roots and parabolic subgroups; Jordan algebras and Jordan
triple systems; symmetric Lie algebras; Riemannian and Hermitian symmetric
spaces; symmetric and Siegel domains; symplectic representations; classical
groups, quaternion algebras, Clifford algebras, and spin representations.

**Best Mathforge uses.** Module 15 only as a far-later advanced symmetry
extension; Modules 25, 30, 55, and 62 for optional bridges involving linear
representations, geometry, homogeneous spaces, and dynamics. It cannot anchor
the introductory algebra staircase because it presupposes rather than teaches
the basic theory of groups, rings, fields, finite fields, and homomorphisms.

### Advanced Markov Chain Monte Carlo Methods: Learning from Past Samples

- **Authors:** Faming Liang, Chuanhai Liu, and Raymond J. Carroll
- **Publication:** John Wiley & Sons, 2010
- **File:** [`advanced_markov_chain_monte_carlo_methods.pdf`](advanced_markov_chain_monte_carlo_methods.pdf)
- **Type:** Graduate textbook on advanced MCMC and computational statistics
- **Searchability:** Good text layer
- **Difficulty:** Graduate to research-level; assumes probability and
  statistical-inference foundations
- **Primary roles:** Principal advanced-MCMC curriculum source, problem source,
  algorithm source, reference source
- **Solution warning:** Contains exercises after every chapter; no answer
  source was identified in the repository

**Major sequence.** Bayesian inference and Monte Carlo integration; importance
sampling and acceptance-rejection generation; Gibbs sampling and acceleration;
Metropolis-Hastings and reversible-jump methods; auxiliary-variable and
population-based MCMC; dynamically weighted importance sampling; stochastic-
approximation Monte Carlo; adaptive proposals; applications to optimization,
networks, model selection, and scientific inference.

**Best Mathforge uses.** Modules 39–41 as an advanced computational bridge;
Module 41 as the principal systematic MCMC text; Modules 49 and 54 for Markov,
ergodic, and stochastic-approximation prerequisites; Module 56 for simulated
annealing and global-optimization applications; Module 67 for integrated
sampling systems. Chapter 1 and Chapter 6 strengthen importance and rejection
sampling in Module 40, but the book explicitly does not fully treat importance
sampling and does not cover the module's control-variate, antithetic,
stratification, or systematic rare-event sequence. It also does not provide the
particle-filtering sequence required for standard Sequential Monte Carlo.

### A Course in Game Theory

- **Authors:** Martin J. Osborne and Ariel Rubinstein
- **Publication:** MIT Press, 1994; repository PDF version dated January 19,
  2011
- **File:** [`a_course_in_game_theory.pdf`](a_course_in_game_theory.pdf)
- **Type:** Graduate game-theory textbook
- **Searchability:** Good text layer
- **Difficulty:** Advanced undergraduate to graduate; proof-oriented
- **Primary roles:** Principal game-theory curriculum source, proof source,
  problem source, reference source
- **Solution warning:** Contains many challenging exercises. Instructor
  solutions are referenced by the book but are not stored in the repository

**Major sequence.** Strategic games and Nash equilibrium; mixed, correlated,
and evolutionary equilibrium; rationalizability and dominated actions;
knowledge and common knowledge; extensive games with perfect information;
bargaining and repeated games; complexity and implementation; extensive games
with imperfect information; sequential and perfect Bayesian equilibrium;
coalitional games, the core, stable sets, the Shapley value, and the Nash
bargaining solution.

**Best Mathforge uses.** Module 59 as the principal complete source; Modules 05,
21, 58, and 60 for imperfect information, computational complexity, utility,
beliefs, sequential choice, and strategic planning; Module 67 for multi-agent,
negotiation, coalition, and mechanism-design projects. Its exercise staircase
begins above Mathforge's Level 0, so early challenges should isolate the models
and computations before adapting its harder proof problems.

### Symmetry Approach to Integrability and Non-Associative Algebraic Structures

- **Author:** Vladimir Sokolov
- **Publication:** Lecture-based monograph, arXiv:1711.10624v1, November 29,
  2017
- **File:** [`symmetry_approach_to_integrability_and_non_associative_algebraic_structures.pdf`](symmetry_approach_to_integrability_and_non_associative_algebraic_structures.pdf)
- **Type:** Research monograph on classical integrability and algebraic
  structures
- **Searchability:** Good text layer
- **Difficulty:** Graduate to research-level; intended for PhD students and
  specialists
- **Primary roles:** Advanced reference source, optional extension source,
  research-problem source
- **Solution warning:** Contains selected exercises, proofs, worked examples,
  and numerous open problems; it is not a gradual exercise textbook

**Major sequence.** Infinitesimal symmetries and conservation laws; symmetry-
based classification of integrable ODEs and PDEs; recursion, symplectic, and
Hamiltonian operators; Liouville-type hyperbolic equations; non-Abelian
equations; left-symmetric, Jordan, and triple Jordan structures; integrable
vector evolution equations.

**Best Mathforge uses.** Module 15 as a far-later bridge between algebraic laws
and symmetry; Modules 31 and 62 for optional studies of integrable evolution,
conservation, and transformations; Modules 25 and 30 for advanced operator and
geometric prerequisites; Module 67 for research-level symbolic or numerical
experiments. It does not close the introductory abstract-algebra gap and should
not determine the early module sequence.

## Catalog maintenance

New PDF filenames must use lowercase `snake_case`, derive from the official
English title, omit download-site labels, ISBNs, edition markers, and archive
identifiers, and include an author name only when needed to avoid ambiguity.
Bibliographic title, authorship, edition, and publication details belong in this
catalog rather than in the filename.

Tracked PDF renames must include explicit `.gitignore` exceptions or another
Git-aware migration step. Do not silently turn a rename into deletion of a
tracked book when `books/` is otherwise ignored.

When a book is added, removed, or replaced:

1. verify its title, author, edition, and file format;
2. inspect its table of contents rather than inferring scope from the filename;
3. identify whether it contains hints or solutions;
4. record its searchability and any special access limitation;
5. map it to curriculum areas and source roles;
6. update affected module source maps;
7. recalculate the affected statuses in
   [`MODULE_COVERAGE.md`](MODULE_COVERAGE.md).

Do not rename externally titled works merely to normalize their language. File
renaming may be considered separately when it improves maintainability and does
not break references.

## Current curriculum coverage

The complete module-by-module audit is maintained in
[`MODULE_COVERAGE.md`](MODULE_COVERAGE.md). At the time of this catalog update,
60 of 67 modules have adequate local coverage, 7 have partial coverage, and
none remain complete source gaps.

Important partial gaps remain in introductory abstract algebra; advanced Monte
Carlo and sequential Monte Carlo; network science; Hidden Markov Models; time
series; and MDPs and POMDPs.

Adequate coverage does not eliminate targeted research. Before planning any
module, recheck the catalog and coverage audit, then use current authoritative
external sources when local books leave a specialized question unresolved.
