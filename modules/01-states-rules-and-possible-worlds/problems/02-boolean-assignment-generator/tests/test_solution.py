from __future__ import annotations

import importlib.util
from collections.abc import Callable
from itertools import product
from pathlib import Path
from types import ModuleType

import pytest

SOLUTION_PATH = Path(__file__).resolve().parents[1] / "solution.py"


def load_solution() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "boolean_assignment_generator_solution",
        SOLUTION_PATH,
    )
    assert spec is not None, f"Could not create an import spec for {SOLUTION_PATH}"
    assert spec.loader is not None, f"Could not load {SOLUTION_PATH}"

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_generate_boolean_assignments() -> Callable[[int], list[tuple[bool, ...]]]:
    module = load_solution()
    function = getattr(module, "generate_boolean_assignments", None)
    assert callable(function), (
        "solution.py must define a callable named generate_boolean_assignments "
        "with the interface specified in README.md"
    )
    return function


def expected_assignments(position_count: int) -> list[tuple[bool, ...]]:
    return list(product((False, True), repeat=position_count))


def test_required_interface_exists() -> None:
    get_generate_boolean_assignments()


def test_readme_single_position_example() -> None:
    generate_boolean_assignments = get_generate_boolean_assignments()

    assert generate_boolean_assignments(1) == [
        (False,),
        (True,),
    ]


def test_readme_two_position_example() -> None:
    generate_boolean_assignments = get_generate_boolean_assignments()

    assert generate_boolean_assignments(2) == [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ]


@pytest.mark.parametrize("position_count", range(1, 7))
def test_every_assignment_appears_once_in_required_order(
    position_count: int,
) -> None:
    generate_boolean_assignments = get_generate_boolean_assignments()

    assignments = generate_boolean_assignments(position_count)

    assert assignments == expected_assignments(position_count)
    assert len(assignments) == len(set(assignments))


@pytest.mark.parametrize("position_count", range(1, 7))
def test_output_size_doubles_for_each_added_position(position_count: int) -> None:
    generate_boolean_assignments = get_generate_boolean_assignments()

    assignments = generate_boolean_assignments(position_count)

    assert len(assignments) == 2**position_count


@pytest.mark.parametrize("position_count", range(1, 7))
def test_assignments_have_the_required_exact_types_and_lengths(
    position_count: int,
) -> None:
    generate_boolean_assignments = get_generate_boolean_assignments()

    assignments = generate_boolean_assignments(position_count)

    assert type(assignments) is list
    for assignment in assignments:
        assert type(assignment) is tuple
        assert len(assignment) == position_count
        assert all(type(value) is bool for value in assignment)
