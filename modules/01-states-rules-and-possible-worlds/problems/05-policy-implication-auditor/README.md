# Policy Implication Auditor

## Context

A configuration service has two Boolean policies. Its maintainers claim that
whenever the first policy accepts a state, the second policy must also accept
that state. Before relying on this guarantee, they need to audit it over every
possible state of the declared feature flags.

## Problem

Implement a function that determines whether `premise_policy` implies
`conclusion_policy` over the complete Boolean state space described by
`flag_names`.

The implication holds when every state accepted by `premise_policy` is also
accepted by `conclusion_policy`.

Return a pair containing:

- whether the implication holds;
- `None` when it holds, or a counterexample assignment when it does not.

A counterexample is an assignment accepted by `premise_policy` and rejected by
`conclusion_policy`. If more than one counterexample exists, return the first
one in lexicographic order with `False` before `True`. The last flag changes
value most frequently, as in the previous truth-table challenge.

For each assignment that is evaluated, call the policies with a dictionary
mapping every flag name to the Boolean value at the corresponding position.

## Mathematical Goal

Understand logical implication as a directional relationship between two
Boolean policies, and understand a counterexample as evidence that a universal
claim is false.

## Prerequisites

Before attempting this challenge, complete Problem 04 and review:

- exhaustive enumeration of a finite Boolean state space;
- positional alignment between flag names and assignments;
- the distinction between a policy and the Boolean value it returns for one
  state.

## Constraints

- Use only the Python standard library.
- Do not use `itertools.product` or another ready-made Cartesian-product or
  truth-table generator.
- `flag_names` will contain between one and six distinct, nonempty strings.
- Both policies will be deterministic callables that accept a
  `dict[str, bool]` containing exactly the declared flag names and return a
  value whose exact type is `bool`.
- Do not perform input/output or mutate caller-owned inputs.
- The challenge is standalone. You may adapt the state-generation mechanism
  you implemented in Problem 04, but no cross-directory import is required.

## Interface

Implement this function in `solution.py`:

```python
from collections.abc import Callable


def audit_policy_implication(
    flag_names: tuple[str, ...],
    premise_policy: Callable[[dict[str, bool]], bool],
    conclusion_policy: Callable[[dict[str, bool]], bool],
) -> tuple[bool, tuple[bool, ...] | None]:
    ...
```

The returned pair is:

- `(True, None)` when the implication holds for the complete state space;
- `(False, assignment)` when it fails, where `assignment` is the first
  counterexample in the required order.

## Examples

The policy "approved and tested" implies the policy "tested":

```python
def approved_and_tested(state: dict[str, bool]) -> bool:
    return state["approved"] and state["tested"]


def tested(state: dict[str, bool]) -> bool:
    return state["tested"]


audit_policy_implication(
    ("approved", "tested"),
    approved_and_tested,
    tested,
)
```

returns:

```python
(True, None)
```

The policy "approved" does not imply the policy "tested":

```python
audit_policy_implication(
    ("approved", "tested"),
    lambda state: state["approved"],
    lambda state: state["tested"],
)
```

returns:

```python
(False, (True, False))
```

## Completion Criteria

The challenge is complete when:

- `audit_policy_implication` has the specified interface;
- it returns the correct result for every relationship between the two
  policies, including cases where the premise is never satisfied;
- any returned counterexample is valid and is the first one in the required
  order;
- flag names and assignment positions remain correctly aligned;
- returned containers and Boolean values use the exact specified types;
- all tests pass;
- you can explain why only one kind of policy-result pair disproves an
  implication, why a successful finite audit is exhaustive evidence, which
  policy is the sufficient condition, which is the necessary condition, and
  the worst-case growth of the audit as flags are added.
