# Complete Mathforge Module Roadmap

## Purpose

This document translates the Mathforge body of knowledge into a complete
module sequence, from foundational reasoning to integrated mathematical and
algorithmic systems.

The current roadmap contains **67 modules**. That number is an initial planning
decision, not a graduation requirement carved in stone. A module may be split,
merged, reordered, or revisited when student evidence or a newly cataloged book
shows that the dependency structure should change.

This roadmap does not authorize creating challenge folders in advance. When a
module begins, the Agent must consult the books, create that module's
`PROBLEMS.md`, and materialize only one challenge at a time.

## Design principles

- The first nine modules preserve the opening sequence already described in
  [`initial-modules.md`](initial-modules.md).
- Mathematics and algorithms develop together.
- Exact finite models precede approximation whenever practical.
- Proof, correctness, numerical error, and complexity recur throughout the
  curriculum.
- Local books guide prerequisites and problem families; student evidence
  determines the actual pace.
- A field reappears at increasing depth instead of being “finished” in one pass.
- Each phase ends with an integration gate or Boss Challenge using only material
  already introduced.
- Source gaps are explicit. A future module without a dedicated local book must
  begin with book-first review followed by careful external source selection.

## Phase overview

| Phase | Modules | Main purpose |
| --- | --- | --- |
| I | 01–09 | Finite models, probability, simulation, and the first Monte Carlo pass |
| II | 10–22 | Proof, discrete techniques, algorithms, complexity, and computation models |
| III | 23–32 | Geometry, linear algebra, calculus, differential equations, and numerical methods |
| IV | 33–42 | Continuous probability, statistics, Bayesian computation, and scientific evaluation |
| V | 43–54 | Graphs, networks, Markov chains, and stochastic processes |
| VI | 55–61 | Optimization, operations research, decision, strategy, and learning by action |
| VII | 62–66 | Dynamics, control, information, causality, and concurrency |
| VIII | 67 | Final synthesis through integrated systems |

## Phase I — Finite models, uncertainty, and experimentation

### Module 01 — States, Rules, and Possible Worlds

**Description.** Model finite states, Boolean rules, predicates, sets,
functions, relations, and invariants as executable Python structures.

**Why it matters for programming.** These structures underlie validation,
permissions, configuration, state machines, rule engines, and exhaustive tests.

**Main contents.** Logic; predicates and quantifiers; sets; Cartesian products;
functions; relations; finite cardinality; invariants; exhaustive enumeration.

**Primary local sources.** Levin Sections 0.2–0.4 and Chapter 3; Cummings
Chapters 3, 5, 8, and 9; Hehner Chapters 1–4.

### Module 02 — Counting Without Generating Everything

**Description.** Count finite configurations directly and under restrictions,
then compare counting with explicit generation.

**Why it matters for programming.** It exposes combinatorial explosion before a
program wastes time or memory materializing an impossible search space.

**Main contents.** Addition and multiplication principles; permutations;
combinations; inclusion-exclusion; pigeonhole principle; recurrence;
backtracking; output-sensitive complexity.

**Primary local sources.** Levin Chapters 1–2; *Concrete Mathematics* Chapters
1, 2, 5, and 7; Parberry and Gasarch Chapters 2, 4, and 10.

### Module 03 — Algorithmic Foundations: Representation, Search, and Cost

**Description.** Make the first explicit study of data representation,
correctness, search, sorting, and computational cost.

**Why it matters for programming.** It builds the vocabulary needed to compare
solutions in everyday work and technical interviews without memorizing tricks.

**Main contents.** Abstract data types; sequences; sets and maps; linear and
binary search; elementary sorting; invariants; termination; `O`, `Ω`, and `Θ`;
time-space trade-offs.

**Primary local sources.** Parberry and Gasarch Chapters 3, 5–7, and 13; Hehner
Chapters 4–5; *Concrete Mathematics* Chapter 9.

### Module 04 — Exact Probability in Finite Spaces

**Description.** Build discrete probability models whose results can be
calculated exactly through enumeration and counting.

**Why it matters for programming.** Random behavior needs an auditable model
before it becomes a simulation or randomized algorithm.

**Main contents.** Sample spaces; events; multiplicity; finite distributions;
indicator functions; rational arithmetic; exact probability solvers.

**Primary local sources.** Grimmett and Stirzaker Chapters 1–3; *Concrete
Mathematics* Chapter 8; Levin's introductory probability material.

### Module 05 — Evidence, Dependence, and Bayes

**Description.** Update finite probability models in response to evidence and
distinguish conditional probability from reversed reasoning.

**Why it matters for programming.** Diagnostics, filters, risk systems, and
recommendations depend on correct conditioning and base rates.

**Main contents.** Conditional probability; independence; total probability;
Bayes' theorem; partitions; probability trees; conditional counting.

**Primary local sources.** Grimmett and Stirzaker Chapters 1–3; Chernoff and
Moses Chapters 3 and 5–6 for Bayesian decision examples; Levin for the discrete
and combinatorial prerequisites.

### Module 06 — Random Variables: Measuring Uncertain Outcomes

**Description.** Map elementary outcomes to quantities and distributions that
measure cost, duration, reward, demand, and risk.

**Why it matters for programming.** Programs usually need summaries and trade-
offs, not merely a list of possible states.

**Main contents.** Discrete random variables; mass and cumulative functions;
expectation; moments; variance; covariance; joint and marginal distributions;
transformations.

**Primary local sources.** Grimmett and Stirzaker Chapters 2–3; *Concrete
Mathematics* Chapter 8.

### Module 07 — Sampling and Reproducible Simulation

**Description.** Transform uniform pseudorandom values into samples from
declared discrete distributions and validate the sampler against exact theory.

**Why it matters for programming.** Reproducibility and distributional
correctness are essential in simulations, randomized tests, and procedural
generation.

**Main contents.** Weighted sampling; cumulative distributions; inverse
transformation in finite cases; seeds; controlled random sources; empirical
frequency; search-preprocessing trade-offs.

**Primary local sources.** Grimmett and Stirzaker's simulation appendix;
Hehner Section 5.7; *Concrete Mathematics* Chapter 8.

### Module 08 — Statistics for Computational Experiments

**Description.** Describe repeated simulation results and quantify how sample
statistics vary.

