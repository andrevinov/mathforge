# Mathforge Mathematical Body of Knowledge

## Purpose of this document

This document is the reference map of the mathematical fields and closely
related algorithmic disciplines we intend to study in Mathforge. It describes
**what makes up the curriculum**, not the order in which the subjects will be
studied.

The fields below naturally overlap. Markov chains, for example, use probability
and linear algebra; optimization appears in operations research, control, and
reinforcement learning; algorithm design turns all of these structures into
effective programs. This overlap is desirable: mastery means recognizing the
same structure in different problems and knowing how to compute with it.

The inclusion criterion is not merely “this may be useful in one specific
project.” We want fields that improve the general ability to:

- represent problems precisely;
- recognize structures and invariants;
- design algorithms;
- choose representations and data structures deliberately;
- reason about correctness and termination;
- evaluate time and memory costs;
- reason about uncertainty;
- measure errors and interpret results;
- make decisions subject to objectives and constraints;
- build reliable simulations;
- explain why a program works.

The topic lists indicate the intended scope, but they are not commitments to
study everything at once or at the same depth.

## 1. Foundations, structures, and counting

### Mathematical logic

**Description.** The study of propositions, predicates, quantifiers,
connectives, implication, equivalence, validity, and proof methods. It is the
language used to turn informal statements into precise conditions.

**Why study it.** Programs are built from conditions, invariants,
preconditions, and consequences. Logic improves the writing of filters and
rules, helps identify missing cases, supports stronger tests, and makes it
possible to reason about correctness instead of relying only on examples.

**Planned topics.** Propositional logic; predicate logic; quantifiers; truth
tables; equivalences; implication; negation of propositions; direct proof,
proof by contraposition, and proof by contradiction; invariants.

### Mathematical proof and reasoning

**Description.** The study of how mathematical claims are formulated,
justified, refuted, and connected. Proof turns examples and intuition into a
general argument whose assumptions and conclusions can be inspected.

**Why study it.** Programming requires more than observing that code passes a
few examples. Proof habits support loop invariants, termination arguments,
correctness reviews, counterexample construction, test design, and the ability
to distinguish a specification from evidence about one execution.

**Planned topics.** Definitions and theorem statements; direct proof; proof by
cases; contrapositive; contradiction; induction and strong induction;
constructive existence; uniqueness; counterexamples; necessary and sufficient
conditions; invariants; proof critique; correspondence between proofs and
algorithms.

### Set theory and relations

**Description.** The study of collections of objects and the relationships
between them. It provides the formal language for domains, membership, subsets,
Cartesian products, partitions, equivalence, and order.

**Why study it.** Nearly every program manipulates sets of states, entities,
permissions, or possibilities. Set operations appear in queries, access
control, deduplication, databases, state analysis, and rule specification.
Relations model dependencies, precedence, compatibility, and association.

**Planned topics.** Membership and inclusion; union, intersection, difference,
and complement; power sets; Cartesian products; binary relations; equivalence
relations; partitions; partial orders; closures; cardinality.

### Theory of functions

**Description.** The study of functions as mappings between sets, including
composition, inversion, and structural properties.

**Why study it.** Mathematical functions are an essential model for data and
state transformations. Well-defined domains and codomains reduce ambiguity;
composition helps build complex systems from parts; injectivity and
invertibility clarify when a transformation loses information.

**Planned topics.** Domain, codomain, and image; composition; inverse functions;
injective, surjective, and bijective functions; restriction; indicator
functions; elementary asymptotic growth.

### Discrete mathematics

**Description.** The study of finite or countable structures. It brings
together and connects logic, sets, relations, functions, proofs, recurrences,
counting, and graphs.

**Why study it.** Program states, data structures, trees, dependencies, state
machines, and search spaces are naturally discrete. The field teaches how to
model and reason about these structures without depending on exhaustive
experimentation.

**Planned topics.** Mathematical induction; invariants; recurrences; recursive
structures; summations; counting principles; relations; introductory trees and
graphs.

### Sequences, recurrences, and discrete summation

**Description.** The study of discretely indexed quantities, cumulative sums,
and rules that define each value from earlier values. These techniques form a
bridge between discrete mathematics, algorithms, and asymptotic analysis.

