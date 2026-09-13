# Truth Table Reporter

## Context

A policy-debugging tool needs to show how a Boolean policy behaves in every
possible state of a small collection of feature flags. The tool receives the
flag names and the policy separately so that the same reporting engine can be
used for many policies.

## Problem

Implement a function that builds a complete truth table for a deterministic
Boolean policy.

Each returned row must contain:

- one assignment of Boolean values, represented as a tuple whose positions
  correspond to `flag_names`;
- the result of evaluating the policy for that assignment.

Every possible assignment must appear exactly once.

Rows must use deterministic lexicographic order with `False` before `True`.
The last flag changes value most frequently. For example, the assignments for
`("a", "b")` must appear in this order:

```python
(False, False)
(False, True)
(True, False)
(True, True)
```

To evaluate a row, call `policy` with a dictionary that maps each flag name to
the Boolean value in the corresponding position of the assignment tuple.

## Mathematical Goal

Model a truth table as an exhaustive enumeration of a finite Boolean state
space.

## Prerequisites

Before attempting this challenge, complete:

- Problem 02, which isolates generation of the ordered Boolean assignments;
- Problem 03, which isolates interpretation and policy evaluation for one
  assignment.

This challenge asks you to compose those two previously practiced capabilities.

## Constraints

- Use only the Python standard library.
- Do not use `itertools.product` or another ready-made Cartesian-product or
  truth-table generator. Generating the complete state space is the
  mathematical mechanism being practiced.
- `flag_names` will be a tuple containing between one and six distinct,
  nonempty strings.
- `policy` will be a deterministic callable that accepts a `dict[str, bool]`
  containing exactly those flag names and returns a value whose exact type is
  `bool`.
- Do not perform input/output or mutate external state.

## Interface

Implement this function in `solution.py`:

```python
from collections.abc import Callable


def build_truth_table(
    flag_names: tuple[str, ...],
    policy: Callable[[dict[str, bool]], bool],
) -> list[tuple[tuple[bool, ...], bool]]:
    ...
```

The returned list contains pairs of `(assignment, result)`:

- `assignment` is a tuple of Boolean values aligned positionally with
  `flag_names`;
- `result` is the Boolean returned by `policy` for that assignment.

## Examples

```python
def both_enabled(state: dict[str, bool]) -> bool:
    return state["search_enabled"] and state["billing_enabled"]


build_truth_table(
    ("search_enabled", "billing_enabled"),
    both_enabled,
)
```

returns:

```python
[
    ((False, False), False),
    ((False, True), False),
    ((True, False), False),
    ((True, True), True),
]
```

For a single flag:

```python
build_truth_table(("enabled",), lambda state: not state["enabled"])
```

returns:

```python
[
    ((False,), True),
    ((True,), False),
]
```

## Completion Criteria

The challenge is complete when:

- `build_truth_table` exists with the specified interface;
- every possible assignment appears exactly once and in the required order;
- every assignment is aligned correctly with its flag names when the policy is
  evaluated;
- every assignment value and policy result has exact type `bool`;
- all tests pass;
- you can explain why the table is complete, why it contains no duplicate
  assignments, and how its size and runtime grow when another flag is added.
