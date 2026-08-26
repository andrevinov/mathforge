# Module 01 Problem Plan — States, Rules, and Possible Worlds

## Plan status

**Module status:** Ready to begin

**Initial challenge count:** 19

This is an adaptive curriculum plan, not a fixed contract. Challenge count,
order, scope, and reuse decisions may change after each student implementation.
A smaller intermediate problem will be inserted whenever the next conceptual
step proves too large. A redundant problem may be skipped when mastery is
already evident.

Only one challenge becomes active at a time. No problem directory is created
until the student explicitly requests the first or next problem.

## Module purpose

Develop the ability to represent finite states, rules, mappings, relationships,
and invariants precisely enough to implement and test them.

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

## Mathematical milestones

1. **Boolean rules:** propositions, truth assignments, and equivalence.
2. **Predicates and quantifiers:** rules over domains, universal claims,
   existential claims, and negation.
3. **Sets and state spaces:** membership, set operations, power sets, and
   Cartesian products.
4. **Functions and mappings:** domain, codomain, image, composition, and mapping
   properties.
5. **Relations:** binary relations, structural properties, equivalence, and
   partial order.
6. **Integrated finite models:** states, rules, mappings, relations, cardinality,
   and invariants working together.

## Evidence required for module mastery

The student must eventually demonstrate the ability to:

- translate plain-language rules into correct predicates;
- test finite Boolean claims exhaustively;
- produce or interpret a counterexample;
- distinguish universal and existential requirements;
- model finite collections and state spaces as sets;
- describe and classify finite functions;
- represent and inspect finite relations;
- state and test invariants;
- integrate these structures without being told which one to use;
- explain correctness, assumptions, and basic enumeration cost.

## Future fields that depend on this module

- discrete mathematics;
- combinatorics;
- probability and sample spaces;
- graph theory;
- state machines and dynamical systems;
- formal specification and verification;
- optimization over finite domains;
- Markov chains and Markov decision processes.

## Milestone 1 — Boolean rules

### 01 — Feature Release Gate

**Status:** Planned

**Problem idea:** Implement the decision rule used by a deployment service to
decide whether a feature may be released from a small collection of Boolean
facts such as approval, test status, maintenance mode, and emergency override.

**New concept:** Compound propositions built from negation, conjunction, and
disjunction. These connectives form one small inseparable group because the
first useful rule needs both combination and exclusion.

**Reinforces:** Python Boolean values, comparisons, conditionals, and total
functions over a tiny finite domain.

**Prerequisites:** Ability to read a verbal rule carefully and evaluate simple
Boolean expressions.

**Why this step is next:** It exposes the smallest useful mathematical object in
the module—a proposition—inside an ordinary programming rule.

**Likely variants:** Add one emergency exception; transfer the same rule shape
to an account-access decision.

**Reuse:** Standalone. A later challenge may reuse its rule as a callable but
will not depend on its internal implementation.

### 02 — Truth Table Reporter

**Status:** Planned

**Problem idea:** Build a diagnostic tool that reports the result of a Boolean
policy for every possible assignment of a small declared set of flags.

**New concept:** Truth tables as exhaustive models of finite Boolean behavior.

**Reinforces:** Compound propositions and finite iteration from Problem 01.

**Prerequisites:** Understanding Boolean variables and being able to evaluate a
rule for one assignment.

**Why this step is next:** Problem 01 evaluates one case; this problem changes
only the scale of observation by covering the entire small domain.

**Likely variants:** Include named intermediate columns; increase from two flags
to three while preserving deterministic row order.

**Reuse:** Standalone implementation, shaped so its completed enumeration engine
may be reused by Problem 03.

### 03 — Policy Equivalence Auditor

**Status:** Planned

**Problem idea:** Compare two Boolean policies over a declared finite domain and
report whether they always agree, including a disagreement case when they do
not.

**New concept:** Logical equivalence.

**Reinforces:** Truth tables, exhaustive finite testing, propositions, and
counterexamples.

**Prerequisites:** Ability to enumerate all truth assignments and evaluate a
rule on each one.

**Why this step is next:** It gives the truth-table machinery from Problem 02 a
single new purpose: comparing meanings rather than merely listing outputs.

**Likely variants:** Detect whether a policy is always true or always false;
audit a simplified production policy against its original form.

**Reuse:** Extends Problem 02 and may import its completed truth-assignment
engine if doing so remains simple.

## Milestone 2 — Predicates and quantified requirements