**Why it matters for programming.** Benchmarks and simulations are misleading
when reported as isolated averages without uncertainty or experimental control.

**Main contents.** Samples and populations; descriptive statistics; estimators;
bias; standard error; sampling distributions; introductory confidence
intervals; streaming summaries; numerical stability.

**Primary local sources.** Pestman Chapters I–II; Chernoff and Moses Chapters
2–3 and 7; the scientific-discovery paper for evaluation motivation.

### Module 09 — Monte Carlo I: Computing Through Experimentation

**Description.** Estimate probabilities, expectations, sums, and geometric
quantities when exact enumeration becomes expensive.

**Why it matters for programming.** Monte Carlo turns a clear model into a
practical approximation while forcing explicit reasoning about error and cost.

**Main contents.** Monte Carlo estimators; standard error; convergence; law of
large numbers; introductory central limit theorem; confidence intervals;
exact-versus-approximate selection.

**Primary local sources.** Grimmett and Stirzaker's probability and simulation
material; *Concrete Mathematics* Chapter 8; White Chapter 4 for using
reproducible Monte Carlo studies to evaluate adaptive algorithms.

**Phase I integration gate.** Build a finite system that has an exact solver, a
reproducible sampler, a statistical report, and a measured Monte Carlo
approximation.

## Phase II — Proof, discrete methods, and algorithms

### Module 10 — Mathematical Proof and Counterexamples

**Description.** Turn definitions and observations into general arguments, and
learn to destroy false claims with minimal counterexamples.

**Why it matters for programming.** Proof habits improve specifications,
invariant design, code review, test selection, and correctness explanations.

**Main contents.** Direct proof; cases; contrapositive; contradiction;
constructive existence; uniqueness; counterexamples; necessary and sufficient
conditions; proof critique.

**Primary local sources.** Cummings Chapters 1–7; Levin Chapter 3.

### Module 11 — Specifications, Invariants, and Program Correctness

**Description.** State program behavior mathematically and connect
specifications to implementations through invariants and termination arguments.

**Why it matters for programming.** Tests sample executions; specifications and
proof reasoning clarify what all valid executions must guarantee.

**Main contents.** Preconditions; postconditions; assertions; refinement;
state relations; loop invariants; termination variants; soundness;
specification composition; proof versus testing.

**Primary local sources.** Hehner Chapters 4–5; Parberry and Gasarch Chapter 5.

### Module 12 — Induction, Recursion, and Recurrences

**Description.** Study the shared structure behind recursive definitions,
recursive programs, induction proofs, and recurrence equations.

**Why it matters for programming.** Recursive data and algorithms are easier to
design when construction, correctness, termination, and cost follow the same
decomposition.

**Main contents.** Induction; strong induction; structural induction; recursive
data; recursion trees; first- and higher-order recurrences; characteristic
roots; full-history recurrences.

**Primary local sources.** Levin Chapter 2; *Concrete Mathematics* Chapters 1
and 7; Parberry and Gasarch Chapters 2 and 4; Hehner Chapter 6.

### Module 13 — Discrete Sums, Floors, and Asymptotics

**Description.** Manipulate sums and integer-valued functions to analyze exact
and limiting behavior.

**Why it matters for programming.** Loop costs, batching, indexing, pagination,
and divide-and-conquer analyses often reduce to sums, floors, ceilings, and
growth rates.

**Main contents.** Sigma notation; arithmetic, geometric, harmonic, and
telescoping sums; multiple sums; floors and ceilings; finite differences;
asymptotic hierarchies; asymptotic manipulation.

**Primary local sources.** *Concrete Mathematics* Chapters 2, 3, and 9;
Parberry and Gasarch Chapter 3.

### Module 14 — Number Theory and Modular Algorithms

**Description.** Implement the arithmetic structure of integers and cycles.

**Why it matters for programming.** Modular arithmetic supports cryptography,
hashing, checksums, calendars, identifiers, pseudorandom mechanisms, and many
interview problems.

**Main contents.** Divisibility; Euclidean algorithm; primes; factorization;
congruences; modular exponentiation; Diophantine equations; elementary
cryptographic applications.

**Primary local sources.** *Concrete Mathematics* Chapters 3–4; Cummings
Chapter 2; Hehner Section 1.1.

### Module 15 — Algebraic Structures and Symmetry

**Description.** Recognize common laws behind operations, symmetries, modular
systems, and transformations.

**Why it matters for programming.** Algebraic structure supports reusable
abstractions, property-based tests, cryptography, coding, graphics, and safe
composition.

**Main contents.** Binary operations; semigroups and monoids conceptually;
groups; subgroups; symmetry; homomorphisms; rings; fields; finite fields at an
introductory level.

**Primary local sources.** Cummings' introduction to group theory; *Concrete
Mathematics* for modular examples; Satake for a far-later extension into
algebraic groups, Jordan structures, Lie algebras, and advanced symmetry;
Sokolov for a different advanced bridge through non-associative algebras,
symmetries, and integrable differential equations. Both advanced monographs
assume substantial prerequisites, so a dedicated introductory source for
groups, rings, fields, finite fields, and homomorphisms is still needed.

### Module 16 — Generating Functions and Advanced Counting

**Description.** Encode sequences and constrained counting problems as formal
power series that can be manipulated algebraically.

**Why it matters for programming.** Generating functions reveal recurrence,
convolution, distribution, and counting structure that direct enumeration
hides.

**Main contents.** Ordinary and exponential generating functions;
coefficients; convolution; solving recurrences; inclusion-exclusion at greater
depth; special combinatorial numbers; probability-generating functions.

**Primary local sources.** *Concrete Mathematics* Chapters 5–8; Levin's
advanced counting material.

### Module 17 — Data Structures

**Description.** Implement and compare representations that support different
operation and memory requirements.

**Why it matters for programming.** Data-structure choice often determines the
clarity and performance of the entire algorithm.

**Main contents.** Arrays; linked structures; stacks; queues; deques; hash
tables; heaps; search trees; balanced-tree concepts; tries; union-find;
dense-versus-sparse representations; invariants and amortized costs.

**Primary local sources.** Parberry and Gasarch Chapter 11; Hehner Chapters 2,
5, and 7.

### Module 18 — Divide and Conquer, Search, and Sorting

**Description.** Decompose problems into smaller instances and analyze how
combination work affects total cost.

