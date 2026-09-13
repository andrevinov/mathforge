# Policy Assignment Evaluator

## Context

A policy engine describes one system state in two parallel pieces: an ordered
tuple of flag names and an ordered tuple of Boolean values. Before building a
complete report, the engine needs to evaluate one such assignment correctly.

## Problem

Implement a function that evaluates a supplied Boolean policy for one supplied
assignment.

The position of each value in `assignment` determines which name in
`flag_names` it belongs to. Call `policy` with a dictionary containing exactly
those name-to-value correspondences, then return the policy's Boolean result.

For example, given:

```python
flag_names = ("approved", "maintenance_mode")
assignment = (True, False)
```

the policy must receive:

```python
{"approved": True, "maintenance_mode": False}
```

## Mathematical Goal

Interpret a truth assignment by associating each named proposition with its
Boolean value, then evaluate a proposition under that assignment.

## Constraints

- Use only the Python standard library.
- `flag_names` will contain between one and six distinct, nonempty strings.
- `assignment` will have the same length as `flag_names` and will contain only
  values whose exact type is `bool`.
- `policy` will be a deterministic callable that accepts a `dict[str, bool]`
  containing exactly the declared flag names and returns a value whose exact
  type is `bool`.
- Do not perform input/output or mutate external state.

## Interface

Implement this function in `solution.py`:

```python
from collections.abc import Callable


def evaluate_policy_assignment(
    flag_names: tuple[str, ...],
    assignment: tuple[bool, ...],
    policy: Callable[[dict[str, bool]], bool],
) -> bool:
    ...
```

## Examples

```python
def may_deploy(state: dict[str, bool]) -> bool:
    return state["approved"] and not state["maintenance_mode"]


evaluate_policy_assignment(
    ("approved", "maintenance_mode"),
    (True, False),
    may_deploy,
)
```

returns `True`.

The same policy evaluated with `(False, False)` returns `False`.

For a single flag:

```python
evaluate_policy_assignment(
    ("enabled",),
    (False,),
    lambda state: not state["enabled"],
)
```

returns `True`.

## Completion Criteria

The challenge is complete when:

- `evaluate_policy_assignment` exists with the specified interface;
- names and values remain correctly aligned for every position;
- the policy receives a plain dictionary with exactly the declared names;
- the returned value is exactly the result of the supplied policy and has
  exact type `bool`;
- all tests pass;
- you can explain what mathematical assignment the dictionary represents and
  why changing the order of values can change the result.
