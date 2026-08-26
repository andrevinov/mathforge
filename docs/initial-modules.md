# Initial Mathforge Modules

## Purpose of this document

This document defines Mathforge's initial learning sequence. Unlike the body of
knowledge, the unit of learning here is the **module**: a deliberate combination
of mathematical and algorithmic material from different fields, organized
around a capability that can be demonstrated in programs.

This is not yet the complete list of project modules. The sequence ends when
there is enough foundation to open later tracks in advanced algorithms and data
structures, statistics, linear algebra, Markov chains, graphs, optimization,
and stochastic processes.

Each module will follow the cycle:

> understand → model → implement → test → explain → integrate

The Agent will write the challenges and tests; André will write the
implementations. By default, only the Python standard library will be used, and
no library function will replace the mathematical mechanism being studied.

## The longitudinal algorithmic spine

Algorithms are not confined to one module. From the beginning, challenges will
gradually require the student to reason about:

- the representation chosen for a mathematical object;
- the invariant that makes an algorithm correct;
- why the algorithm terminates;
- time and memory costs as input grows;
- exhaustive solutions as baselines;
- the point at which brute force becomes impractical;
- trade-offs between exactness, approximation, time, and memory;
- whether an earlier component should be reused or recomputed;
- recurring problem structures rather than memorized code templates.

Interview-style problems are appropriate when they isolate one of these
capabilities. They will be treated as mathematical and engineering exercises,
not as timed trick questions. The student should be able to explain why a
solution works, derive its complexity, and recognize meaningful variants.

Algorithmic concepts follow the same one-step progression as mathematical
concepts. A challenge will not introduce a new mathematical concept, a new data
structure, and a new optimization technique simultaneously unless all but one
have already been mastered.

## Module 1 — States, rules, and possible worlds

### Description

An introduction to the mathematical language used to describe discrete
systems. A state will be represented as an explicit combination of attributes;
rules will be predicates that classify states as valid or invalid; events will
be sets of states.

The module begins with examples small enough to enumerate and inspect in full.
The goal is not to study logic in the abstract for a long time, but to learn how
to turn statements into verifiable models.

### Why study this module

Programs operate on states and apply rules. Knowing how to declare a function's
domain precisely, combine conditions, and identify invariants reduces boundary
bugs and contradictory rules. This skill is useful in validators, rule engines,
permissions, state machines, filters, tests, and configuration systems.

By the end, the student should be able to answer: which states exist, which are
valid, and which rule accepts or rejects each one?

### Mathematical and algorithmic content explored

- propositional logic;
- predicates and quantifiers;
- set theory;
- Cartesian products;
- relations;
- theory of functions;
- cardinality and simple invariants;
- exhaustive enumeration of tiny finite domains;
- counterexamples as correctness evidence;
- elementary time and memory reasoning.

## Module 2 — Counting without generating everything

### Description

The study of techniques for determining the size of possibility spaces without
enumerating every element. Problems progress from independent choices to
configurations involving repetition, order, exclusions, and constraints.

Direct enumeration will first be used as an oracle for small instances. Then
formulas and recurrences must produce the same result without constructing every
case. Where generation is required, the student will compare naive enumeration
with recursive construction, backtracking, and elementary pruning.

### Why study this module

Search spaces grow quickly. Before writing a brute-force solution, a programmer
needs to estimate how many cases exist and recognize when an approach is not
feasible. Counting techniques help generate tests, plan algorithms, avoid
duplicates, and understand exponential costs.

By the end, the student should distinguish “I can describe the possibilities”
from “I can materialize all of them in memory,” and should know when an
algorithm's running time is dominated by the size of its output.

### Mathematical and algorithmic content explored

- addition and multiplication principles;
- permutations, arrangements, and combinations;
- conditional counting;
- combinations with constraints;
- pigeonhole principle;
- inclusion-exclusion principle;
- mathematical induction;
- recurrences;
- generating functions at a conceptual level;
- exhaustive generation;
- recursion and backtracking;
- elementary pruning;
- output-sensitive complexity;
- time and memory costs of materializing a search space.

## Module 3 — Algorithmic foundations: representation, search, and cost

### Description

An explicit first pass through data structures, algorithm correctness, and
complexity. Problems begin with operations on sequences and small collections,
then compare alternative representations and search strategies under clear
constraints.