**Why it matters for programming.** Search and sorting are foundational, while
divide and conquer teaches a transferable design method rather than one
algorithm.

**Main contents.** Linear and binary search; merge and partition ideas;
comparison sorting; selection; recurrence analysis; stability; lower bounds;
search and sort invariants.

**Primary local sources.** Parberry and Gasarch Chapters 6–7 and 13; Hehner
Sections 4.2 and 8.1; *Concrete Mathematics* for recurrences and asymptotics.

### Module 19 — Exhaustive Search, Backtracking, and Constraint Solving

**Description.** Explore finite decision spaces systematically and prune partial
states that cannot lead to valid solutions.

**Why it matters for programming.** Many scheduling, configuration, puzzle,
optimization, and world-generation problems begin as constraint search.

**Main contents.** State-space trees; exhaustive search; permutations and
combinations; backtracking; feasibility predicates; pruning; branch and bound;
constraint propagation conceptually; bitmask representations.

**Primary local sources.** Parberry and Gasarch Chapter 10; Hehner Section 5.4;
Levin's counting material.

### Module 20 — Greedy Algorithms and Dynamic Programming

**Description.** Contrast locally committed choices with cached optimization
over overlapping subproblems.

**Why it matters for programming.** These paradigms solve many interview and
production problems, but only when their structural assumptions are understood.

**Main contents.** Greedy-choice and exchange reasoning; optimal substructure;
overlapping subproblems; memoization; tabulation; state design; reconstruction;
knapsack; interval and sequence problems.

**Primary local sources.** Parberry and Gasarch Chapters 8–9; *Concrete
Mathematics* for recurrence tools.

### Module 21 — Complexity, Reductions, and Computational Limits

**Description.** Classify computational growth and relate problems by
transforming instances of one into another.

**Why it matters for programming.** It distinguishes problems needing better
code from problems needing approximation, restrictions, or a different goal.

**Main contents.** Time and space classes; polynomial versus exponential
growth; decision and optimization problems; reductions; P and NP;
NP-completeness; lower bounds; decidability and undecidability conceptually.

**Primary local sources.** Parberry and Gasarch Chapters 3, 12, and 13;
*Concrete Mathematics* Chapter 9; Pettorossi Chapters 5–6 for Turing machines,
decidability, and undecidability; Lattimore and Szepesvári Chapters 13–17 for
lower-bound reasoning in a specialized probabilistic setting.

### Module 22 — Automata, Formal Languages, and Program Semantics

**Description.** Give precise computational meaning to machines, languages,
parsers, expressions, scope, and recursive execution.

**Why it matters for programming.** The material supports parsers, protocol
validators, interpreters, regular expressions, compilers, state machines, and
clear reasoning about language behavior.

**Main contents.** Finite automata; regular languages and expressions;
grammars; pushdown machines; parsing; expressions and state; substitution;
scope; recursion; fixed-point ideas; Turing machines conceptually.

**Primary local sources.** Pettorossi Chapters 1–6 for grammars, finite and
pushdown automata, parsing, Turing machines, computability, and decidability;
Hehner Chapters 3 and 5–7 for expressions, substitution, scope, recursion,
fixed-point reasoning, and program semantics; Parberry and Gasarch for
complexity and algorithm-design bridges.

**Phase II integration gate.** Build a small language or constraint engine with
a formal specification, parser, data structures, correctness argument,
complexity analysis, and multiple solving strategies.

## Phase III — Geometry, linear algebra, calculus, and numerical methods

### Module 23 — Geometry, Trigonometry, and Vectors

**Description.** Represent position, orientation, distance, shape, rotation,
and periodic behavior computationally.

**Why it matters for programming.** Graphics, games, maps, simulations,
robotics, and visualization all depend on geometric models and coordinate
transformations.

**Main contents.** Euclidean and analytic geometry; coordinates; vectors;
distance; angles; sine and cosine; polar coordinates; dot products; projections;
2D transformations.

**Primary local sources.** Thomas and Finney's preliminaries and Chapters 9–11;
Hefferon Chapter 1's linear geometry.

### Module 24 — Linear Systems and Gaussian Elimination

**Description.** Model simultaneous linear constraints and implement elimination
without hiding the row operations behind a library.

**Why it matters for programming.** Linear systems appear in simulation,
graphics, fitting, networks, economics, and optimization.

**Main contents.** Linear equations; solution sets; Gaussian and Gauss-Jordan
elimination; echelon forms; homogeneous systems; rank intuition; operation
counts; exact and floating-point cases.

**Primary local sources.** Hefferon Chapter 1; the answer volume for validation
only.

### Module 25 — Vector Spaces and Linear Transformations

**Description.** Generalize vectors and matrices into spaces, bases, dimensions,
and structure-preserving maps.

**Why it matters for programming.** It clarifies representations, coordinate
changes, compression, transformations, and why the same matrix mechanism appears
across domains.

**Main contents.** Vector spaces; subspaces; span; independence; basis;
dimension; linear maps; range and null spaces; isomorphisms; matrix
representations; change of basis.

**Primary local sources.** Hefferon Chapters 2–3.

### Module 26 — Matrix Algorithms and Numerical Linear Algebra

**Description.** Turn linear-algebra definitions into stable and efficient
finite-precision algorithms.

**Why it matters for programming.** Direct formulas can magnify rounding error
or waste computation; representation and conditioning matter as much as
algebraic correctness.

**Main contents.** Floating-point matrices; pivoting; residuals; conditioning;
LU, QR, and Cholesky ideas; Gram-Schmidt; least squares; sparse matrices;
complexity and stability.

**Primary local sources.** Hefferon's accuracy, matrix-operation, projection,
and line-of-best-fit topics; van Kan, Segal, and Vermolen Chapter 9 for direct,
iterative, sparse, and preconditioned linear solvers.

### Module 27 — Eigenvalues, Spectral Methods, and Matrix Dynamics

**Description.** Study directions and modes preserved by linear
transformations, and use them to understand repeated matrix action.

**Why it matters for programming.** Eigenstructure supports Markov chains,
PageRank, stable populations, dimensionality reduction, oscillations, and
long-term system behavior.

**Main contents.** Determinants; similarity; eigenvalues and eigenvectors;
diagonalization; power iteration; spectral interpretation; repeated
transformation; stability.