**Why study it.** Recursive programs, loop costs, divide-and-conquer algorithms,
dynamic programs, simulations over time, and many combinatorial structures are
naturally described by recurrences. Summation techniques turn repeated work
into analyzable expressions and often reveal a faster algorithm.

**Planned topics.** Arithmetic, geometric, and harmonic sequences; sigma
notation; finite and infinite sums; telescoping; multiple sums; finite
differences; floors and ceilings; first- and higher-order recurrences; linear
recurrences; characteristic roots; full-history recurrences; recurrence trees;
special sequences; asymptotic estimates; computational verification of
identities.

### Combinatorics

**Description.** The study of how to count, construct, and organize finite
configurations, especially when direct enumeration is expensive or impossible.

**Why study it.** Combinatorics makes it possible to estimate the size of search
spaces, understand combinatorial explosion, generate cases without duplication,
and select feasible algorithms. It is fundamental to combinatorial testing,
allocation, scheduling, discrete optimization, and sampling configurations.

**Planned topics.** Addition and multiplication principles; permutations;
arrangements; combinations; conditional counting; counting with constraints;
pigeonhole principle; inclusion-exclusion; bijective arguments; combinatorial
recurrences; generating functions at a conceptual level.

### Elementary algebra

**Description.** The study of expressions, equations, inequalities, functions,
and elementary symbolic manipulation. It is the operational language shared by
much of the mathematics that follows.

**Why study it.** Computational models frequently need to convert verbal
relationships into equations, isolate parameters, and understand how an output
changes when inputs change. Algebraic fluency prevents manipulation difficulties
from hiding the actual structure of an algorithm.

**Planned topics.** Expressions and identities; equations and inequalities;
polynomials; polynomial, rational, exponential, and logarithmic functions;
coordinate systems; elementary sequences and series.

### Number theory

**Description.** The study of properties of integers, especially divisibility,
prime numbers, and modular arithmetic.

**Why study it.** Number theory provides the mathematics of integer algorithms,
cryptography, checksums, calendars, cycles, hashing, and pseudorandom generation.
It is also an excellent laboratory for proofs, invariants, and algorithm
analysis.

**Planned topics.** Divisibility; Euclidean algorithm; greatest common divisor;
prime numbers; factorization; congruences; modular arithmetic; elementary
Diophantine equations; modular exponentiation.

### Abstract algebra

**Description.** The study of algebraic structures defined by operations and
laws, such as groups, rings, and fields.

**Why study it.** Abstract algebra teaches us to recognize when apparently
different systems obey the same rules. This perspective is useful in
cryptography, coding theory, symmetries, transformations, computer graphics,
and the design of correct abstractions. It will be a later field, not an initial
requirement.

**Planned topics.** Binary operations; groups and subgroups; symmetries;
homomorphisms; rings; introductory finite fields.

## 2. Space, motion, and continuous structures

### Geometry

**Description.** The study of shapes, positions, distances, angles, and the
properties of space. It includes Euclidean, analytic, and computational
perspectives.

**Why study it.** Geometry is indispensable to graphics, games, interfaces,
visualization, robotics, collision detection, maps, and spatial algorithms. It
also develops intuition for coordinates, metrics, and transformations.

**Planned topics.** Euclidean geometry; analytic geometry; coordinates;
distances; lines and planes; polygons; areas and volumes; transformations;
introductory computational geometry.

### Trigonometry

**Description.** The study of relationships between angles, triangles, circles,
and periodic functions.

**Why study it.** Trigonometry makes it possible to model rotation,
orientation, waves, oscillations, periodic motion, and projections. It appears
directly in computer graphics, audio, signals, computational physics, and
spatial simulations.

**Planned topics.** Sine, cosine, and tangent; the unit circle; identities; laws
of sines and cosines; periodicity; polar coordinates; vectors and rotations in
the plane.

### Linear algebra

**Description.** The study of vectors, matrices, linear systems, vector spaces,
and linear transformations.

**Why study it.** Linear algebra is the language of transformations,
many-variable models, 2D and 3D graphics, signal processing, statistics,
optimization, Markov chains, and machine learning. Implementing it manually
also exposes important questions of computational cost and numerical stability.