The module will not be a disconnected collection of interview tricks. Each
challenge will isolate one reusable idea, establish its invariant, test it
exhaustively on small domains, and then vary the scale or representation.

### Why study this module

Mathematical models become useful software only when the program can process
them correctly and within available resources. This module develops the ability
to choose a data structure, justify an algorithm, and predict how performance
changes as inputs grow.

These capabilities are central to ordinary software work and technical
interviews. By the end, the student should be able to solve foundational search
and collection problems without relying on memorized templates, explain the
invariant that makes a solution correct, and derive its basic time and memory
costs.

### Mathematical and algorithmic content explored

- abstract data types and concrete representations;
- arrays, strings, linked structures, stacks, queues, sets, and maps;
- elementary hash-table behavior and collision concepts;
- linear search and binary search;
- elementary comparison-based sorting and selection;
- preconditions, postconditions, and loop invariants;
- termination arguments;
- time and space complexity;
- best, worst, and average cases;
- asymptotic notation `O`, `Ω`, and `Θ`;
- introductory amortized reasoning;
- recursion and divide-and-conquer structure;
- introductory two-pointer, sliding-window, and prefix-sum techniques;
- explicit trade-offs between preprocessing, query time, and memory.

## Module 4 — Exact probability in finite spaces

### Description

The construction of discrete probabilistic models that can be calculated
exactly. The student will work with coins, dice, cards, and urns before moving to
larger domains. The emphasis will be on correctly defining elementary outcomes
and preserving their multiplicities.

Probabilities will initially be represented by exact fractions. Simulation will
not be used as a substitute for a calculation that can still be performed by
enumeration or counting.

### Why study this module

Randomized algorithms and systems under uncertainty require a model, not just
calls to a random number generator. Defining the sample space prevents classic
mistakes, such as treating dice sums as equally likely or ignoring repeated
outcomes.

By the end, the student should be able to construct a discrete distribution,
calculate the probability of an event, and justify every assigned weight.

### Mathematical and algorithmic content explored

- sample spaces;
- events and operations on events;
- probability axioms;
- equally likely outcomes and multiplicity;
- finite discrete distributions;
- combinatorics;
- indicator functions;
- exact rational arithmetic;
- frequency maps;
- exhaustive enumeration as an exact solver;
- complexity of explicit sample spaces;
- representation trade-offs for distributions.

## Module 5 — Evidence, dependence, and Bayes

### Description

The study of how probabilities change when new information becomes known. The
module will contrast actual dependence with apparent coincidence and use
tables, trees, and enumeration to make conditioning visible.

Bayes' theorem will be derived from conditional probability and decomposition
of the sample space instead of being presented merely as a formula to memorize.

### Why study this module

Programs frequently make decisions after observing evidence: diagnostics, spam
filters, fault detection, and recommendation systems are examples. Without
correct conditioning, it is easy to reverse probabilities, assume nonexistent
independence, or ignore base rates.

By the end, the student should clearly distinguish `P(A | B)` from `P(B | A)`
and explain which assumptions support an update.

### Mathematical and algorithmic content explored

- conditional probability;
- independence of events;
- multiplication rule;
- law of total probability;
- Bayes' theorem;
- set partitions;
- probability trees;
- conditional counting;
- tree and table representations of evidence;
- reuse of intermediate counts;
- consistency checks across equivalent computations.

## Module 6 — Random variables: measuring uncertain outcomes

### Description

The transformation of elementary outcomes into relevant quantities. The
student will build probability mass functions and manually implement measures
such as expectation, variance, standard deviation, and covariance.

Pairs of random variables, joint distributions, and marginal distributions will
also be introduced through small discrete examples.

### Why study this module

In practice, knowing only which state occurred is rarely enough. We want to
measure the cost, duration, reward, demand, or risk associated with the state.
Random variables form this bridge. Expectation makes it possible to compare
average outcomes; variance and covariance reveal risk and dependence that the
mean alone hides.

By the end, the student should be able to turn a state model into a distribution
of metrics and interpret its measures without using the `statistics` module.

### Mathematical and algorithmic content explored

- functions and the image of a function;
- discrete random variables;
- probability mass functions;
- discrete cumulative distribution functions;
- expectation;
- moments;
- variance and standard deviation;
- covariance;
- joint and marginal distributions;
- transformations of discrete random variables;
- grouping outcomes with maps;
- dense versus sparse distribution representations;
- one-pass and multi-pass computation trade-offs.