**Primary local sources.** Hefferon Chapters 4–5 and the topics on Markov
chains, PageRank, stable populations, and coupled oscillators; Engelberg
Chapters 9–10 and Zabczyk Part I for state-space dynamics, stability,
controllability, and observability applications.

### Module 28 — Calculus I: Limits, Change, and Derivatives

**Description.** Model continuous change and local approximation through limits
and derivatives.

**Why it matters for programming.** Derivatives underlie optimization,
sensitivity, physical simulation, continuous probability, and learning
algorithms.

**Main contents.** Functions; limits; continuity; derivatives; derivative
rules; linear approximation; rates of change; numerical differentiation;
single-variable optimization.

**Primary local sources.** Thomas and Finney Chapters 1–3 and 6; Loomis and
Sternberg Chapter 3 as a later rigorous reference.

### Module 29 — Calculus II: Accumulation, Integration, and Series

**Description.** Model accumulation and approximation through integrals,
sequences, and infinite series.

**Why it matters for programming.** Integration supports probability densities,
physical totals, numerical quadrature, and error analysis; series support
approximation and computation.

**Main contents.** Definite and indefinite integrals; fundamental theorem;
substitution; improper integrals; numerical quadrature; Taylor series; power
series; convergence tests; approximation error.

**Primary local sources.** Thomas and Finney Chapters 4–8; *Concrete
Mathematics* for discrete analogies; Loomis and Sternberg Chapter 8 as a later
rigorous reference.

### Module 30 — Multivariable Calculus and Gradients

**Description.** Extend change and accumulation to functions with many inputs.

**Why it matters for programming.** Statistics, optimization, machine learning,
control, and physical simulation operate in multidimensional parameter spaces.

**Main contents.** Partial derivatives; gradients; directional derivatives;
Jacobians; Hessians; multiple integrals; constrained change; chain rule in many
variables; numerical gradient checks.

**Primary local sources.** Thomas and Finney Chapters 12–14; Loomis and
Sternberg Chapters 3 and 8; Hefferon for the linear-algebra prerequisites.

### Module 31 — Differential Equations and Numerical Evolution

**Description.** Model continuously evolving systems and approximate their
trajectories with discrete time steps.

**Why it matters for programming.** Population, epidemic, physical, economic,
and control simulations often begin as differential equations.

**Main contents.** Ordinary differential equations; initial-value problems;
systems; phase plots; Euler methods; Runge-Kutta ideas; step-size error;
stability; conservation checks.

**Primary local sources.** Thomas and Finney Section 6.11–6.12 for the entry;
Loomis and Sternberg Chapter 6; Perko for qualitative ODE theory; van Kan,
Segal, and Vermolen Chapters 10–12 for numerical evolution of PDE models;
Hefferon's coupled-oscillator application; Engelberg and Zabczyk for controlled
linear and nonlinear differential-equation systems; Sokolov only as a
far-later extension into integrable ODEs and PDEs, conservation laws, and
symmetry methods.

### Module 32 — Mathematical and Numerical Analysis

**Description.** Make convergence, approximation, conditioning, and stability
precise across numerical algorithms.

**Why it matters for programming.** A formula may be mathematically correct yet
produce an unreliable algorithm on finite-precision hardware.

**Main contents.** Real-number completeness conceptually; sequence and function
convergence; continuity; error bounds; root finding; interpolation;
conditioning; backward error; stable reformulation; convergence-rate
experiments.

**Primary local sources.** Loomis and Sternberg Chapters 3–4 and 8; van Kan,
Segal, and Vermolen Chapters 3–12; *Concrete Mathematics* Chapter 9 and
Hefferon's accuracy topics provide discrete and linear bridges.

**Phase III integration gate.** Build a geometric or physical simulator that
uses linear algebra, calculus, numerical evolution, convergence tests, and an
explicit error budget.

## Phase IV — Continuous probability, inference, and scientific evaluation

### Module 33 — Continuous Probability and Distribution Families

**Description.** Move from finite mass functions to densities, distribution
functions, and continuous waiting or measurement models.

**Why it matters for programming.** Continuous models appear in latency,
lifetimes, physical measurements, finance, queues, and simulation.

**Main contents.** Distribution and density functions; uniform, exponential,
normal, gamma, and related families; expectation and variance; numerical
integration; inverse transforms.

**Primary local sources.** Grimmett and Stirzaker Chapters 4–5; Pestman Chapter
I.

### Module 34 — Joint Probability and Transformations

**Description.** Model several dependent quantities together and determine how
their distributions change under transformation.

**Why it matters for programming.** Real systems expose correlated metrics and
derived quantities whose risks cannot be analyzed independently.

**Main contents.** Joint, marginal, and conditional distributions; covariance;
correlation; independence; transformations; Jacobian method; sums and ratios;
multivariate normal ideas.

**Primary local sources.** Grimmett and Stirzaker Chapters 2–5 and 7; Pestman
Chapters I and VIII.

### Module 35 — Convergence and Limit Theorems

**Description.** Study how random sequences stabilize in distribution,
probability, mean, or almost surely.

**Why it matters for programming.** Simulation error, statistical estimators,
and stochastic algorithms depend on precise forms of convergence.

**Main contents.** Modes of convergence; laws of large numbers; central limit
theorem; concentration intuition; Slutsky-style composition conceptually;
simulation diagnostics.

**Primary local sources.** Grimmett and Stirzaker Chapter 7; Pestman Chapter I;
*Concrete Mathematics* Chapter 8; Lattimore and Szepesvári Chapter 5 for
concentration of measure and later chapters for its repeated application;
Cover and Thomas Chapters 3 and 11 for asymptotic equipartition, large
deviations, and information-theoretic asymptotics.

### Module 36 — Statistical Estimation and Likelihood

**Description.** Infer unknown parameters from samples and compare estimators by
their repeated-sampling behavior.

**Why it matters for programming.** Metrics and simulations become decisions
only after uncertainty, bias, and model assumptions are quantified.

**Main contents.** Point estimation; bias; variance; consistency; efficiency;
method of moments; likelihood; maximum likelihood; Fisher-information intuition;
identifiability.

**Primary local sources.** Pestman Chapters I–II; Chernoff and Moses Chapters
7–10; Ding for randomization-based, propensity-weighted, matching, and doubly
robust estimators; Grimmett and Stirzaker for probability prerequisites.