### 04 — Deployment Record Validator

**Status:** Planned

**Problem idea:** Implement a validator that decides whether one structured
deployment record satisfies a documented collection of eligibility rules.

**New concept:** Predicates interpreted over an explicit domain.

**Reinforces:** Boolean rules and careful translation from prose.

**Prerequisites:** Propositions, functions, tuples or dictionaries, and the
difference between valid input data and a true predicate result.

**Why this step is next:** Earlier rules used only Boolean flags; this problem
adds variables whose values come from a meaningful domain.

**Likely variants:** Validate a user-registration record; return the names of
failed rules without changing eligibility semantics.

**Reuse:** Standalone validator designed to become the predicate used by
Problems 05 and 06.

### 05 — Fleet-Wide Compliance Check

**Status:** Planned

**Problem idea:** Decide whether every deployment record in a fleet satisfies a
provided compliance predicate, including the behavior of an empty fleet.

**New concept:** Universal quantification.

**Reinforces:** Predicates, explicit domains, empty-input behavior, and Boolean
results.

**Prerequisites:** Ability to apply one predicate to one record and understand
what population the claim refers to.

**Why this step is next:** It changes only one dimension of Problem 04: a rule
about one object becomes a claim about every object in a collection.

**Likely variants:** Require compliance only within a selected environment;
report the number of records checked while preserving the same universal claim.

**Reuse:** May import the completed validator from Problem 04.

### 06 — Incident Witness Finder

**Status:** Planned

**Problem idea:** Search a collection of system records for evidence that an
alert condition occurs, returning a concrete witness when one exists.

**New concept:** Existential quantification and witnesses.

**Reinforces:** Predicates, collection domains, and the distinction between a
Boolean claim and supporting evidence.

**Prerequisites:** Universal quantification and applying a predicate across a
collection.

**Why this step is next:** It introduces the other fundamental quantified claim
while retaining the same record-and-predicate model used in Problem 05.

**Likely variants:** Return all witnesses instead of the first; search for a
counterexample to a compliance claim.

**Reuse:** May reuse the validator or predicate contract from Problem 04, but
the existential search is new.

### 07 — Compliance Negation Auditor

**Status:** Planned

**Problem idea:** Audit paired compliance queries that express a requirement and
its negation, checking their agreement across finite collections and reporting a
collection that exposes an incorrect negation.

**New concept:** Negation of quantified statements.

**Reinforces:** Universal and existential quantification, logical equivalence,
and counterexamples.

**Prerequisites:** Problems 03, 05, and 06; familiarity with negating a simple
Boolean statement.

**Why this step is next:** It composes the two quantifiers already implemented
and adds only the rules governing their negation.

**Likely variants:** Audit “none” versus “not some”; transfer the same logic to
permission or inventory records.

**Reuse:** May import the completed universal and existential query engines from
Problems 05 and 06.

## Milestone 3 — Sets and state-space construction

### 08 — Access Scope Containment

**Status:** Planned

**Problem idea:** Determine whether all permissions requested by a service are
contained in the permissions granted to it, and report any requests outside the
granted scope.

**New concept:** Set membership and the subset relationship.

**Reinforces:** Universal claims, predicates, witnesses, and the effect of
duplicates in input data.

**Prerequisites:** Quantified collection rules and basic familiarity with Python
sets.

**Why this step is next:** It reinterprets a familiar compliance question using
a mathematical collection whose equality and containment ignore order.

**Likely variants:** Check strict containment; distinguish required, optional,
and forbidden permissions.

**Reuse:** Standalone set model. Its normalized permission representation may be
reused by Problem 09.

### 09 — Permission Set Reconciler

**Status:** Planned

**Problem idea:** Compare two permission snapshots and report shared,
newly-added, removed, and combined permissions without treating order or
duplicates as meaningful.

**New concept:** The basic family of set operations—union, intersection, and
difference. They are grouped because one reconciliation report defines them
side by side over the same two sets.

**Reinforces:** Membership, subsets, finite cardinality, and precise output
contracts.

**Prerequisites:** Problem 08 and the mathematical distinction between a set and
a sequence.

**Why this step is next:** It retains the same permission domain and adds ways
to construct related sets instead of asking only about containment.

**Likely variants:** Add symmetric difference; reconcile three snapshots while
preserving the meaning of each report field.

**Reuse:** Extends Problem 08's data normalization when that reuse does not hide
the set operations.

### 10 — Feature Bundle Enumerator