**Planned topics.** Vectors and matrices; matrix operations; linear systems;
Gaussian elimination; linear independence; basis and dimension; linear
transformations; determinants; eigenvalues and eigenvectors; orthogonality;
projections; matrix decompositions.

### Numerical linear algebra

**Description.** The study of reliable and efficient algorithms for linear
systems, matrix factorizations, least-squares problems, eigenvalues, and other
linear-algebra computations on finite-precision machines.

**Why study it.** A mathematically valid matrix formula may be slow or unstable
when implemented directly. Numerical linear algebra supports graphics,
statistics, optimization, scientific simulation, Markov models, PageRank, and
machine learning while making error, conditioning, sparsity, and computational
cost explicit.

**Planned topics.** Gaussian and Gauss-Jordan elimination; pivoting;
conditioning; residuals; stability; sparse and dense representations; LU, QR,
and Cholesky factorizations; least squares; Gram-Schmidt and its numerical
limitations; power iteration; numerical eigenvalue methods; iterative linear
solvers at an introductory level.

### Differential and integral calculus

**Description.** The study of change and accumulation through limits,
derivatives, and integrals, in one or several variables.

**Why study it.** Calculus provides tools for understanding rates of change,
local approximations, areas, accumulation, continuous densities, gradients, and
optimization. It is the basis of physical simulations, continuous models, and
many learning algorithms.

**Planned topics.** Limits; continuity; derivatives; differentiation rules;
integrals; fundamental theorem of calculus; series; partial derivatives;
gradient; Jacobian; Hessian; multiple integrals.

### Differential equations

**Description.** The study of equations that relate a function to its rates of
change, describing the continuous evolution of systems.

**Why study it.** Differential equations make it possible to model growth,
motion, epidemics, populations, inventories, circuits, and other systems that
change over time. In programming, they connect mathematical models to
step-by-step simulation methods.

**Planned topics.** Ordinary differential equations; initial-value problems;
systems of equations; qualitative solutions; Euler and Runge–Kutta methods;
elementary stability.

### Dynamical systems

**Description.** The study of how the state of a system evolves according to a
rule, in either discrete or continuous time.

**Why study it.** Dynamical systems teach us to analyze long-term behavior,
feedback, and sensitivity to initial conditions. They help us build simulations
in which local rules produce global patterns and distinguish stable behavior
from numerical artifacts.

**Planned topics.** State and evolution; iterated maps; equilibrium points;
stability; attractors; cycles; feedback; bifurcations; chaos treated carefully.

### Mathematical analysis

**Description.** The rigorous foundation of limits, continuity, convergence,
differentiation, and integration.

**Why study it.** Mathematical analysis develops the maturity required to know
when approximations and algorithms converge, which hypotheses a theorem needs,
and where intuition can fail. It will be studied gradually, after practical
experience with calculus.

**Planned topics.** Real numbers; sequences and series; convergence;
continuity; introductory compactness; convergence of functions; rigorous
foundations of calculus.

### Numerical analysis

**Description.** The study of algorithms that approximate mathematical
solutions and the errors produced by those approximations.

**Why study it.** Computers operate with finite resources and floating-point
numbers. Numerical analysis teaches us to detect instability, control errors,
and choose methods that work on a machine rather than only on paper.

**Planned topics.** Floating-point arithmetic; absolute and relative error;
conditioning; stability; root finding; interpolation; numerical differentiation
and integration; numerical solution of linear systems and differential
equations.

### Scientific computing

**Description.** The disciplined use of mathematical models, numerical
algorithms, simulation, experiments, and software to investigate systems that
cannot be understood through symbolic work alone.

**Why study it.** Scientific computing connects mathematics to executable
experiments. It develops reproducibility, error budgets, validation against
known cases, sensitivity analysis, parameter sweeps, and the ability to tell a
property of the modeled system from an artifact of the implementation.

**Planned topics.** Model formulation; units and dimensional analysis;
discretization; verification versus validation; parameter sweeps; sensitivity
analysis; reproducible experiments; benchmark construction; reference cases;
error propagation; experiment logs; visualization as diagnosis; computational
notebooks conceptually, while repository implementations remain ordinary
Python modules.

## 3. Uncertainty, data, and randomness

### Probability theory

**Description.** The study of mathematical models for uncertainty and
randomness, starting with sample spaces and extending to joint distributions and
convergence theorems.