### Module 37 — Confidence, Hypothesis Tests, and Experimental Design

**Description.** Quantify uncertainty in comparisons and design experiments
that can answer a stated question.

**Why it matters for programming.** A/B tests, performance investigations, and
simulation comparisons fail when sampling and stopping decisions are ignored.

**Main contents.** Confidence intervals; null and alternative hypotheses;
test statistics; p-values; power; Type I and II errors; multiple testing;
randomization; controls; sample-size planning; sequential caveats.

**Primary local sources.** Pestman Chapters III and V; Chernoff and Moses
Chapters 7, 9, and 10; Ding Parts II and III for Fisher randomization tests,
Neymanian repeated-sampling inference, stratification, rerandomization,
regression adjustment, matched designs, and observational comparisons; White
Chapters 2 and 7 for adaptive A/B testing and its operational hazards;
Lattimore and Szepesvári Chapter 21 for optimal design in least-squares
estimation; the scientific-discovery paper for evaluation structure. Targeted
external research remains useful for modern multiple-testing procedures and
prospective power calculations.

### Module 38 — Regression and Exploratory Data Analysis

**Description.** Describe relationships in data, diagnose models, and separate
prediction from causal interpretation.

**Why it matters for programming.** Simulations and production systems produce
multivariable data that require more than isolated averages.

**Main contents.** Visualization; correlation; simple and multiple linear
regression; residuals; least squares; transformations; regularization intuition;
logistic-regression concepts; prediction versus explanation.

**Primary local sources.** Pestman Chapters IV, VII, and VIII; Hefferon's
line-of-best-fit topic for linear foundations; Ding for regression adjustment,
propensity methods, balance diagnostics, and repeated warnings against reading
causal effects directly from associational regressions.

### Module 39 — Bayesian Inference

**Description.** Treat inference as probabilistic updating from prior beliefs to
posterior and predictive distributions.

**Why it matters for programming.** Bayesian models support diagnosis,
forecasting, personalization, belief-bearing agents, and sequential evidence.

**Main contents.** Prior; likelihood; posterior; evidence; conjugate models;
posterior predictive; sequential updating; hierarchical models; model
comparison; calibration.

**Primary local sources.** Pestman's Bayesian-estimation section; Chernoff and
Moses Chapters 5–6; Box and Tiao for prior construction, nuisance parameters,
Normal-theory inference, robustness, hierarchical designs, multivariate
models, transformations, and model criticism; Grimmett and Stirzaker for
probability foundations; Lattimore and Szepesvári Chapters 34–36 for sequential
Bayesian learning, Bayesian bandits, and Thompson sampling; Sell for advanced
computation and posterior-predictive applications. Targeted current references
remain useful for modern model-comparison and calibration workflows.

### Module 40 — Monte Carlo II: Variance Reduction and Rare Events

**Description.** Improve simulation estimators and sample efficiently when
ordinary random sampling wastes most computation.

**Why it matters for programming.** High-dimensional, rare-event, and expensive
simulations require better estimators rather than merely larger loops.

**Main contents.** Control variates; antithetic variables; stratification;
importance sampling; rejection sampling; rare-event estimation; bootstrap;
effective sample cost.

**Primary local sources.** Grimmett and Stirzaker's simulation material;
Liang, Liu, and Carroll Chapter 1 for Monte Carlo integration, importance
sampling, and acceptance-rejection generation and Chapter 6 for advanced
importance weighting; Pestman Chapter VII for bootstrap; Sell for advanced
sampling context. Control variates, antithetic variables, stratified sampling,
and systematic rare-event methods still lack a dedicated local source.

### Module 41 — MCMC and Sequential Monte Carlo

**Description.** Construct dependent samples from difficult target
distributions and track distributions that evolve with incoming evidence.

**Why it matters for programming.** Complex Bayesian and stochastic models often
cannot be normalized or sampled directly.

**Main contents.** Markov-chain sampling; Metropolis-Hastings; Gibbs sampling;
burn-in and mixing; autocorrelation; diagnostics; particle filtering;
resampling; degeneracy.

**Primary local sources.** Liang, Liu, and Carroll Chapters 2–8 as the principal
systematic source for Gibbs, Metropolis-Hastings, auxiliary-variable,
population-based, stochastic-approximation, and adaptive MCMC; Sell Chapters
2–4 for research-level MCMC and parallel sampling; Grimmett and Stirzaker for
probability and Markov prerequisites. Standard Sequential Monte Carlo and
particle filtering still lack a dedicated local source.

### Module 42 — Scientific Computing, Benchmarks, and Discovery Evaluation

**Description.** Design reproducible computational experiments and evaluate
algorithms or intelligent systems at both component and project levels.

**Why it matters for programming.** A system can optimize a benchmark while
failing the real task unless scenarios, metrics, controls, and validity are
designed carefully.

**Main contents.** Verification and validation; baselines; controls; ablations;
scenario-grounded evaluation; benchmark validity; leakage; calibration;
reproducibility; error analysis; human-in-the-loop experiments.

**Primary local sources.** *Evaluating Large Language Models in Scientific
Discovery*; van Kan, Segal, and Vermolen for modeling, numerical validation, and
error analysis; Hefferon's application and accuracy topics; White Chapter 4 for
Monte Carlo comparison of adaptive algorithms.

**Phase IV integration gate.** Design, implement, and evaluate a simulation
study with an explicit hypothesis, analytical baseline, uncertainty analysis,
reproducible protocol, and failure analysis.

## Phase V — Graphs, networks, and stochastic processes

### Module 43 — Graphs I: Representation, Traversal, and Connectivity

**Description.** Model relationships as graphs and implement the fundamental
operations for exploring them.

**Why it matters for programming.** Dependencies, maps, social links, syntax,
workflows, and state transitions are graph-shaped.

**Main contents.** Directed and undirected graphs; adjacency representations;
degrees; walks and paths; BFS; DFS; components; connectivity; traversal
invariants; dense-versus-sparse costs.

**Primary local sources.** Bondy and Murty Chapters 1 and 3; Levin Chapter 4;
Parberry and Gasarch's graph problems.

### Module 44 — Graphs II: Trees, DAGs, Paths, and Spanning Structure

