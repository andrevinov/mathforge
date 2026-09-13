# Module 01 Problem Plan — States, Rules, and Possible Worlds

## Plan status

**Module status:** Active

**Original challenge count:** 25

**Current planned challenge count:** 27

This is an adaptive curriculum plan, not a fixed contract. Challenge count,
order, scope, and reuse decisions may change after each student implementation.
A smaller intermediate problem will be inserted whenever the next conceptual
step proves too large. A redundant problem may be skipped when mastery is
already evident.

Only one challenge becomes active at a time. No problem directory is created
until the student explicitly requests the first or next problem.

## Module purpose

Develop the ability to represent finite states, rules, mappings, relationships,
transitions, and invariants precisely enough to implement and test them.

## Prerequisites

There are no prerequisite Mathforge modules.

The student should already be able to:

- write and call simple Python functions;
- use Boolean expressions and conditionals;
- iterate over a collection;
- use tuples, lists, sets, and dictionaries at an introductory level;
- read a function signature and a basic `pytest` failure.

Any gap in these programming prerequisites should be handled as a small review,
not silently converted into mathematical difficulty.

## Curriculum Sources

The module sequence was checked against the following local sources:

- **Primary:** Oscar Levin, *Discrete Mathematics: An Open Introduction*,
  Sections 0.2–0.4 and Chapter 3, for implications, necessary and sufficient
  conditions, predicates, quantifiers, sets, functions, truth tables, logical
  equivalence, and counterexamples.
- **Primary:** Jay Cummings, *Proofs: A Long-Form Mathematics Textbook*, Chapters
  3, 5, 8, and 9, for sets, complements, De Morgan's laws, power sets,
  Cartesian products, logic, functions, relation properties, equivalence
  relations, and partial orders.
- **Programming bridge:** Eric Hehner, *A Practical Theory of Programming*,
  Chapters 1–4 and Section 5.4, for binary expressions, predicates, functions,
  quantifiers, specifications, program behavior, assertions, and invariants.
- **Correctness reference:** Ian Parberry and William Gasarch, *Problems on
  Algorithms*, Chapter 5, for the later transition from exhaustive examples to
  correctness reasoning.

Levin contains selected hints and solutions, and Parberry and Gasarch contains
chapter-level hints and solutions. These parts are validation sources only and
must not be used to disclose a challenge solution. See
[`books/CATALOG.md`](../../books/CATALOG.md) for full routing and source-use
policy.

## Mathematical milestones

1. **Boolean rules:** propositions, truth assignments, implication, necessary
   and sufficient conditions, and equivalence.
2. **Predicates and quantifiers:** rules over domains, universal and existential
   claims, witnesses, counterexamples, and quantified negation.
3. **Sets and state spaces:** membership, set operations, complements, De
   Morgan's laws, power sets, and Cartesian products.
4. **Functions and mappings:** domain, codomain, image, composition,
   injectivity, surjectivity, and bijectivity.
5. **Relations:** pair representation; reflexive, symmetric, antisymmetric, and
   transitive behavior; equivalence; and partial order.
6. **Invariants and integration:** transition preservation followed by a finite
   system that combines the module's mathematical structures.

## Evidence required for module mastery

The student must eventually demonstrate the ability to:

- translate plain-language rules into correct predicates;
- test finite Boolean claims exhaustively;
- distinguish implication from equivalence and necessary from sufficient;
- produce or interpret witnesses and counterexamples;
- distinguish universal and existential requirements;
- model finite collections and state spaces as sets;
- reason about a set relative to a declared universe;
- describe and classify finite functions;
- represent finite relations and audit their properties independently;
- state an invariant and test whether transitions preserve it;
- integrate these structures without being told which one to use;
- explain correctness, assumptions, and basic enumeration cost.

## Future fields that depend on this module

- discrete mathematics and proof;
- combinatorics and probability spaces;
- algorithms, specifications, and verification;
- graph theory and state machines;
- optimization over finite domains;
- Markov chains and Markov decision processes.

## Milestone 1 — Boolean rules

### 01 — Feature Release Gate