**Why study it.** Probability makes it possible to build systems that reason
about uncertain outcomes, risks, and frequencies without confusing guesses,
possibility, and probability. It is central to simulation, randomized
algorithms, reliability, statistics, learning, and decision-making.

**Planned topics.** Sample spaces and events; probability axioms; conditional
probability; independence; Bayes' theorem; random variables; expectation,
variance, and covariance; discrete and continuous distributions; joint
distributions; distribution and density functions; transformations of random
variables; Bernoulli, binomial, geometric, Poisson, uniform, exponential,
normal, gamma, and related distribution families; probability-generating,
moment-generating, and characteristic functions at appropriate depths; law of
large numbers; central limit theorem.

### Statistics

**Description.** The study of how to describe data and infer properties of a
population or process from limited observations.

**Why study it.** Programs produce metrics and experiments, but numbers do not
interpret themselves. Statistics helps separate signal from noise, quantify
uncertainty, compare alternatives, and avoid unwarranted conclusions from
simulations or A/B tests.

**Planned topics.** Exploratory analysis; measures of location and dispersion;
sampling; estimators; bias and variance; confidence intervals; hypothesis tests;
regression; correlation; maximum likelihood; experimental design; correlation
versus causation.

### Bayesian inference

**Description.** The treatment of inference as updating probabilistic beliefs
in light of evidence.

**Why study it.** Bayesian inference offers a coherent way to combine prior
knowledge with data, update models sequentially, and produce predictions that
express uncertainty. It is useful in diagnosis, forecasting, personalization,
and decisions under incomplete information.

**Planned topics.** Prior; likelihood; posterior; evidence; posterior
predictive distribution; sequential updating; conjugate models; hierarchical
models; model comparison.

### Monte Carlo methods

**Description.** Methods that use random sampling to estimate mathematical
quantities or explore systems for which exact calculation is difficult.

**Why study it.** Monte Carlo methods make it possible to evaluate algorithms
and policies across thousands of scenarios, approximate integrals, measure
risks, and investigate large state spaces. Studying error prevents a convincing
simulation from being mistaken for a reliable conclusion.

**Planned topics.** Pseudorandom sampling; Monte Carlo estimators; standard
error and convergence; variance reduction; antithetic variates; importance
sampling; rejection sampling; bootstrap; sequential Monte Carlo; MCMC at a
later stage.

### Stochastic processes

**Description.** The study of families of random variables that represent the
evolution of uncertain systems over time or space.

**Why study it.** Stochastic processes model queues, failures, traffic, prices,
populations, propagation, and waiting times. They let us ask not only “what can
happen?” but also “when?”, “in what order?”, and “along which trajectory?”.

**Planned topics.** Bernoulli processes; random walks; Poisson processes;
waiting times; birth-and-death processes; hazard rates; martingales at a
conceptual level; stationary processes; branching processes; renewal processes;
Brownian motion; diffusion processes; covariance functions and trajectories.

### Markov chains

**Description.** Stochastic processes in which the distribution of the next
state depends on the present state according to a transition rule.

**Why study it.** Markov chains provide compact models for state systems,
behavior, queues, reliability, and search or ranking algorithms. They also form
an especially clear bridge between probability, graphs, and linear algebra.

**Planned topics.** States; transition matrices; distributions after multiple
steps; communicating classes; recurrence and transience; absorbing states;
stationary distributions; hitting times; higher-order chains; Hidden Markov
Models later.

### Queueing theory

**Description.** The study of systems in which demands arrive, wait, and receive
service under limited capacity.

**Why study it.** Queueing theory applies directly to servers, task queues,
networks, service systems, scheduling, and resource sizing. It explains why
small changes in load can produce large changes in waiting time.

**Planned topics.** Arrival and service processes; utilization; Little's law;
simple queues; queueing networks; priorities; discrete-event simulation.

### Renewal and reliability theory

**Description.** The study of systems that repeatedly reset after events and of
the probability that components or services continue to function over time.

**Why study it.** Renewal and reliability models apply to failures, repairs,
caches, maintenance, inventory replenishment, customer return, and service
lifetime. They connect waiting-time distributions, hazard rates, simulation,
queues, and operational decisions.

