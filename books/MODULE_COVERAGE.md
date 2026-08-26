# Mathforge Module Source Coverage

## Purpose

This document evaluates whether the books currently stored in `books/` provide
enough material to plan every module in the
[`complete curriculum roadmap`](../docs/curriculum-modules.md).

Coverage is evaluated collectively. A module does not need a textbook devoted
exclusively to its title when several local sources jointly cover its concepts,
prerequisites, examples, exercises, and important edge cases.

## Status definitions

- **Adequate:** Local sources are sufficient to anchor the module. External
  research may still improve examples or specialized details.
- **Partial:** Local sources cover meaningful foundations, but a major part of
  the planned module needs a better curricular source.
- **Gap:** No current local source can responsibly anchor the module.

This is a source audit, not a judgment about whether a module is ready to start.
Student prerequisites and demonstrated mastery remain separate requirements.

## Summary

| Status | Modules | Count |
| --- | --- | ---: |
| Adequate | locally anchored | 60 |
| Partial | useful material exists, but an important gap remains | 7 |
| Gap | no adequate curricular anchor | 0 |
| **Total** |  | **67** |

Every module now has at least meaningful local support. The collection is
sufficient to anchor 60 modules directly; the remaining 7 modules still need
stronger sources for important planned material.

## Phase I — Finite models, uncertainty, and experimentation

| Module | Status | Principal local support |
| --- | --- | --- |
| 01 — States, Rules, and Possible Worlds | Adequate | Levin; Cummings; Hehner |
| 02 — Counting Without Generating Everything | Adequate | Levin; *Concrete Mathematics*; Parberry and Gasarch |
| 03 — Algorithmic Foundations | Adequate | Parberry and Gasarch; Hehner; *Concrete Mathematics* |
| 04 — Exact Probability in Finite Spaces | Adequate | Grimmett and Stirzaker; *Concrete Mathematics* |
| 05 — Evidence, Dependence, and Bayes | Adequate | Grimmett and Stirzaker; Chernoff and Moses |
| 06 — Random Variables | Adequate | Grimmett and Stirzaker; *Concrete Mathematics* |
| 07 — Sampling and Reproducible Simulation | Adequate | Grimmett and Stirzaker |
| 08 — Statistics for Computational Experiments | Adequate | Pestman; Chernoff and Moses |
| 09 — Monte Carlo I | Adequate | Grimmett and Stirzaker; exact probability sources; White for simulation-based bandit evaluation |

## Phase II — Proof, discrete methods, and algorithms

| Module | Status | Principal local support or missing material |
| --- | --- | --- |
| 10 — Mathematical Proof and Counterexamples | Adequate | Cummings; Levin |
| 11 — Specifications, Invariants, and Program Correctness | Adequate | Hehner; Parberry and Gasarch |
| 12 — Induction, Recursion, and Recurrences | Adequate | Levin; *Concrete Mathematics*; Hehner; Parberry and Gasarch |
| 13 — Discrete Sums, Floors, and Asymptotics | Adequate | *Concrete Mathematics*; Parberry and Gasarch |
| 14 — Number Theory and Modular Algorithms | Adequate | *Concrete Mathematics*; Cummings |
| 15 — Algebraic Structures and Symmetry | Partial | Cummings introduces groups and modular sources provide examples; Satake and Sokolov supply advanced algebraic-group, Jordan, Lie, non-associative, and symmetry material but assume substantial prerequisites; introductory rings, fields, finite fields, and homomorphisms still need a dedicated first-course source |
| 16 — Generating Functions and Advanced Counting | Adequate | *Concrete Mathematics*; Levin |
| 17 — Data Structures | Adequate | Parberry and Gasarch; Hehner |
| 18 — Divide and Conquer, Search, and Sorting | Adequate | Parberry and Gasarch; Hehner; *Concrete Mathematics* |
| 19 — Exhaustive Search, Backtracking, and Constraint Solving | Adequate | Parberry and Gasarch; Hehner; Levin |
| 20 — Greedy Algorithms and Dynamic Programming | Adequate | Parberry and Gasarch; Gupta |
| 21 — Complexity, Reductions, and Computational Limits | Adequate | Parberry and Gasarch; *Concrete Mathematics*; Pettorossi for decidability and undecidability; Lattimore and Szepesvári for bandit lower bounds |
| 22 — Automata, Formal Languages, and Program Semantics | Adequate | Pettorossi provides the automata, grammars, parsing, Turing-machine, computability, and decidability sequence; Hehner provides program semantics, recursion, and formal execution |