**Status:** Planned

**Problem idea:** Produce every distinct feature bundle that can be selected
from a small catalog, including the empty bundle and the full catalog.

**New concept:** Power sets.

**Reinforces:** Subsets, set equality, cardinality, exhaustive generation, and
deterministic representation.

**Prerequisites:** Problems 08 and 09; ability to distinguish a collection of
subsets from one subset.

**Why this step is next:** Earlier problems inspected or combined given sets;
this one constructs the complete set of their possible subsets.

**Likely variants:** Restrict bundle size; attach a Boolean compatibility
predicate without introducing counting formulas.

**Reuse:** Standalone generator. Its output may later serve as one dimension of
a finite state model.

### 11 — Deployment Matrix Builder

**Status:** Planned

**Problem idea:** Build every possible deployment state from independent finite
collections such as environments, runtime versions, and regions, preserving the
meaning and order of each state attribute.

**New concept:** Cartesian products.

**Reinforces:** Sets, ordered tuples, finite cardinality, exhaustive generation,
and empty-domain behavior.

**Prerequisites:** Set membership and confidence representing one state as an
ordered tuple.

**Why this step is next:** Problem 10 generated selections from one catalog;
this problem combines choices from distinct domains into structured states.

**Likely variants:** Support a variable number of dimensions; filter invalid
states with a previously learned predicate.

**Reuse:** Standalone state-space engine intended for reuse in Problems 12 and
19 if its interface remains appropriate.

## Milestone 4 — Functions and mappings

### 12 — State Classifier Contract

**Status:** Planned

**Problem idea:** Audit a finite classifier that maps each declared system state
to one of a declared collection of operational categories, and report which
categories are actually produced.

**New concept:** Domain, codomain, and image of a function.

**Reinforces:** Finite state spaces, predicates, sets, and explicit validation of
inputs and outputs.

**Prerequisites:** Cartesian products, set membership, and the programming idea
of calling a function.

**Why this step is next:** The module has built a state space; this problem adds
one mapping from those states to a second declared set.

**Likely variants:** Audit a partially specified mapping; classify user records
instead of deployment states.

**Reuse:** May consume states produced by Problem 11 without depending on how
that product was implemented.

### 13 — Transformation Pipeline Auditor

**Status:** Planned

**Problem idea:** Check the behavior and compatibility of two finite
transformations connected as a data-processing pipeline, including an identity
stage.

**New concept:** Function composition.

**Reinforces:** Domains, codomains, images, total mappings, and exhaustive finite
evaluation.

**Prerequisites:** Problem 12 and the ability to reason about the output type of
one function as the input type of another.

**Why this step is next:** It keeps the finite-function model from Problem 12
and adds exactly one structural operation between two functions.

**Likely variants:** Compare two pipeline orders; detect the first state for
which two pipelines disagree.

**Reuse:** Extends the finite function-audit representation from Problem 12.

### 14 — Identifier Mapping Integrity Audit

**Status:** Planned

**Problem idea:** Classify a finite mapping between legacy and replacement
identifiers according to whether values collide, destinations remain unused, or
the mapping supports a complete reversible migration.

**New concept:** Injective, surjective, and bijective mappings. These properties
are grouped because the programming task is one integrity classification and
their contrast is the learning objective.

**Reinforces:** Domain, codomain, image, cardinality, and information loss.

**Prerequisites:** Problem 12; a clear distinction between codomain and image.

**Why this step is next:** It adds structural quality questions to a function
whose basic contract the student already knows how to audit.

**Likely variants:** Construct a reverse lookup only when justified; identify
the exact collisions or unused destination identifiers.

**Reuse:** Extends Problem 12's finite mapping model and may reuse its validation
component.

## Milestone 5 — Relations

### 15 — Compatibility Relation Registry

**Status:** Planned

**Problem idea:** Represent and query compatibility between two finite catalogs,
such as plugins and runtime versions, where an item may be compatible with many
items on the other side.

**New concept:** Binary relations as sets of ordered pairs.

**Reinforces:** Cartesian products, membership, sets, domains, and the
distinction between a relation and a function.

**Prerequisites:** Problems 11 and 12; comfort with ordered pairs.

**Why this step is next:** A function allowed one output per input; this problem
removes that restriction while retaining a precise finite pair representation.

**Likely variants:** Query compatibility in the reverse direction; report all
pairs missing from a declared compatibility matrix.