**Planned topics.** Interarrival and lifetime distributions; renewal counting
processes; renewal reward ideas; residual life; survival functions; hazard
rates; series and parallel reliability; repairable systems; availability;
failure simulation; reliability block models.

### Causal inference

**Description.** The study of when and how data can distinguish association
from causal effect.

**Why study it.** A program that learns from observations may find misleading
correlations. Causal inference provides language for interventions,
experiments, and confounders, improving automated decisions and the
interpretation of metrics.

**Planned topics.** Directed causal graphs; confounders; interventions;
introductory potential outcomes; adjustment criteria; randomized experiments;
the difference between observing and causing.

## 4. Networks, decisions, and action

### Graph theory

**Description.** The study of structures formed by vertices and edges, capable
of representing relationships and paths.

**Why study it.** Software dependencies, transportation networks, maps, syntax
trees, links, and social relationships are graphs. The field provides models
and algorithms for connectivity, search, flow, ordering, and network
optimization.

**Planned topics.** Directed and undirected graphs; weights; degrees; paths;
cycles; connectivity; components; trees; traversals; shortest paths;
topological sorting; Euler tours; Hamilton cycles; spanning trees; minimum
spanning trees; matchings; independent sets; cliques; edge and vertex coloring;
planarity; directed graphs; centrality; flows and cuts; cycle and cut spaces;
graph representations and classical complexity boundaries.

### Network science

**Description.** The study of collective properties of large networks and the
processes that take place on them.

**Why study it.** Network science helps explain propagation, robustness,
influence, cascades, and community formation in distributed systems, social
networks, infrastructure, and information systems.

**Planned topics.** Random networks; small-world networks; degree
distributions; hubs; communities; diffusion; contagion; cascades; robustness
and failures.

### Mathematical optimization

**Description.** The study of how to find the best possible solution according
to an objective function and a set of constraints.

**Why study it.** Programming frequently means choosing: reduce latency, cost,
or memory; increase coverage, quality, or return; satisfy competing constraints.
Optimization turns these trade-offs into explicit models and analyzable
algorithms.

**Planned topics.** Objective functions; constraints; feasible regions;
discrete and continuous optimization; convexity; gradients; linear programming;
integer programming; combinatorial optimization; local search; heuristics and
metaheuristics.

### Operations research

**Description.** The application of mathematical modeling, optimization, and
probability to decisions involving resources and operations.

**Why study it.** Operations research provides methods for turning vague
operational problems into variables, objectives, and constraints. It is useful
in logistics, allocation, routing, inventories, scheduling, and capacity
planning.

**Planned topics.** Resource allocation; transportation problems; routing;
scheduling; inventories; logistics; linear and integer programming; queues;
discrete-event simulation.

### Decision theory

**Description.** The study of choices among actions when their outcomes have
different values, costs, and uncertainties.

**Why study it.** Decision theory helps separate beliefs about the world from
preferences over outcomes. This separation is essential for recommendation,
planning, diagnosis, and agents that need to justify choices under risk.

**Planned topics.** Utility; expected value; risk aversion; decision trees;
value of information; Bayesian decision theory; introductory multicriteria
decision-making.

### Game theory

**Description.** The study of decisions in which each participant's outcome
also depends on the actions of others.

**Why study it.** Game theory models competition, cooperation, negotiation,
protocols, and incentives. It teaches us to anticipate strategic behavior and
design rules that do not reward undesirable effects.

**Planned topics.** Simultaneous and sequential games; pure and mixed
strategies; dominance; Nash equilibrium; zero-sum and non-zero-sum games;
repeated games; perfect and imperfect information; Bayesian games; cooperation
and coalitions.

### Markov decision processes

**Description.** Models that combine states, actions, probabilistic transitions,
and rewards to represent sequential decisions.

**Why study it.** Markov decision processes make it possible to program agents
that evaluate future consequences rather than only immediate rewards. They are
fundamental to planning, stochastic control, and reinforcement learning.

**Planned topics.** States; actions; rewards; policies; horizons; discounting;
value functions; Bellman equations; policy evaluation and improvement; value
iteration; partial observability later.

### Multi-armed bandit problems

**Description.** The study of repeated decisions in which exploration of
uncertain alternatives must be balanced against exploitation of the best-known
options.

