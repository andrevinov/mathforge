# Mathforge Mathematical Body of Knowledge

## Purpose of this document

This document is the reference map of the mathematical fields we intend to
study in Mathforge. It describes **what makes up the curriculum**, not the order
in which the subjects will be studied.

The fields below naturally overlap. Markov chains, for example, use probability
and linear algebra; optimization appears in operations research, control, and
reinforcement learning. This overlap is desirable: mastering mathematics means
recognizing the same structure in different problems.

The inclusion criterion is not merely “this may be useful in one specific
project.” We want fields that improve the general ability to:

- represent problems precisely;
- recognize structures and invariants;
- design algorithms;
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
variables; law of large numbers; central limit theorem.

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
conceptual level.

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
topological sorting; centrality; flows and cuts.

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

## 5. How this map will be used

Mathforge challenges do not need to belong to a single field. A module on
Markov chains can simultaneously exercise probability, matrices, graphs, and
numerical analysis. The module document records these combinations and their
concrete pedagogical order.

Specialized libraries will not replace implementation of the mathematical
mechanisms. If one is introduced in the future, it will be only after the manual
implementation and generally for comparison, validation, or work at scale.