**Status:** Completed

**Problem idea:** Implement the decision rule used by a deployment service to
decide whether a feature may be released from a few Boolean facts such as
approval, test status, maintenance mode, and emergency override.

**New concept:** Compound propositions using negation, conjunction, and
disjunction. This small group is inseparable in the first useful policy.

**Reinforces:** Python Boolean values, comparisons, conditionals, and total
functions over a tiny finite domain.

**Prerequisites:** Ability to read a verbal rule and evaluate a simple Boolean
expression.

**Why this step is next:** It exposes the smallest useful mathematical object
in the module—a proposition—inside an ordinary programming rule.

**Likely variants:** Change which requirements the emergency override bypasses;
transfer the rule shape to an account-access decision.

**Reuse:** Standalone. Later problems may call the completed rule without
depending on its implementation.

**Source basis:** Levin Sections 0.2 and 3.1; Cummings Chapter 5; original
feature-release adaptation.

### 02 — Boolean Assignment Generator

**Status:** Active

**Problem idea:** Generate every ordered tuple of Boolean values for a requested
number of positions, without yet naming the positions or evaluating a policy.

**New concept:** Systematic exhaustive enumeration of a finite Boolean state
space.

**Reinforces:** Boolean values, tuples, iteration, deterministic order, and the
idea that each additional Boolean choice enlarges the possible state space.

**Prerequisites:** Problem 01 and the ability to build a list while iterating.

**Why this step is next:** It isolates assignment generation from all policy,
dictionary, and callable concerns in the original truth-table challenge.

**Progression evidence:** Problem 01 passed its exhaustive suite, but the first
attempt at the original Problem 02 showed that generating all assignments while
also evaluating an arbitrary policy was too large a conceptual jump. This
smaller step targets the unfinished state-generation capability directly.

**Likely variants:** Represent truth values as `"F"` and `"T"`; generate the
same assignments lazily after generators have been studied.

**Reuse:** Standalone. Its output contract and enumeration reasoning are
composed with policy evaluation in Problem 04.

**Source basis:** Levin Section 3.1 and Cummings Section 5.2 for
systematic truth-table rows over one or more propositions; original finite-state
generator adaptation.

### 03 — Policy Assignment Evaluator

**Status:** Planned

**Materialization note:** Its directory was created early at the student's
explicit request for both preparatory challenges. Problem 02 remains the only
active challenge.

**Problem idea:** Given flag names, one aligned Boolean assignment, and a
policy callable, construct the named state and return the policy's result.

**New concept:** Interpreting a truth assignment as a mapping from named
propositions to Boolean values.

**Reinforces:** Positional correspondence, dictionaries, callable arguments,
compound propositions, and exact Boolean results.

**Prerequisites:** Problem 02 and the ability to call a supplied function.

**Why this step is next:** Problem 02 generates assignments without interpreting
them; this adds names and evaluates exactly one assignment without an
exhaustive loop.

**Likely variants:** Return the named state together with the result; evaluate
two policies on the same assignment.

**Reuse:** Standalone. Its state-alignment and evaluation reasoning are composed
with enumeration in Problem 04.

**Source basis:** Levin Section 3.1 and Cummings Section 5.2 for evaluating a
proposition under an assignment; Hehner Chapters 1 and 3 for functions and
predicates; original single-row policy adaptation.

### 04 — Truth Table Reporter

**Status:** Revised

**Problem idea:** Report the result of a Boolean policy for every possible
assignment of a small declared set of flags.

**New concept:** A truth table as the complete pairing of a finite Boolean
domain with the results of a proposition over that domain.

**Reinforces:** Problems 02 and 03, compound propositions, positional
correspondence, and deterministic finite enumeration.

**Prerequisites:** Problems 02 and 03.

**Why this step is next:** The student now composes two separately practiced
capabilities: generating the full ordered domain and interpreting one of its
assignments.

**Progression evidence:** This challenge was originally Problem 02. The
student's difficulty showed that it combined multiple unpracticed programming
operations, so it was deferred and preceded by two diagnostic steps. The
student's existing draft is preserved in its new location.