**Why study it.** Multi-armed bandits provide simple and powerful models for
recommendation, adaptive testing, strategy selection, and systems that learn
while operating. They make the cost of learning and the regret caused by
suboptimal decisions explicit.

**Planned topics.** Exploration versus exploitation; regret; epsilon-greedy;
UCB; Thompson sampling; contextual bandits at a later stage.

### Information theory

**Description.** The study of how to quantify information, uncertainty,
compression, and statistical dependence.

**Why study it.** Information theory underpins compression, communication,
feature selection, anomaly detection, and comparison between distributions. It
also offers precise measures of surprise and information gain.

**Planned topics.** Entropy; joint and conditional entropy; mutual information;
Kullback–Leibler divergence; coding; compression; introductory channel
capacity.

### Control theory

**Description.** The study of how to influence the evolution of a system using
measurement, feedback, and control actions.

**Why study it.** Control theory is useful whenever a program must keep a
variable near a target despite disturbances: temperature, speed, server load,
inventory, or process behavior. It teaches us to design feedback without
causing instability.

**Planned topics.** State; output; setpoint; error; open-loop and closed-loop
control; feedback; stability; proportional, integral, and derivative control;
adaptive controllers at a later stage.

## 5. Algorithms, programming theory, and computational problem-solving

The subjects in this section are computer science disciplines rather than
branches of mathematics in the narrowest sense. They belong in Mathforge
because mathematical understanding is incomplete for our purposes until it can
be transformed into a correct and efficient program.

### Data structures

**Description.** The study of ways to organize data so that required operations
have clear semantics and predictable costs. A data structure is both a
representation and a set of supported operations with invariants.

**Why study it.** Choosing a representation often determines whether an
algorithm is simple or difficult, fast or slow, correct or fragile. Data
structures support everyday programming, technical interviews, simulation
engines, compilers, databases, schedulers, graph systems, and nearly every
nontrivial software system.

**Planned topics.** Arrays and dynamic arrays; strings; linked structures;
stacks; queues and deques; sets and maps; hash tables; heaps and priority
queues; trees; binary search trees; tries; graph representations; disjoint-set
union; dense and sparse representations; mutability and persistence at an
introductory level.

### Design and analysis of algorithms

**Description.** The study of procedures for solving computational problems,
together with methods for proving their correctness and measuring their use of
time and memory.

**Why study it.** A program can produce correct examples and still be wrong,
fail to terminate, or become unusable as input grows. Algorithm analysis makes
performance and correctness explicit. It also develops the transferable
problem-solving skills expected in software-engineering interviews without
reducing them to memorized tricks.

**Planned topics.** Problem specifications; preconditions and postconditions;
loop and structural invariants; termination; correctness arguments; time and
space complexity; best, worst, and average cases; asymptotic notation
`O`, `Ω`, and `Θ`; amortized analysis; empirical measurement versus theoretical
analysis; searching; sorting; selection; string processing; elementary graph
algorithms.

### Algorithmic paradigms

**Description.** The study of reusable strategies for constructing algorithms
from the structure of a problem rather than from a memorized implementation.

**Why study it.** Paradigms make unfamiliar problems recognizable. They help a
programmer decide whether to enumerate, decompose, cache, choose locally, prune,
randomize, approximate, or reorganize the state space. This is useful both in
real systems and in interview-style problem solving.

**Planned topics.** Exhaustive search; recursion; decrease and conquer; divide
and conquer; backtracking; pruning; greedy algorithms; dynamic programming;
memoization; branch and bound; randomized algorithms; online and streaming
algorithms; approximation algorithms; heuristics. Recurring techniques such as
two pointers, sliding windows, prefix sums, fast and slow pointers, interval
merging, sweep lines, bitmasks, monotonic stacks, and monotonic queues will be
treated as compositions of underlying ideas rather than recipes to memorize.

### Computational complexity

**Description.** The study of the resources required to solve classes of
problems and of the boundaries between tractable, intractable, approximable,
and undecidable computation.

**Why study it.** Complexity explains when better implementation is enough and
when the problem itself requires a different formulation, approximation,
parameter restriction, or heuristic. It prevents wasted effort on exhaustive
solutions that cannot scale and clarifies the value of reductions and lower
bounds.