**Description.** Exploit graph structure to order dependencies, find efficient
routes, and connect vertices without cycles.

**Why it matters for programming.** Build systems, routing, scheduling, file
trees, indexes, and network design depend on these structures.

**Main contents.** Trees; rooted trees; directed acyclic graphs; topological
ordering; shortest paths; spanning trees; minimum spanning trees; correctness of
greedy graph algorithms.

**Primary local sources.** Bondy and Murty Chapters 2, 3, 9, and 10; Parberry
and Gasarch Chapters 7, 9, and 13.

### Module 45 — Graphs III: Flow, Cuts, and Matching

**Description.** Model capacity, assignment, and pairing problems as network
optimization.

**Why it matters for programming.** Logistics, scheduling, resource allocation,
matching markets, and communication networks reduce to flow or matching.

**Main contents.** Networks; residual capacity; augmenting paths; maximum flow;
minimum cuts; bipartite matching; Hall-style conditions; assignment problems;
integrality.

**Primary local sources.** Bondy and Murty Chapters 5 and 11; Parberry and
Gasarch Chapters 9 and 13; Gupta Chapter 5 for transportation and assignment.

### Module 46 — Graphs IV: Coloring, Planarity, and Hard Structure

**Description.** Study global graph constraints that model conflicts,
geographic layout, and combinatorially difficult choices.

**Why it matters for programming.** Coloring supports scheduling and resource
conflict; planarity supports layout and networks; cliques and independent sets
expose hard optimization boundaries.

**Main contents.** Euler and Hamilton structure; edge and vertex coloring;
independent sets; cliques; planar graphs; duality; cycle and cut spaces;
NP-hard graph problems; exact and heuristic solvers.

**Primary local sources.** Bondy and Murty Chapters 4–9 and 12; Parberry and
Gasarch Chapters 10 and 12.

### Module 47 — Network Science and Diffusion

**Description.** Study large-network structure and processes that propagate
through it.

**Why it matters for programming.** Rumors, epidemics, failures, influence,
recommendations, and infrastructure cascades emerge from both topology and
dynamics.

**Main contents.** Random graphs; degree distributions; small-world structure;
hubs; communities; centrality; diffusion; contagion; cascades; robustness;
network experiments.

**Primary local sources.** Bondy and Murty for graph foundations; Ghosh and
Ghosh Chapters 10–12 for gossip, diffusion, and overlay networks. Random-graph,
centrality, community, and robustness theory still lack a dedicated local
network-science source.

### Module 48 — Markov Chains I: Finite-State Dynamics

**Description.** Model memoryless evolution over finite states and compute
multi-step distributions.

**Why it matters for programming.** State behavior, reliability, ranking,
queues, and simulations often admit compact transition models.

**Main contents.** States; transition probabilities; matrices; paths;
multi-step evolution; communicating classes; recurrence and transience;
simulation versus matrix calculation.

**Primary local sources.** Grimmett and Stirzaker Chapter 6; Hefferon's Markov
chain topic; Cover and Thomas Chapter 4 for entropy rates of Markov chains.

### Module 49 — Markov Chains II: Long-Term Behavior and Hidden State

**Description.** Analyze stationary behavior, absorption, hitting events, and
models whose states are only indirectly observed.

**Why it matters for programming.** Long-term behavior and partial observation
matter in prediction, ranking, reliability, agent belief, and sequence models.

**Main contents.** Stationary distributions; convergence; detailed balance;
absorbing chains; hitting probabilities and times; higher-order chains; Hidden
Markov Models; forward and filtering ideas.

**Primary local sources.** Grimmett and Stirzaker Chapter 6; Hefferon's spectral
and Markov topics; Engelberg Chapter 10 for a discrete-time Kalman-filter
bridge. Hidden Markov Models and systematic discrete-state filtering still
lack a dedicated local source.

### Module 50 — Discrete Stochastic Processes and Random Walks

**Description.** Model uncertainty unfolding through discrete time rather than
as a single random outcome.

**Why it matters for programming.** Repeated trials, cumulative fortunes,
search, population changes, and randomized algorithms depend on trajectories.

**Main contents.** Bernoulli processes; random walks; stopping times;
first-passage events; branching processes; gambler's ruin; path simulation;
trajectory statistics.

**Primary local sources.** Grimmett and Stirzaker Chapters 8–9; *Concrete
Mathematics* Chapter 8.

### Module 51 — Poisson, Continuous-Time, and Birth-Death Processes

**Description.** Model events that occur at random times and state systems that
change through arrivals and departures.

**Why it matters for programming.** Failures, traffic, requests, incidents,
population changes, and service systems are naturally continuous-time event
processes.

**Main contents.** Poisson process; exponential waiting; independent increments;
superposition and thinning; continuous-time Markov chains; birth-death models;
event-driven simulation.

**Primary local sources.** Grimmett and Stirzaker Chapters 8 and 13.

### Module 52 — Renewal, Queues, and Reliability

**Description.** Analyze repeated lifecycles, waiting systems, failures,
repairs, and capacity.

**Why it matters for programming.** Servers, workers, inventories, maintenance,
and customer systems need both stochastic models and operational decisions.

**Main contents.** Renewal processes; residual life; renewal reward; queue
notation; utilization; Little's law; priorities; queue networks; survival and
hazard; series and parallel reliability; availability.

**Primary local sources.** Grimmett and Stirzaker Chapters 10–11.

### Module 53 — Stationary Processes and Time Series

**Description.** Study random signals whose statistical behavior is stable over
time and analyze dependence across lags.

**Why it matters for programming.** Monitoring, forecasting, telemetry, audio,
economics, and system health produce ordered data rather than independent
samples.

**Main contents.** Stationarity; autocovariance; autocorrelation; moving-average
and autoregressive ideas; spectral intuition; estimation from finite series;
forecast validation.

**Primary local sources.** Grimmett and Stirzaker Chapter 9; Pestman's
stochastic-analysis material; Cover and Thomas Chapters 4 and 12 for entropy
rates and stationary Gaussian processes; Mansuripur Chapter 9 for stationary
sources. Autoregressive modeling, diagnostics, and forecast validation still
lack a dedicated local time-series source.

### Module 54 — Martingales, Brownian Motion, and Diffusion

**Description.** Study fair-game structure and continuous random trajectories.