**Likely variants:** Include named intermediate columns; increase the number of
flags while preserving deterministic row order.

**Reuse:** Integrates the capabilities from Problems 02 and 03 in one
standalone solution.

**Source basis:** Levin Section 3.1 and Cummings Section 5.2 for
systematic truth-table rows over two or more propositions; original
diagnostic-tool adaptation.

### 05 — Policy Implication Auditor

**Status:** Planned

**Problem idea:** Determine whether satisfying one finite Boolean policy always
guarantees another and report a state that disproves the guarantee when it
fails.

**New concept:** Logical implication, including necessary and sufficient
conditions.

**Reinforces:** Truth tables, exhaustive testing, and counterexamples.

**Prerequisites:** Problem 04 and familiarity with evaluating two rules on the
same assignment.

**Why this step is next:** The student already knows every row of a policy; this
adds one directional claim between two policies.

**Likely variants:** Audit the reverse implication; classify a condition as
necessary, sufficient, both, or neither.

**Reuse:** May import the truth-assignment engine from Problem 04.

**Source basis:** Levin Section 0.2 and Cummings Chapter 5 for implications and
counterexamples; original policy-contract adaptation.

### 06 — Policy Equivalence Auditor

**Status:** Planned

**Problem idea:** Compare two Boolean policies over a declared finite domain and
report whether they always agree, including a disagreement state when they do
not.

**New concept:** Logical equivalence and biconditional meaning.

**Reinforces:** Both directions of implication, truth tables, exhaustive finite
testing, and counterexamples.

**Prerequisites:** Problem 05 and the distinction between a one-way guarantee
and equal behavior.

**Why this step is next:** It composes the directional reasoning from Problem
05 into a stronger comparison without changing the domain.

**Likely variants:** Detect tautologies and contradictions; audit a simplified
production rule against its original form.

**Reuse:** May extend the engines from Problems 04 and 05.

**Source basis:** Levin Chapter 3 and Cummings Chapter 5 for equivalence;
original policy-audit adaptation.

## Milestone 2 — Predicates and quantified requirements

### 07 — Deployment Record Validator

**Status:** Planned

**Problem idea:** Decide whether one structured deployment record satisfies a
documented collection of eligibility rules.

**New concept:** Predicates interpreted over an explicit domain.

**Reinforces:** Boolean rules and careful translation from prose.

**Prerequisites:** Milestone 1, functions, and tuples or dictionaries.

**Why this step is next:** Earlier propositions used Boolean flags; this adds
variables whose values come from a meaningful domain.

**Likely variants:** Validate a user-registration record; return the names of
failed rules without changing eligibility semantics.

**Reuse:** Designed to become the predicate used by Problems 08 and 09.

**Source basis:** Levin Section 0.2 and Hehner Chapters 1 and 3 for predicates;
original deployment-record adaptation.

### 08 — Fleet-Wide Compliance Check

**Status:** Planned

**Problem idea:** Decide whether every deployment record in a fleet satisfies a
provided compliance predicate, including the empty-fleet case.

**New concept:** Universal quantification.

**Reinforces:** Predicates, explicit domains, and boundary behavior.

**Prerequisites:** Problem 07 and clarity about the population being checked.

**Why this step is next:** A rule about one object becomes a claim about every
object, with no other conceptual change.

**Likely variants:** Restrict the domain to one environment; return a violating
record when compliance fails.

**Reuse:** May import the validator from Problem 07.

**Source basis:** Levin Section 0.2, Cummings Chapter 5, and Hehner Chapter 3;
original fleet-compliance adaptation.

### 09 — Incident Witness Finder

**Status:** Planned

**Problem idea:** Search system records for evidence that an alert condition
occurs, returning a concrete witness when one exists.

**New concept:** Existential quantification and witnesses.

**Reinforces:** Predicates, collection domains, and evidence for a Boolean
claim.

**Prerequisites:** Problem 08 and applying a predicate across a collection.

**Why this step is next:** It introduces the other fundamental quantified claim
while retaining the same record-and-predicate model.