## Phase III — Geometry, linear algebra, calculus, and numerical methods

| Module | Status | Principal local support |
| --- | --- | --- |
| 23 — Geometry, Trigonometry, and Vectors | Adequate | Thomas and Finney; Hefferon |
| 24 — Linear Systems and Gaussian Elimination | Adequate | Hefferon |
| 25 — Vector Spaces and Linear Transformations | Adequate | Hefferon; Loomis and Sternberg |
| 26 — Matrix Algorithms and Numerical Linear Algebra | Adequate | Hefferon; van Kan, Segal, and Vermolen |
| 27 — Eigenvalues, Spectral Methods, and Matrix Dynamics | Adequate | Hefferon |
| 28 — Calculus I | Adequate | Thomas and Finney; Loomis and Sternberg |
| 29 — Calculus II | Adequate | Thomas and Finney; Loomis and Sternberg |
| 30 — Multivariable Calculus and Gradients | Adequate | Thomas and Finney; Loomis and Sternberg |
| 31 — Differential Equations and Numerical Evolution | Adequate | Thomas and Finney; Loomis and Sternberg; Perko; van Kan, Segal, and Vermolen; Sokolov for advanced integrability extensions |
| 32 — Mathematical and Numerical Analysis | Adequate | Loomis and Sternberg; van Kan, Segal, and Vermolen |

## Phase IV — Continuous probability, inference, and scientific evaluation

| Module | Status | Principal local support or missing material |
| --- | --- | --- |
| 33 — Continuous Probability and Distribution Families | Adequate | Grimmett and Stirzaker; Pestman |
| 34 — Joint Probability and Transformations | Adequate | Grimmett and Stirzaker; Pestman |
| 35 — Convergence and Limit Theorems | Adequate | Grimmett and Stirzaker; Pestman; Lattimore and Szepesvári for concentration inequalities; Cover and Thomas for asymptotic equipartition and information-theoretic asymptotics |
| 36 — Statistical Estimation and Likelihood | Adequate | Pestman; Chernoff and Moses |
| 37 — Confidence, Hypothesis Tests, and Experimental Design | Adequate | Pestman and Chernoff–Moses cover confidence, testing, and power; Ding provides extensive randomization-based designs, stratification, rerandomization, matched experiments, and regression adjustment; White and Lattimore–Szepesvári add adaptive and optimal-design perspectives |
| 38 — Regression and Exploratory Data Analysis | Adequate | Pestman; Hefferon; Ding for regression adjustment, propensity methods, diagnostics, and the distinction between association and causal effect |
| 39 — Bayesian Inference | Adequate | Pestman and Chernoff–Moses cover elementary Bayesian estimation and decisions; Box and Tiao provide the classical inferential and hierarchical-model sequence; Lattimore and Szepesvári provide sequential Bayesian learning; Sell supplies modern computational and posterior-predictive applications |
| 40 — Monte Carlo II | Partial | Liang, Liu, and Carroll cover introductory importance and acceptance-rejection sampling plus advanced importance weighting; Pestman covers bootstrap; control variates, antithetic variables, stratification, and systematic rare-event estimation still need a dedicated source |
| 41 — MCMC and Sequential Monte Carlo | Partial | Liang, Liu, and Carroll provide the principal systematic advanced-MCMC coverage and Sell adds research-level variants; standard sequential Monte Carlo and particle filtering remain uncovered |
| 42 — Scientific Computing, Benchmarks, and Discovery Evaluation | Adequate | van Kan, Segal, and Vermolen; scientific-discovery evaluation paper; Hefferon; White for Monte Carlo comparison of adaptive algorithms |

