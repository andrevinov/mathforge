# Boolean Assignment Generator

## Context

A configuration explorer needs the complete list of possible on/off states for
a small number of feature flags. At this stage it does not know the flags'
names and does not evaluate any policy. It only builds the Boolean assignments
that a later tool will inspect.

## Problem

Implement a function that returns every possible Boolean assignment of a given
length.

Represent one assignment as a tuple of Boolean values. Every assignment must
appear exactly once.

Return the assignments in deterministic lexicographic order with `False`
before `True`. The last position changes value most frequently. For two
positions, the required order is:

```python
(False, False)
(False, True)
(True, False)
(True, True)
```

## Mathematical Goal

Construct the complete finite state space formed by a fixed number of Boolean
choices.

## Constraints

- Use only the Python standard library.
- Do not use `itertools.product` or another ready-made Cartesian-product or
  Boolean-assignment generator. Producing the assignments is the mathematical
  mechanism being practiced.
- `position_count` will be an integer from 1 through 6.
- Do not perform input/output or mutate external state.

## Interface

Implement this function in `solution.py`:

```python
def generate_boolean_assignments(
    position_count: int,
) -> list[tuple[bool, ...]]:
    ...
```

Each returned tuple must contain exactly `position_count` values, and every
value must have exact type `bool`.

## Examples

```python
generate_boolean_assignments(1)
```

returns:

```python
[
    (False,),
    (True,),
]
```

For two positions:

```python
generate_boolean_assignments(2)
```

returns:

```python
[
    (False, False),
    (False, True),
    (True, False),
    (True, True),
]
```

## Completion Criteria

The challenge is complete when:

- `generate_boolean_assignments` exists with the specified interface;
- every possible assignment appears exactly once and in the required order;
- every assignment has the requested length and exact Boolean value types;
- all tests pass;
- you can explain why the output is complete, why it has no duplicates, and
  what happens to its size when one more position is added.