**Likely variants:** Return every witness; search specifically for a
counterexample to universal compliance.

**Reuse:** May reuse the predicate contract from Problem 07.

**Source basis:** Levin Section 0.2 and Cummings Chapter 5 for existential
claims and witnesses; original incident-search adaptation.

### 10 — Compliance Negation Auditor

**Status:** Planned

**Problem idea:** Check whether paired compliance queries correctly express a
quantified requirement and its negation, reporting a finite collection that
exposes an incorrect rewrite.

**New concept:** Negation of quantified statements.

**Reinforces:** Universal and existential quantification, equivalence, and
counterexamples.

**Prerequisites:** Problems 06, 08, and 09.

**Why this step is next:** It composes the two quantifiers already implemented
and changes only how a quantified claim is negated.

**Likely variants:** Audit “none” versus “not some”; transfer the logic to
permissions or inventory records.

**Reuse:** May import the universal and existential query engines.

**Source basis:** Levin Sections 0.2 and 3.1 and Cummings Chapter 5 for
quantifier negation; original compliance-audit adaptation.

## Milestone 3 — Sets and state-space construction

### 11 — Access Scope Containment

**Status:** Planned

**Problem idea:** Determine whether all permissions requested by a service are
contained in its granted permissions and report requests outside the scope.

**New concept:** Set membership and subset containment.

**Reinforces:** Universal claims, witnesses, and duplicate-insensitive data.

**Prerequisites:** Milestone 2 and introductory familiarity with Python sets.

**Why this step is next:** It reinterprets a familiar compliance question using
a collection whose equality and containment ignore order.

**Likely variants:** Check proper containment; distinguish required, optional,
and forbidden permissions.

**Reuse:** Its normalized permission representation may be reused by Problem
12.

**Source basis:** Levin Section 0.3 and Cummings Chapter 3 for membership and
subsets; original access-scope adaptation.

### 12 — Permission Set Reconciler

**Status:** Planned

**Problem idea:** Compare two permission snapshots and report shared, added,
removed, and combined permissions without treating order or duplicates as
meaningful.

**New concept:** Union, intersection, and difference as one operational family
over the same two sets.

**Reinforces:** Membership, subsets, cardinality, and precise output contracts.

**Prerequisites:** Problem 11 and the distinction between sets and sequences.

**Why this step is next:** It retains the same domain and adds ways to construct
related sets instead of asking only about containment.

**Likely variants:** Add symmetric difference; reconcile three snapshots.

**Reuse:** May extend Problem 11's data normalization.

**Source basis:** Levin Section 0.3, Cummings Chapter 3, and Hehner Chapter 2;
original permission-reconciliation adaptation.

### 13 — Policy Boundary Auditor

**Status:** Planned

**Problem idea:** Given an explicit universe of capabilities, compare original
and rewritten allow/deny policies and report any capability classified
differently.

**New concept:** Set complement relative to a declared universe and De Morgan's
laws for sets. These are paired because complement has no unambiguous meaning
without the universe used by the policy rewrite.

**Reinforces:** Union, intersection, difference, equivalence, and
counterexamples.

**Prerequisites:** Problems 06 and 12.

**Why this step is next:** Previous operations combined known sets; this adds
their boundary relative to an explicit surrounding domain.

**Likely variants:** Audit a second De Morgan rewrite; reject sets containing
values outside the declared universe.

**Reuse:** May reuse the equivalence-reporting pattern from Problem 06 and set
normalization from Problem 12.

**Source basis:** Levin Section 0.3 and Cummings Chapters 3 and 5 for
complements and De Morgan's laws; original policy-boundary adaptation.

### 14 — Feature Bundle Enumerator

**Status:** Planned

**Problem idea:** Produce every distinct feature bundle selectable from a small
catalog, including the empty and full bundles.

**New concept:** Power sets.

**Reinforces:** Subsets, set equality, cardinality, exhaustive generation, and
deterministic representation.

**Prerequisites:** Problems 11–13 and the distinction between a set and a set of
sets.