## Phase V — Graphs, networks, and stochastic processes

| Module | Status | Principal local support or missing material |
| --- | --- | --- |
| 43 — Graphs I | Adequate | Bondy and Murty; Levin; Parberry and Gasarch |
| 44 — Graphs II | Adequate | Bondy and Murty; Parberry and Gasarch |
| 45 — Graphs III | Adequate | Bondy and Murty; Parberry and Gasarch; Gupta |
| 46 — Graphs IV | Adequate | Bondy and Murty; Parberry and Gasarch |
| 47 — Network Science and Diffusion | Partial | Ghosh and Ghosh cover gossip and overlays; random graphs, centrality, communities, and robustness need a network-science source |
| 48 — Markov Chains I | Adequate | Grimmett and Stirzaker; Hefferon |
| 49 — Markov Chains II | Partial | Long-term and absorbing behavior are covered, and Engelberg adds a Kalman-filter bridge; Hidden Markov Models and systematic discrete-state filtering still need a dedicated source |
| 50 — Discrete Stochastic Processes and Random Walks | Adequate | Grimmett and Stirzaker; *Concrete Mathematics* |
| 51 — Poisson, Continuous-Time, and Birth–Death Processes | Adequate | Grimmett and Stirzaker |
| 52 — Renewal, Queues, and Reliability | Adequate | Grimmett and Stirzaker; Gupta for operational applications |
| 53 — Stationary Processes and Time Series | Partial | Grimmett and Stirzaker and Cover and Thomas cover stationary processes and entropy rates; AR/MA modeling, diagnostics, and forecast validation still need a time-series source |
| 54 — Martingales, Brownian Motion, and Diffusion | Adequate | Grimmett and Stirzaker; Sell for diffusion-based sampling applications |

## Phase VI — Optimization, decisions, strategy, and learning by action

| Module | Status | Principal local support or missing material |
| --- | --- | --- |
| 55 — Continuous and Convex Optimization | Adequate | Gupta; Thomas and Finney; Loomis and Sternberg; Lattimore and Szepesvári for convex analysis and online optimization |
| 56 — Discrete and Combinatorial Optimization | Adequate | Parberry and Gasarch; Gupta; Bondy and Murty; Lattimore and Szepesvári for combinatorial bandits; Liang, Liu, and Carroll for annealing and stochastic-approximation applications |
| 57 — Operations Research and Mathematical Programming | Adequate | Gupta; Bondy and Murty; Parberry and Gasarch |
| 58 — Decision Theory and Utility | Adequate | Chernoff and Moses; Pestman; Lattimore and Szepesvári for sequential Bayesian decisions |
| 59 — Game Theory and Strategic Interaction | Adequate | Osborne and Rubinstein provide the principal sequence through strategic, extensive, repeated, Bayesian, bargaining, implementation, and coalitional games; Gupta and Chernoff–Moses provide gentler zero-sum and decision-theory bridges |
| 60 — Markov Decision Processes and Partial Observability | Partial | Lattimore and Szepesvári provide a systematic MDP and reinforcement-learning bridge; Zabczyk adds Bellman equations, value functions, and optimal control; Sell and Gupta add control and dynamic programming; POMDPs and belief-state planning still need a dedicated source |
| 61 — Multi-Armed Bandits | Adequate | White provides the practical entry through epsilon-greedy, softmax, UCB, simulation, and operational complications; Lattimore and Szepesvári provide the rigorous stochastic, adversarial, contextual, linear, combinatorial, nonstationary, and Bayesian sequence |