## Module 7 — Sampling and reproducible simulation

### Description

The construction of mechanisms that transform uniform pseudorandom numbers into
outcomes from other discrete distributions. The student will build weighted
samplers, simulate repeated processes, and design reproducible experiments
through seeds and explicit random-generator injection.

Whenever possible, simulated results will be compared with exact models built
in previous modules.

### Why study this module

Simulation is not merely running `random.choice` inside a loop. It is necessary
to know which distribution produces the results, how to reproduce an
experiment, and how to detect bias in a sampler. This discipline is valuable in
randomized tests, procedural generation, risk assessment, and algorithm
experimentation.

By the end, the student should be able to implement and validate a weighted
discrete sampler without using `random.choices`.

### Mathematical and algorithmic content explored

- uniform and discrete distributions;
- cumulative probabilities;
- inverse transformation in the discrete case;
- Bernoulli trials;
- independence;
- empirical frequencies;
- an intuitive introduction to the law of large numbers;
- absolute and relative error;
- foundations of pseudorandom numbers;
- cumulative-table representation;
- linear and binary search over cumulative weights;
- preprocessing versus sampling-time trade-offs;
- deterministic dependency injection for tests.

## Module 8 — Statistics for computational experiments

### Description

An introduction to describing and interpreting data produced by simulations.
The student will implement fundamental statistics, study their variation across
samples, and learn to communicate results together with their uncertainty.

The module will distinguish properties of a theoretical distribution,
statistics computed from a sample, and estimates of population properties.

### Why study this module

Running a simulation is easy; drawing a valid conclusion from it is harder.
This module prevents isolated averages, convincing plots, or a single seed from
being treated as sufficient evidence. The skill applies to benchmarks, load
tests, product experiments, and performance analysis.

By the end, the student should be able to plan repetitions, summarize results,
quantify error, and explain the limits of the conclusions.

### Mathematical and algorithmic content explored

- population and sample;
- mean, median, quantiles, and histograms;
- population and sample variance;
- estimators, bias, and standard error;
- sampling distributions;
- law of large numbers;
- an introductory view of the central limit theorem;
- introductory confidence intervals;
- exploratory data analysis;
- correlation versus causation;
- streaming summaries;
- stable one-pass and two-pass algorithms;
- numeric stability and accumulated floating-point error;
- complexity of repeated experiments.

## Module 9 — Monte Carlo I: computing through experimentation

### Description

The deliberate use of random sampling to estimate probabilities, expectations,
and other quantities for which exact calculation is expensive. The student will
derive estimators, measure their convergence, and compare strategies that
produce estimates with different costs and variances.

The module will culminate in a system with two paths: an exact solver for small
instances and a Monte Carlo estimator for large instances.

### Why study this module

Many real problems have clear models but state spaces too large for enumeration.
Monte Carlo provides a computational way forward, provided its error is measured
and communicated. Comparison with exact cases teaches when to trust an
approximation and how much additional precision costs.

By the end, the student should be able to choose an estimator, justify its
correctness, measure its error, and recognize that more samples produce
convergence rather than a guarantee of monotonic improvement.

### Mathematical and algorithmic content explored

- Monte Carlo estimators;
- expectation and variance of estimators;
- standard error;
- convergence in probability;
- law of large numbers;
- central limit theorem;
- confidence intervals;
- estimation of sums, probabilities, and geometric areas;
- introductory variance reduction;
- computational cost analysis;
- batching and streaming samples;
- stopping rules at an introductory level;
- exact-versus-approximate algorithm selection;
- opportunities and limits of parallel independent trials.

## Boundary of this initial sequence

After these modules, there will be enough foundation to follow several tracks
without losing the connections between them:

- linear algebra and Markov chains;
- graphs and network science;
- calculus, continuous probability, and optimization;
- stochastic processes and queues;
- statistical and Bayesian inference;
- decision theory, game theory, and MDPs;
- advanced data structures and string algorithms;
- greedy algorithms, dynamic programming, and advanced backtracking;
- graph algorithms and computational complexity.

These tracks will be specified after the initial modules have produced evidence
about the most appropriate pace, difficulties, and depth.