**Why this step is next:** Earlier problems inspected or combined given sets;
this constructs the complete collection of their subsets.

**Likely variants:** Restrict bundle size; filter bundles with a compatibility
predicate without introducing counting formulas.

**Reuse:** Its output may later serve as one dimension of a finite state model.

**Source basis:** Levin Section 0.3 and Cummings Chapter 3 for power sets;
original feature-bundle adaptation.

### 15 — Deployment Matrix Builder

**Status:** Planned

**Problem idea:** Build every deployment state from independent finite domains
such as environments, runtime versions, and regions, preserving attribute
meaning and order.

**New concept:** Cartesian products.

**Reinforces:** Sets, ordered tuples, cardinality, exhaustive generation, and
empty-domain behavior.

**Prerequisites:** Set membership and representing one state as an ordered
tuple.

**Why this step is next:** Problem 14 generated choices from one catalog; this
combines choices from distinct domains into structured states.

**Likely variants:** Support a variable number of dimensions; filter states
with a previously learned predicate.

**Reuse:** Intended for reuse by Problems 16, 26, and 27 when appropriate.

**Source basis:** Levin Section 0.3 and Cummings Chapter 3 for Cartesian
products; original deployment-matrix adaptation.

## Milestone 4 — Functions and mappings

### 16 — State Classifier Contract

**Status:** Planned

**Problem idea:** Audit a finite classifier from declared system states to
declared operational categories and report the categories actually produced.

**New concept:** Domain, codomain, and image as the inseparable contract of a
finite function.

**Reinforces:** Finite state spaces, predicates, sets, and input/output
validation.

**Prerequisites:** Problem 15 and the programming idea of calling a function.

**Why this step is next:** The module has built a state space; this adds one
mapping from those states to another declared set.

**Likely variants:** Audit a partially specified mapping; classify user records
instead of deployment states.

**Reuse:** May consume states from Problem 15.

**Source basis:** Levin Section 0.4, Cummings Chapter 8, and Hehner Chapter 3;
original classifier-contract adaptation.

### 17 — Transformation Pipeline Auditor

**Status:** Planned

**Problem idea:** Check the behavior and compatibility of two finite
transformations connected as a data-processing pipeline, including an identity
stage.

**New concept:** Function composition and identity functions.

**Reinforces:** Domains, codomains, images, and exhaustive finite evaluation.

**Prerequisites:** Problem 16 and reasoning about one function's output as
another function's input.

**Why this step is next:** It keeps the finite-function model and adds one
structural operation between functions.

**Likely variants:** Compare two pipeline orders; report the first state on
which two pipelines disagree.

**Reuse:** Extends the finite function representation from Problem 16.

**Source basis:** Cummings Chapter 8 and Hehner Chapter 3 for composition;
original transformation-pipeline adaptation.

### 18 — Identifier Collision Auditor

**Status:** Planned

**Problem idea:** Inspect a finite identifier migration and report whether two
source identifiers ever collapse onto the same replacement identifier,
including the colliding sources when they do.

**New concept:** Injective functions and information preservation.

**Reinforces:** Domain, codomain, image, equality, and counterexamples.

**Prerequisites:** Problem 16 and a clear distinction between inputs and
outputs.

**Why this step is next:** It asks the first structural-quality question about
a function, isolated from destination coverage.

**Likely variants:** Report every collision group; compare collision behavior
before and after a normalization stage.

**Reuse:** Extends Problem 16's finite mapping validation.

**Source basis:** Levin Section 0.4 and Cummings Chapter 8 for injectivity;
original identifier-migration adaptation.

### 19 — Migration Coverage Auditor

**Status:** Planned

**Problem idea:** Determine whether every declared replacement identifier is
reached by a migration and whether the mapping supports a complete reversible
correspondence.

**New concept:** Surjective functions; bijectivity is recognized by composing
surjectivity with the injectivity learned in Problem 18.

**Reinforces:** Injectivity, codomain versus image, cardinality, and
counterexamples.

**Prerequisites:** Problems 16 and 18.

**Why this step is next:** It adds destination coverage while retrieving the
previously isolated collision property.

