# Feature Release Gate

## Context

A deployment service must decide whether a feature can be released. Its
decision depends on four Boolean facts supplied by other parts of the system.

## Problem

Implement the release decision as one deterministic Boolean rule.

A release is allowed only when all of these requirements are satisfied:

- the automated tests passed;
- maintenance mode is off;
- the release has product approval, an emergency override, or both.

An emergency override replaces the need for product approval only. It does not
bypass failed tests or maintenance mode.

## Mathematical Goal

Model a compound proposition using negation, conjunction, and inclusive
disjunction.

## Constraints

- Use only the Python standard library.
- Do not import a library that evaluates or simplifies Boolean expressions.
- The four inputs will always be values of type `bool`; behavior for other
  input types is outside this challenge's contract.
- Return a value whose exact type is `bool`.
- Do not mutate external state or perform input/output.

## Interface

Implement this function in `solution.py`:

```python
def can_release(
    approved: bool,
    tests_passed: bool,
    maintenance_mode: bool,
    emergency_override: bool,
) -> bool:
    ...
```

Parameter meanings:

- `approved`: product approval has been granted.
- `tests_passed`: the automated test suite passed.
- `maintenance_mode`: deployments are temporarily suspended.
- `emergency_override`: emergency authorization has been granted.

## Examples

```python
can_release(True, True, False, False) is True
can_release(False, True, False, True) is True
can_release(True, True, True, True) is False
can_release(True, False, False, True) is False
```

## Completion Criteria

The challenge is complete when:

- `can_release` exists with the specified interface;
- it returns the correct decision for every possible combination of the four
  Boolean inputs;
- every returned value has exact type `bool`;
- all tests pass;
- you can explain which simple propositions make up the policy and how the
  connectives combine them.
