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
        "truth_table_reporter_solution",
        SOLUTION_PATH,
    )
    assert spec is not None, f"Could not create an import spec for {SOLUTION_PATH}"
    assert spec.loader is not None, f"Could not load {SOLUTION_PATH}"

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_build_truth_table() -> Callable[
    [tuple[str, ...], Callable[[dict[str, bool]], bool]],
    list[tuple[tuple[bool, ...], bool]],
]:
    module = load_solution()
    function = getattr(module, "build_truth_table", None)
    assert callable(function), (
        "solution.py must define a callable named build_truth_table with the "
        "interface specified in README.md"
    )
    return function


def expected_assignments(flag_count: int) -> list[tuple[bool, ...]]:
    return list(product((False, True), repeat=flag_count))


def test_required_interface_exists() -> None:
    get_build_truth_table()


def test_readme_two_flag_example() -> None:
    build_truth_table = get_build_truth_table()

    def both_enabled(state: dict[str, bool]) -> bool:
        return state["search_enabled"] and state["billing_enabled"]

    assert build_truth_table(
        ("search_enabled", "billing_enabled"),
        both_enabled,
    ) == [
        ((False, False), False),
        ((False, True), False),
        ((True, False), False),
        ((True, True), True),
    ]


def test_readme_single_flag_example() -> None:
    build_truth_table = get_build_truth_table()

    assert build_truth_table(
        ("enabled",),
        lambda state: not state["enabled"],
    ) == [
        ((False,), True),
        ((True,), False),
    ]


@pytest.mark.parametrize("flag_count", range(1, 7))
def test_every_assignment_appears_once_in_required_order(flag_count: int) -> None:
    build_truth_table = get_build_truth_table()
    flag_names = tuple(f"flag_{index}" for index in range(flag_count))

    table = build_truth_table(flag_names, lambda state: True)
    assignments = [assignment for assignment, _ in table]

    assert assignments == expected_assignments(flag_count)
    assert len(assignments) == len(set(assignments))


def test_policy_receives_names_aligned_with_assignment_positions() -> None:
    build_truth_table = get_build_truth_table()
    flag_names = ("approved", "tests_passed", "maintenance_mode")

    def policy(state: dict[str, bool]) -> bool:
        assert type(state) is dict
        assert set(state) == set(flag_names)
        return (
            state["approved"]
            and state["tests_passed"]
            and not state["maintenance_mode"]
        )

    table = build_truth_table(flag_names, policy)

    assert table == [
        (assignment, assignment[0] and assignment[1] and not assignment[2])
        for assignment in expected_assignments(3)
    ]


def test_policy_is_evaluated_for_every_possible_state() -> None:
    build_truth_table = get_build_truth_table()
    flag_names = ("alpha", "beta", "gamma", "delta")
    observed_states: set[tuple[bool, ...]] = set()

    def recording_policy(state: dict[str, bool]) -> bool:
        assignment = tuple(state[name] for name in flag_names)
        observed_states.add(assignment)
        return state["alpha"] != state["delta"]

    build_truth_table(flag_names, recording_policy)

    assert observed_states == set(expected_assignments(4))


def test_results_follow_the_supplied_policy_not_a_fixed_rule() -> None:
    build_truth_table = get_build_truth_table()
    flag_names = ("first", "second", "third")

    any_enabled = build_truth_table(flag_names, lambda state: any(state.values()))
    all_enabled = build_truth_table(flag_names, lambda state: all(state.values()))

    assert [result for _, result in any_enabled] == [
        any(assignment) for assignment in expected_assignments(3)
    ]
    assert [result for _, result in all_enabled] == [
        all(assignment) for assignment in expected_assignments(3)
    ]


def test_each_row_uses_the_required_exact_types() -> None:
    build_truth_table = get_build_truth_table()

    table = build_truth_table(
        ("left", "right", "override"),
        lambda state: state["left"] or state["right"] or state["override"],
    )

    assert type(table) is list
    for row in table:
        assert type(row) is tuple
        assert len(row) == 2

        assignment, result = row
        assert type(assignment) is tuple
        assert all(type(value) is bool for value in assignment)
        assert type(result) is bool


def test_flag_names_are_not_used_as_assignment_values() -> None:
    build_truth_table = get_build_truth_table()
    flag_names = ("False", "True")

    table = build_truth_table(
        flag_names,
        lambda state: state["False"] == state["True"],
    )

    assert table == [
        ((False, False), True),
        ((False, True), False),
        ((True, False), False),
        ((True, True), True),
    ]
