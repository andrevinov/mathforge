# Module 01 — States, Rules, and Possible Worlds

## Purpose

This module develops the mathematical language needed to describe finite
computational systems precisely.

A program often has:

- a collection of possible states;
- rules that accept or reject states;
- transformations from one representation to another;
- relationships among objects;
- properties that must remain true.

These familiar programming ideas are instances of propositions, predicates,
sets, functions, relations, and invariants. The purpose of this module is to
make those structures explicit enough to model, implement, test, and explain.

This is the first Mathforge module. It has no mathematical prerequisite beyond
basic arithmetic and ordinary reasoning, but it assumes introductory Python
fluency.

## Why this module matters for programming

Many software defects begin before the code is written: the possible states are
unclear, a rule is ambiguous, two conditions are mistakenly treated as
equivalent, or a transformation silently loses information.

The material in this module supports everyday programming tasks such as:

- validating configuration and user input;
- implementing permissions and business rules;
- describing feature-flag behavior;
- filtering and classifying records;
- detecting contradictory policies;
- representing state machines;
- reconciling collections of identifiers;
- specifying compatibility and dependency relationships;
- generating exhaustive tests for small domains;
- stating and checking invariants.

The long-term payoff is the ability to replace vague statements such as “this
case should probably be allowed” with precise, testable rules over an explicit
domain.

## Learning outcomes

By the end of the module, the student should be able to:

- translate a verbal rule into a precise Boolean condition;
- distinguish implication from equivalence and identify necessary and
  sufficient conditions;
- distinguish a proposition from a predicate;
- reason about universal and existential statements;
- identify counterexamples to claims;
- model collections and events as sets;
- use set operations to express relationships among collections;
- reason about complements and De Morgan's laws over a declared universe;
- construct finite state spaces from Cartesian products;
- distinguish the domain, codomain, and image of a function;
- reason about composition and information loss in mappings;
- represent a binary relation explicitly;
- audit reflexivity, irreflexivity, symmetry, antisymmetry, and transitivity
  independently;
- connect equivalence relations with partitions;
- recognize a partial order;
- state an invariant and determine whether declared transitions preserve it;
- explain the computational cost of exhaustive enumeration in simple cases.

## Mathematical content to review

The material below describes the module as a whole. Do not wait to master every
item before beginning the first challenge. Review each section when its
corresponding challenge becomes active.

### 1. Propositional logic

Review:

- propositions and truth values;
- negation;
- conjunction and disjunction;
- exclusive versus inclusive alternatives;
- implication and biconditional statements;
- operator precedence and grouping;
- truth tables;
- logical equivalence;
- tautologies and contradictions;
- De Morgan's laws;
- necessary and sufficient conditions.

The important programming connection is that a Boolean expression is not just
syntax: it represents a claim about a state. Two expressions that look
different may express the same rule, while two expressions that look similar
may differ on a single critical case.

### 2. Predicates and quantifiers

Review:

- predicates as statements containing variables;
- the domain over which a predicate is interpreted;
- universal quantification;
- existential quantification;
- witnesses and counterexamples;
- scope of a quantifier;
- negation of quantified statements;
- the difference between “all,” “some,” and “none.”

Predicates are the mathematical model behind validators, filters, assertions,
and eligibility rules. Quantifiers describe requirements over collections of
records or states.

### 3. Sets and finite state spaces

Review:

- elements and membership;
- the empty set;
- equality of sets;
- subsets and proper subsets;
- union, intersection, difference, and complement;
- disjoint sets;
- symmetric difference;
- complements relative to an explicit universal set;
- De Morgan's laws for sets;
- power sets;
- Cartesian products;
- finite cardinality;
- sets of tuples as state spaces.

Pay special attention to the distinction between a set and a sequence. Sets do
not preserve duplicates, and mathematical set equality does not depend on
order.

### 4. Functions

Review:

- functions as mappings;
- domain, codomain, and image;
- total and partial functions at a conceptual level;
- function composition;
- identity functions;
- injective, surjective, and bijective functions;
- inverse functions;
- indicator functions.