**Likely variants:** Report every unused destination; construct a reverse lookup
only when the audited properties justify it.

**Reuse:** Extends Problems 16 and 18.

**Source basis:** Levin Section 0.4 and Cummings Chapter 8 for surjectivity,
bijectivity, and inverses; original migration-coverage adaptation.

## Milestone 5 — Relations

### 20 — Compatibility Relation Registry

**Status:** Planned

**Problem idea:** Represent and query compatibility between two finite catalogs,
such as plugins and runtime versions, where one item may relate to many items.

**New concept:** Binary relations as sets of ordered pairs.

**Reinforces:** Cartesian products, membership, sets, domains, and the
distinction between a relation and a function.

**Prerequisites:** Problems 15 and 16; comfort with ordered pairs.

**Why this step is next:** A function allowed one output per input; this removes
that restriction while retaining a precise finite pair representation.

**Likely variants:** Query in the reverse direction; report pairs missing from
a declared compatibility matrix.

**Reuse:** May reuse Cartesian-product validation from Problem 15.

**Source basis:** Cummings Chapter 9 and Hehner Chapter 3 for pairwise
relations; original plugin-compatibility adaptation.

### 21 — Self-Relation Auditor

**Status:** Planned

**Problem idea:** Inspect a relation over one finite domain and report whether
every item relates to itself, no item relates to itself, or neither condition
holds, with evidence for failures.

**New concept:** Reflexive and irreflexive relations as a deliberate contrast
about self-pairs.

**Reinforces:** Binary relations, universal claims, witnesses, and exhaustive
checking.

**Prerequisites:** Problem 20 and universal quantification.

**Why this step is next:** It asks only about diagonal pairs, the smallest
global property of a relation.

**Likely variants:** Return all missing self-pairs; repair only the reflexive
closure as a later extension.

**Reuse:** Extends Problem 20's finite relation representation.

**Source basis:** Cummings Chapter 9 for reflexive relation checks; original
self-relation audit.

### 22 — Reciprocity and Conflict Auditor

**Status:** Planned

**Problem idea:** Audit whether a relation represents reciprocal compatibility
and whether mutual pairs among distinct items violate an ordering-style
contract.

**New concept:** Symmetry and antisymmetry. They are introduced together to
confront the common but incorrect assumption that they are opposites.

**Reinforces:** Ordered pairs, implication, counterexamples, and the relation
engine from Problem 20.

**Prerequisites:** Problems 20 and 21 and the meaning of pair reversal.

**Why this step is next:** It moves from self-pairs to pairs in opposite
directions while changing no representation.

**Likely variants:** Audit only symmetry and list missing reverse pairs; compare
a relation with its inverse.

**Reuse:** Extends the representation and evidence format from Problems 20–21.

**Source basis:** Cummings Chapter 9 for symmetric and antisymmetric behavior;
original reciprocity-audit adaptation.

### 23 — Chained Rule Auditor

**Status:** Planned

**Problem idea:** Determine whether every two-step chain in a finite relation
has the direct relationship required by the declared policy and report a broken
chain when it does not.

**New concept:** Transitive relations.

**Reinforces:** Binary relations, implication, Cartesian products, witnesses,
and counterexamples.

**Prerequisites:** Problems 20–22.

**Why this step is next:** Earlier properties inspected one pair or its reverse;
this adds exactly one form of composition across two related pairs.

**Likely variants:** Return every broken chain; compute a closure only in a
later extension.

**Reuse:** Extends the relation and evidence engines from Problems 20–22.

**Source basis:** Cummings Chapter 9 for transitivity; original chained-policy
adaptation.

### 24 — Account Alias Classifier

**Status:** Planned

**Problem idea:** Validate whether a declared “same account” relation divides
identifiers into non-overlapping alias groups and expose those groups as a
stable partition.

**New concept:** Equivalence relations and their correspondence with
partitions. The pair is operationally inseparable because the groups are the
observable structure produced by the relation.

**Reinforces:** Reflexivity, symmetry, transitivity, sets, and exhaustive
checking.