**Planned topics.** Models of computation; input size; upper and lower bounds;
polynomial and exponential growth; tractability; decision and optimization
problems; reductions; the classes P and NP; NP-completeness; parameterized
thinking at an introductory level; space complexity; computability and
undecidability at a conceptual level.

### Formal methods and program verification

**Description.** The use of mathematical specifications and proof techniques to
state what programs should do and justify that implementations satisfy those
statements.

**Why study it.** Tests demonstrate behavior on selected executions; formal
reasoning addresses all executions covered by stated assumptions. The field
improves API contracts, invariant design, safety-critical logic, refactoring,
and the ability to find specification errors before implementation grows.

**Planned topics.** Preconditions and postconditions; assertions; state
relations; refinement; weakest-precondition ideas at a conceptual level; loop
invariants; termination variants; soundness and completeness; specification
composition; model checking at an introductory level; the complementary roles
of proof, testing, and static analysis.

### Programming language semantics and recursive definitions

**Description.** The study of how programming-language constructs acquire
precise meaning and how recursive data and programs are defined from smaller
instances.

**Why study it.** Semantics clarifies scope, mutation, aliasing, control flow,
recursion, and composition. It helps programmers reason about code independently
of surface syntax, design interpreters and domain-specific languages, and avoid
bugs caused by an unclear execution model.

**Planned topics.** Expressions and state; substitution; scope and binding;
operational and denotational viewpoints at an introductory level; arrays and
records; loops; procedures; recursion; recursive data; structural induction;
fixed-point ideas; parsing; interpreters; refinement between representations.

### Theory of computation and formal languages

**Description.** The study of abstract machines, languages, computability, and
the fundamental limits of algorithms.

**Why study it.** This field explains the structures behind regular
expressions, parsers, protocols, compilers, state machines, and decision
procedures. It also distinguishes a difficult computation from a task that no
general algorithm can solve.

**Planned topics.** Alphabets and formal languages; deterministic and
nondeterministic finite automata; regular expressions; grammars; pushdown
automata; Turing machines conceptually; decidability; reductions; the halting
problem; connections among automata, state machines, and parsers.

### Concurrency and interaction models

**Description.** The study of systems whose components execute, communicate,
or react without a single simple sequential order.

**Why study it.** Real programs coordinate tasks, messages, buffers, services,
and shared state. Mathematical models of concurrency expose races, deadlocks,
ordering constraints, safety properties, and liveness properties that ordinary
single-run testing may miss.

**Planned topics.** Interleavings; concurrent composition; shared and message-
passing state; atomicity; synchronization; producer-consumer systems; buffers;
deadlock; safety and liveness; monitors; channels; broadcast; event-driven and
reactive systems; deterministic simulation of concurrent schedules.

### Computational experimentation and benchmark design

**Description.** The study of how to design computational experiments and
benchmarks that measure the intended capability rather than a convenient but
misleading proxy.

**Why study it.** Simulators, algorithms, and intelligent systems need
evaluation protocols that are reproducible, discriminating, and connected to
real tasks. Good benchmark design prevents data leakage, ambiguous success
criteria, overfitting to examples, and conclusions unsupported by the evidence.

**Planned topics.** Research questions and hypotheses; scenario-grounded tasks;
unit-level versus system-level evaluation; baselines; controls; ablations;
metrics; calibration; leakage and contamination; dataset and case selection;
reproducibility; error analysis; benchmark validity; project-level evaluation;
human-in-the-loop experiments.

## 6. How this map will be used

Mathforge challenges do not need to belong to a single field. A module on
Markov chains can simultaneously exercise probability, matrices, graphs, and
numerical analysis while also requiring an appropriate representation and a
complexity argument. The module document records these combinations and their
concrete pedagogical order.

Specialized libraries will not replace implementation of the mathematical
mechanisms. If one is introduced in the future, it will be only after the manual
implementation and generally for comparison, validation, or work at scale.

Algorithmic practice will be longitudinal. Correctness, invariants,
representation choices, and computational cost will recur throughout the
mathematical modules rather than being confined to a single interview-preparation
unit.

The complete module order that operationalizes this body of knowledge lives in
[`docs/curriculum-modules.md`](curriculum-modules.md). Local book routing and
solution warnings live in [`books/CATALOG.md`](../books/CATALOG.md).