In programming, a callable may behave like a mathematical function only under
certain assumptions. Be prepared to state those assumptions rather than
treating every Python function as automatically equivalent to a mathematical
one.

### 5. Relations

Review:

- ordered pairs;
- binary relations as sets of ordered pairs;
- relations on one set and between two sets;
- reflexive, irreflexive, symmetric, antisymmetric, and transitive properties;
- equivalence relations;
- equivalence classes and partitions;
- partial orders;
- the distinction between a relation and a function.

Relations appear in compatibility tables, aliases, permissions, dependencies,
preferences, and many-to-many data. Graphs will later provide another way to
view many relations, but graph algorithms are outside this module.

### 6. Invariants and finite models

Review:

- state as an assignment of values to attributes;
- valid and invalid states;
- invariants as properties that must always hold;
- transitions that preserve or violate an invariant;
- transition relations over finite state spaces;
- exhaustive enumeration of a small finite domain;
- counterexamples as evidence that a universal claim is false;
- basic time and memory costs of materializing finite state spaces.

The goal is not yet formal program verification. The goal is to state important
properties precisely enough that code and tests can check them.

## Python knowledge to review

The challenges assume familiarity with:

- `bool` values and comparison operators;
- `if`, `elif`, and `else`;
- functions, parameters, return values, and type hints;
- tuples and unpacking;
- lists, sets, frozen sets, and dictionaries;
- iteration with `for` and `while`;
- basic comprehensions;
- raising and handling `ValueError` and `TypeError`;
- importing a module;
- reading a `pytest` failure.

A challenge may prohibit a convenient built-in when implementing its mechanism
manually is the mathematical lesson. Each challenge README will state such
constraints explicitly.

## Important distinctions

Throughout this module, keep these distinctions visible:

- proposition versus predicate;
- value versus statement about a value;
- element versus subset;
- set versus ordered sequence;
- ordered pair versus unordered pair;
- relation versus function;
- domain versus codomain versus image;
- valid state versus reachable state;
- example versus proof;
- failed example versus counterexample;
- implementation behavior versus mathematical specification.

Confusing either side of one of these pairs often produces code that works for
the examples but fails for the underlying problem.

## Module milestones

### Milestone 1 — Boolean rules

Translate, evaluate, enumerate, compare, and audit implications among finite
Boolean rules, including necessary and sufficient conditions.

### Milestone 2 — Predicates and quantified requirements

Apply rules to values and collections, and distinguish universal claims from
existential ones.

### Milestone 3 — Sets and state-space construction

Represent collections mathematically, reason about their boundaries and
complements, and construct finite spaces of possible configurations.

### Milestone 4 — Functions and mappings

Describe transformations precisely and determine whether they preserve or lose
information.

### Milestone 5 — Relations

Represent pairwise structure; audit each major relation property in a small
step; and then recognize equivalence and ordering structures.

### Milestone 6 — Integrated finite models

First determine whether transitions preserve an invariant, then combine states,
rules, mappings, relations, and invariants in one small system.

## Evidence of mastery

Completion of all planned files is not sufficient by itself. Mastery requires
evidence that the student can:

- implement the mathematical structures without hidden library machinery;
- predict important results before running the code;
- explain why the implementation matches the mathematical definition;
- identify assumptions and counterexamples;
- distinguish a failed implication from a failed equivalence;
- design or recognize useful invariants;
- explain why a transition preserves an invariant or provide a violating
  transition;
- estimate when exhaustive enumeration is reasonable;
- recognize these structures in a problem that does not name them explicitly.

The module plan is recorded in [PROBLEMS.md](PROBLEMS.md). It is provisional and
will be revised in response to evidence from each completed challenge.

## Scope boundaries

This module deliberately does not attempt to teach:

- combinatorial counting formulas;
- probability;
- graph traversal algorithms;
- formal proof systems;
- asymptotic analysis beyond simple enumeration costs;
- symbolic logic software;
- SAT or constraint solvers.

Those subjects depend on the language developed here and will appear in later
modules.