**Why it matters for programming.** Martingales support stopping arguments;
diffusions model noisy physical, financial, and biological evolution.

**Main contents.** Conditional expectation as a process; martingales;
submartingales; optional-stopping intuition; Brownian motion; diffusion;
first-passage behavior; discretization and simulation error.

**Primary local sources.** Grimmett and Stirzaker Chapters 12–13; Sell Chapters
2–3 for diffusion-based MCMC applications.

**Phase V integration gate.** Simulate and analytically inspect a networked
stochastic system containing graph structure, state transitions, propagation,
waiting, and failure.

## Phase VI — Optimization, decisions, strategy, and learning by action

### Module 55 — Continuous and Convex Optimization

**Description.** Minimize or maximize continuous objectives under mathematical
constraints.

**Why it matters for programming.** Parameter fitting, control, allocation, and
machine learning depend on choosing good solutions in continuous spaces.

**Main contents.** Objectives and constraints; feasible regions; convex sets and
functions; gradients; optimality conditions; gradient descent; line search;
constrained optimization; duality intuition.

**Primary local sources.** Gupta Chapters 9–10; Thomas and Finney's derivative
and constrained-optimization sections; Loomis and Sternberg Chapter 3; Hefferon
for linear-algebra prerequisites; Lattimore and Szepesvári Chapters 26 and 28
for convex analysis, regularization, and online optimization; Zabczyk Part III
for value functions, linear regulators, Riccati equations, and maximum-principle
bridges to optimal control.

### Module 56 — Discrete and Combinatorial Optimization

**Description.** Optimize over finite configurations where exhaustive search is
too expensive.

**Why it matters for programming.** Scheduling, routing, selection, layout, and
world generation are usually constrained discrete searches.

**Main contents.** Exact search; branch and bound; dynamic programming; greedy
approximations; local search; simulated annealing; tabu concepts; genetic
algorithms conceptually; approximation quality.

**Primary local sources.** Parberry and Gasarch Chapters 8–10 and 12–13; Gupta
Chapters 2, 6–7, and 10; Bondy and Murty for graph optimization examples;
Lattimore and Szepesvári Chapter 30 for combinatorial bandits; Liang, Liu, and
Carroll Chapters 4 and 7 for simulated-annealing and stochastic-approximation
applications to global optimization.

### Module 57 — Operations Research and Mathematical Programming

**Description.** Convert operational systems into variables, objectives, and
constraints that allocate scarce resources.

**Why it matters for programming.** Logistics, transport, scheduling, inventory,
staffing, and production systems require explicit trade-offs and feasibility.

**Main contents.** Linear programming; simplex concepts; duality; integer
programming; transportation and assignment; scheduling; routing; inventory;
queue-informed capacity; sensitivity analysis.

**Primary local sources.** Gupta Chapters 1–7 and 11–13; Bondy and Murty and
Parberry and Gasarch for flow, assignment, and algorithmic foundations.

### Module 58 — Decision Theory and Utility

**Description.** Choose actions by combining uncertain beliefs with values,
costs, and attitudes toward risk.

**Why it matters for programming.** Recommendation, diagnosis, planning, and
autonomous agents need a defensible rule for choosing among uncertain outcomes.

**Main contents.** Utility; expected utility; risk aversion; decision trees;
Bayesian decisions; value of information; multicriteria choices; sensitivity to
belief and preference assumptions.

**Primary local sources.** Chernoff and Moses Chapters 4–6 and Appendix F;
Pestman's Bayesian-estimation material; Lattimore and Szepesvári Chapters
34–36 for sequential Bayesian learning and action selection; the probability
and Bayesian modules.

### Module 59 — Game Theory and Strategic Interaction

**Description.** Analyze systems where each participant's result depends on the
choices of others.

**Why it matters for programming.** Markets, protocols, security, negotiations,
factions, and multi-agent systems require incentive-aware behavior.

**Main contents.** Normal and extensive forms; pure and mixed strategies;
dominance; minimax; Nash equilibrium; repeated games; imperfect information;
Bayesian games; cooperation; coalitions; mechanism-design intuition.

**Primary local sources.** Osborne and Rubinstein as the principal sequence for
strategic games, Nash and mixed equilibrium, extensive and repeated games,
imperfect information, Bayesian games, bargaining, implementation, and
coalitional games; Gupta Chapter 8 for a gentler computational entry through
two-person zero-sum games; Chernoff and Moses Appendix F and Cummings for
introductory bridges.

### Module 60 — Markov Decision Processes and Partial Observability

**Description.** Combine stochastic state transitions, actions, rewards, and
future planning, including belief over hidden state.

**Why it matters for programming.** Goal-directed agents must compare actions by
their future consequences rather than immediate reward alone.

**Main contents.** Policies; horizons; discounting; value functions; Bellman
equations; policy and value iteration; stochastic control; POMDP concepts;
belief states; planning under uncertainty.

**Primary local sources.** Lattimore and Szepesvári Chapter 38 for MDPs,
Bellman optimality, policy computation, and a reinforcement-learning bridge;
Zabczyk Part III for value functions, Bellman equations, and optimal control;
Sell Chapter 6 for Bayesian inverse reinforcement learning and control; Gupta
Chapter 7 for dynamic programming; Grimmett and Stirzaker and Hefferon for
Markov foundations. POMDPs and belief-state planning remain only partially
covered.

### Module 61 — Multi-Armed Bandits

**Description.** Learn while acting by balancing exploration of uncertain
options with exploitation of known good choices.

**Why it matters for programming.** Adaptive recommendations, experiments,
routing, and strategy selection must pay a real cost to acquire information.

**Main contents.** Regret; epsilon-greedy; confidence bounds; UCB; Thompson
sampling; Bayesian updating; nonstationarity; contextual-bandit intuition;
offline evaluation cautions.

**Primary local sources.** White Chapters 1–7 provide the practical entry
through epsilon-greedy, softmax, UCB, simulation, evaluation metrics,
nonstationarity, and contextual extensions. Lattimore and Szepesvári provide
the principal rigorous sequence: stochastic, adversarial, contextual, linear,
combinatorial, nonstationary, and Bayesian bandits; regret analysis; lower
bounds; pure exploration; and Thompson sampling. Probability, Bayesian,
decision, linear-algebra, and optimization modules provide prerequisites.