**Reuse:** Standalone relation representation that may reuse Cartesian-product
validation from Problem 11.

### 16 — Relation Property Auditor

**Status:** Planned

**Problem idea:** Inspect a relation over one finite domain and report which
standard behavioral guarantees it satisfies, together with a violating example
for each guarantee it fails.

**New concept:** Reflexive, symmetric, antisymmetric, and transitive properties.
They are introduced as one small classification vocabulary because all are
independent audits over the same finite relation, and the next two problems
depend on contrasting them.

**Reinforces:** Binary relations, universal claims, implication, exhaustive
finite checking, witnesses, and counterexamples.

**Prerequisites:** Problem 15 and the quantified reasoning from Milestone 2.

**Why this step is next:** Problem 15 represented a relation; this problem asks
what global guarantees follow from the pairs it contains.

**Likely variants:** Audit only one selected property and produce every
counterexample; compare a relation with its reversed relation.

**Reuse:** Extends Problem 15's finite relation representation and is intended
for reuse by Problems 17 and 18.

### 17 — Account Alias Classifier

**Status:** Planned

**Problem idea:** Validate whether a declared “same account” relation genuinely
divides account identifiers into non-overlapping alias groups, then expose those
groups as a stable partition.

**New concept:** Equivalence relations and their correspondence with partitions.
They are paired because constructing the classes is the operational evidence
that the relation has the intended meaning.

**Reinforces:** Relation properties, set partitions, exhaustive checking, and
canonical representation.

**Prerequisites:** Problem 16, especially reflexivity, symmetry, and
transitivity; set membership and disjointness.

**Why this step is next:** It combines a specific subset of already implemented
relation properties into one programming abstraction with practical meaning.

**Likely variants:** Reconstruct the relation from supplied groups; identify the
smallest evidence that malformed alias data is not an equivalence relation.

**Reuse:** May import the completed property checks from Problem 16 while adding
class construction as the new work.

### 18 — Dependency Order Validator

**Status:** Planned

**Problem idea:** Validate a declared “must not come later than” relationship
among tasks and determine whether it behaves like a coherent partial ordering,
without introducing graph traversal algorithms.

**New concept:** Partial orders.

**Reinforces:** Reflexivity, antisymmetry, transitivity, ordered pairs, and
counterexamples.

**Prerequisites:** Problem 16 and the ability to distinguish symmetric from
antisymmetric behavior.

**Why this step is next:** It recombines a different subset of known relation
properties, contrasting ordered structure with the grouping structure from
Problem 17.

**Likely variants:** Use subset containment as the relation; distinguish a total
order from a partial order as a later extension.

**Reuse:** May import the property-audit engine from Problem 16. It must not add
graph infrastructure.

## Milestone 6 — Integrated finite models

### 19 — Possible Worlds Policy Engine

**Status:** Planned

**Problem idea:** Model a small configurable system as a finite space of states,
apply several independent rules, classify valid states, represent a relationship
among selected states, and audit properties that must remain true across the
entire model.

**New concept:** Invariants of a finite state model.

**Reinforces:** Propositions, predicates, quantifiers, sets, Cartesian products,
functions, relations, cardinality, exhaustive checking, and counterexamples.

**Prerequisites:** Completion of the five preceding milestones and the ability
to explain why exhaustive enumeration is feasible for a declared small domain.

**Why this step is next:** It adds no new family of data structure. Instead, it
introduces invariants as the organizing concept that makes all previous
structures work together in one deliberately small system.

**Likely variants:** Add one state attribute and measure the effect on the model;
transfer the engine from deployment policy to a game, workflow, or access-control
domain without naming the mathematical structures in advance.

**Reuse:** Expected to reuse stable contracts or small engines from Problems 11,
12, and 16 when doing so clarifies the integration. The exact reuse decision
will be made only after those implementations have been reviewed.

## Planned progression summary

| Range | Primary focus | Intended progression |
| --- | --- | --- |
| 01–03 | Boolean rules | Mechanical → basic application |
| 04–07 | Predicates and quantifiers | Basic application → composition |
| 08–11 | Sets and state spaces | Mechanical → composition |
| 12–14 | Functions and mappings | Basic application → interpretation |
| 15–18 | Relations | Mechanical → composition |
| 19 | Integrated finite model | Cross-topic within the module |

Problem 19 is the module's initial integration challenge. Whether an additional
open problem or Boss Challenge is needed will be decided from demonstrated
mastery rather than scheduled in advance.