## Phase VII — Dynamics, control, information, causality, and interaction

| Module | Status | Principal local support or missing material |
| --- | --- | --- |
| 62 — Dynamical Systems | Adequate | Perko; Loomis and Sternberg; Hefferon; Engelberg and Zabczyk for controlled linear and nonlinear dynamics; Sokolov for advanced integrability and symmetry extensions |
| 63 — Control Theory | Adequate | Engelberg provides the main classical and modern sequence, including feedback, PID, state space, observers, and discrete-time control; Zabczyk supplies rigorous linear, nonlinear, and optimal control; Perko, Sell, and Hehner provide supporting bridges |
| 64 — Information Theory | Adequate | Stone provides conceptual orientation; Mansuripur provides the introductory coding-and-channel sequence; Cover and Thomas provide the comprehensive rigorous curriculum; Lattimore and Szepesvári and Hehner provide specialized bridges |
| 65 — Causal Inference | Adequate | Ding provides the comprehensive potential-outcomes, experimental, observational, estimation, sensitivity, instrumental-variable, and mediation sequence; Pearl's 2007 paper provides the conceptual entry; Pearl's 2013 paper provides structural causal models, DAGs, d-separation, interventions, identification, do-calculus, mediation, transportability, and missing-data theory |
| 66 — Concurrency, Communication, and Reactive Systems | Adequate | Hehner; Ghosh and Ghosh; Pettorossi for finite-state and transducer foundations |

## Phase VIII — Final synthesis

| Module | Status | Principal local support |
| --- | --- | --- |
| 67 — Integrated Mathematical Systems Laboratory | Adequate | All cataloged books and completed modules; domain-specific primary sources selected per project |

## Remaining coverage gaps

### Uncovered scope in partial modules

The repository is ready to support a strong start and a long sequence of study,
but the following seven modules still contain important material without a
sufficiently systematic local source:

- **15 — Algebraic Structures and Symmetry:** A gradual first course in groups,
  rings, fields, homomorphisms, and finite fields is still needed. The current
  advanced monographs do not replace this foundation.
- **40 — Monte Carlo II:** Control variates, antithetic variables, stratified
  sampling, and systematic rare-event estimation still need a dedicated
  treatment.
- **41 — MCMC and Sequential Monte Carlo:** MCMC is strongly covered, but
  standard Sequential Monte Carlo, particle filtering, particle degeneracy,
  and resampling strategies remain insufficiently covered.
- **47 — Network Science and Diffusion:** Random-graph models, centrality,
  community structure, and systematic network-robustness analysis still need a
  dedicated source.
- **49 — Markov Chains II:** Hidden Markov Models and systematic discrete-state
  filtering remain insufficiently covered.
- **53 — Stationary Processes and Time Series:** AR and MA models, diagnostics,
  forecasting workflow, and forecast validation still need a dedicated source.
- **60 — Markov Decision Processes and Partial Observability:** POMDPs, belief
  states, belief updates, and planning under partial observability remain
  insufficiently covered.

These are source-coverage limitations, not reasons to postpone the curriculum.
None of them blocks the early modules, and each can be resolved before the
student reaches the affected part of the roadmap.

### Acquisition order

The remaining partial-coverage needs can be addressed by adding sources in
approximately this order:

1. variance-reduction and rare-event Monte Carlo, plus sequential Monte Carlo;
2. Hidden Markov Models and discrete-state filtering;
3. POMDPs and reinforcement learning;
4. network science and time-series analysis;
5. introductory abstract algebra.

One carefully chosen source may cover more than one item. A book should be added
for a demonstrated curriculum need, not merely to make every module appear to
have a one-to-one textbook mapping.

## Maintenance rule

Recalculate this audit whenever the roadmap changes or a book is added, removed,
or replaced. Update the affected module entries in
[`docs/curriculum-modules.md`](../docs/curriculum-modules.md) at the same time.