**Phase VI integration gate.** Build a multi-agent resource-allocation system
that plans under uncertainty, compares exact and heuristic optimization, and
reports strategic and statistical failure modes.

## Phase VII — Dynamics, control, information, causality, and interaction

### Module 62 — Dynamical Systems

**Description.** Analyze long-term behavior produced by iterated or continuous
state-update rules.

**Why it matters for programming.** Simulations often exhibit equilibrium,
cycles, instability, or chaos that cannot be understood from one update step.

**Main contents.** State evolution; fixed points; stability; phase space;
attractors; feedback; bifurcations; sensitivity to initial conditions; chaos;
numerical artifacts.

**Primary local sources.** Perko as the principal source; Zabczyk Part II for
nonlinear controllability, Lyapunov stability, and stabilizability; Engelberg
Chapter 8 for concrete nonlinear-control examples; Loomis and Sternberg and
Hefferon's stable-population and oscillator topics for analytical and linear
examples; Sokolov for far-later work on integrability, infinitesimal symmetries,
conservation laws, and Hamiltonian structure.

### Module 63 — Control Theory

**Description.** Choose feedback actions that keep a dynamic system near desired
behavior despite disturbances.

**Why it matters for programming.** Controllers regulate physical processes,
server load, queues, inventory, pacing, and adaptive simulations.

**Main contents.** Open and closed loops; transfer functions; setpoints and
tracking error; frequency and time response; proportional, integral, and
derivative control; stability and robustness; state-space models;
controllability; observability and observers; discrete-time control; optimal
and stochastic-control bridges.

**Primary local sources.** Engelberg as the principal concrete sequence through
classical feedback, stability, compensation, PID, state-space models,
observers, and discrete-time control; Zabczyk for rigorous linear, nonlinear,
and optimal control; Perko for dynamical systems and stability; Sell Chapter 6
for an advanced Bayesian-control application; Hehner's thermostat and
reaction-controller examples.

### Module 64 — Information Theory

**Description.** Quantify uncertainty, surprise, dependence, compression, and
communication limits.

**Why it matters for programming.** Information measures support compression,
feature selection, anomaly detection, model comparison, communication, and
novelty measurement.

**Main contents.** Surprisal; entropy; joint and conditional entropy; mutual
information; KL divergence; cross-entropy; data-processing inequality;
asymptotic equipartition; source coding and compression; noisy channels;
capacity and channel coding; rate distortion; connections to statistics,
Bayesian inference, and learning.

**Primary local sources.** Stone for conceptual orientation; Mansuripur for the
introductory progression through source coding, mutual information, channels,
capacity, coding theorems, error correction, and rate distortion; Cover and
Thomas as the principal rigorous and advanced source. Lattimore and Szepesvári
Chapters 14–17 provide information-theoretic lower-bound applications; Hehner
provides an introductory programming-oriented bridge.

### Module 65 — Causal Inference

**Description.** Distinguish observing a relationship from changing an outcome
through intervention.

**Why it matters for programming.** Systems trained on observational data can
recommend harmful actions when correlation is mistaken for causation.

**Main contents.** Association versus causation; potential outcomes;
structural causal models; causal DAGs and d-separation; confounding, mediators,
colliders, and selection; interventions and do-notation; identifiability and
back-door adjustment; randomized experiments; propensity scores, weighting,
matching, and doubly robust estimation; instrumental variables; mediation;
counterfactuals; sensitivity analysis; transportability.

**Primary local sources.** Pearl's 2007 paper for the conceptual entry from
association to causal language; Ding as the principal comprehensive sequence
through potential outcomes, experiments, observational identification and
estimation, sensitivity, instrumental variables, and mediation; Pearl's 2013
paper for structural causal models, causal graphs, d-separation, interventions,
do-calculus, graphical identification, mediation, transportability, and missing
data. Statistics, probability, graphs, and experimental-design modules provide
prerequisites.

### Module 66 — Concurrency, Communication, and Reactive Systems

**Description.** Model programs whose components interleave, communicate, wait,
and react to events.

**Why it matters for programming.** Servers, workers, simulations, interfaces,
and distributed systems fail through races and deadlocks invisible in a single
sequential execution.

**Main contents.** Interleavings; atomicity; safety and liveness; shared state;
message passing; buffers; producer-consumer systems; monitors; channels;
deadlock; broadcast; deterministic schedule simulation; concurrency invariants.

**Primary local sources.** Hehner Chapters 8–9; Ghosh and Ghosh Chapters 3–13
for communication, ordering, global state, safety, liveness, mutual exclusion,
consensus, gossip, and consistency; Pettorossi Chapter 2 for finite-state,
Moore-machine, Mealy-machine, and transducer foundations.

**Phase VII integration gate.** Build a controlled, concurrent, information-
aware simulation and use causal experiments to distinguish observed behavior
from intervention effects.

## Phase VIII — Final synthesis

### Module 67 — Integrated Mathematical Systems Laboratory

**Description.** Design a sequence of Mega Boss Challenges that combine entire
branches of the curriculum in realistic software systems.

**Why it matters for programming.** Mastery is demonstrated by recognizing
hidden mathematical structure, selecting algorithms, measuring uncertainty,
and defending design decisions without being told which field applies.

**Main contents.** Candidate systems include a stochastic world simulator; a
network epidemic and intervention lab; an uncertainty-aware logistics planner;
a belief-bearing multi-agent environment; a controlled dynamic economy; and a
scientific-discovery benchmark with reproducible evaluation.

**Primary local sources.** All cataloged books and completed Mathforge modules.
The scientific-discovery paper is a principal evaluation reference. External
primary sources will be selected separately for each real-world domain.

## Roadmap maintenance

When a module is about to begin:

1. check completed modules and demonstrated mastery;
2. confirm that its prerequisites still hold;
3. consult [`books/CATALOG.md`](../books/CATALOG.md),
   [`books/MODULE_COVERAGE.md`](../books/MODULE_COVERAGE.md), and relevant
   chapters;
4. confirm or revise the recorded source coverage;
5. research external primary sources only after the local review;
6. create the module README and adaptive `PROBLEMS.md`;
7. materialize exactly one challenge when requested.

The roadmap is complete as a map, but intentionally incomplete as a set of
assignments. Future challenge design remains evidence-driven.