**Prerequisites:** Problems 21–23 and set disjointness.

**Why this step is next:** It composes three independently practiced relation
properties into a useful grouping abstraction.

**Likely variants:** Reconstruct the relation from supplied groups; report the
smallest evidence that malformed aliases fail the contract.

**Reuse:** Expected to import the completed property checks.

**Source basis:** Cummings Chapter 9 for equivalence relations, classes, and
partitions; original account-alias adaptation.

### 25 — Dependency Order Validator

**Status:** Planned

**Problem idea:** Validate a declared “must not come later than” relationship
among tasks as a coherent partial ordering, without introducing graph traversal
algorithms.

**New concept:** Partial orders.

**Reinforces:** Reflexivity, antisymmetry, transitivity, and counterexamples.

**Prerequisites:** Problems 21–23 and the distinction between symmetry and
antisymmetry.

**Why this step is next:** It recombines a different set of known relation
properties and contrasts ordering with the grouping structure of Problem 24.

**Likely variants:** Use subset containment as the relation; distinguish total
from partial order in a later extension.

**Reuse:** Expected to import the completed relation-property checks.

**Source basis:** Cummings Chapter 9 for partial orders and subset containment;
original dependency-order adaptation.

## Milestone 6 — Invariants and integrated finite models

### 26 — State Transition Safety Auditor

**Status:** Planned

**Problem idea:** Given a finite state space, a validity predicate, and declared
state transitions, report whether every transition starting from a valid state
preserves the stated safety property, with a violating transition when it does
not.

**New concept:** Invariant preservation across transitions.

**Reinforces:** Predicates, universal claims, Cartesian-product state spaces,
relations, implication, and counterexamples.

**Prerequisites:** Milestones 1–5 and the distinction between valid and merely
representable states.

**Why this step is next:** It isolates invariants in a small transition model
before the module asks for full integration.

**Likely variants:** Separate initial-state validity from transition safety;
audit two invariants independently.

**Reuse:** May consume the state-space and relation representations from
Problems 15 and 20.

**Source basis:** Hehner Chapters 4–5 for specifications and assertions;
Parberry and Gasarch Chapter 5 for correctness reasoning; original transition-
safety adaptation.

### 27 — Possible Worlds Policy Engine

**Status:** Planned

**Problem idea:** Model a small configurable system as a finite space of states,
apply independent rules, classify valid states, represent transitions or other
relationships, and audit guarantees across the complete model.

**New concept:** No new mathematical family. This is an integration and
recognition challenge in which the student must select and compose previously
implemented structures.

**Reinforces:** Every milestone in the module, including implication,
quantifiers, sets, functions, relations, cardinality, invariants, exhaustive
checking, and counterexamples.

**Prerequisites:** Problem 26 and demonstrated understanding of the five earlier
milestones.

**Why this step is next:** Invariants have already been isolated, so the final
problem can measure integration rather than conceal a new concept inside a
large task.

**Likely variants:** Add one state attribute and measure the effect; transfer
the engine to a game, workflow, or access-control domain without naming the
mathematical structures in advance.

**Reuse:** Expected to reuse stable contracts or small engines when that makes
the mathematics clearer. Exact reuse will depend on reviewed student work.

**Source basis:** Hehner Chapters 4–5; Parberry and Gasarch Chapter 5; original
finite-world synthesis of the preceding problems.

## Planned progression summary

| Range | Primary focus | Intended progression |
| --- | --- | --- |
| 01–06 | Boolean rules | Mechanical → interpretation |
| 07–10 | Predicates and quantifiers | Basic application → composition |
| 11–15 | Sets and state spaces | Mechanical → composition |
| 16–19 | Functions and mappings | Basic application → composition |
| 20–25 | Relations | Mechanical → composition |
| 26 | Transition invariants | Basic application → cross-topic |
| 27 | Integrated finite model | Open integration within the module |

Problem 27 is the module's initial integration challenge. Whether it should be
treated as a Boss Challenge, followed by an additional open problem, or both
will be decided from demonstrated mastery rather than scheduled in advance.
