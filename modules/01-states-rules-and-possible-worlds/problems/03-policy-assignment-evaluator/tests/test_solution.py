from __future__ import annotations

import importlib.util
from collections.abc import Callable
from itertools import product
from pathlib import Path
from types import ModuleType

import pytest

SOLUTION_PATH = Path(__file__).resolve().parents[1] / "solution.py"

Policy = Callable[[dict[str, bool]], bool]
Evaluator = Callable[[tuple[str, ...], tuple[bool, ...], Policy], bool]


def load_solution() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "policy_assignment_evaluator_solution",
        SOLUTION_PATH,
    )
    assert spec is not None, f"Could not create an import spec for {SOLUTION_PATH}"
    assert spec.loader is not None, f"Could not load {SOLUTION_PATH}"

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_evaluate_policy_assignment() -> Evaluator:
    module = load_solution()
    function = getattr(module, "evaluate_policy_assignment", None)
    assert callable(function), (
        "solution.py must define a callable named evaluate_policy_assignment "
        "with the interface specified in README.md"
    )
    return function


def test_required_interface_exists() -> None:
    get_evaluate_policy_assignment()


def test_readme_deployment_example() -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()

    def may_deploy(state: dict[str, bool]) -> bool:
        return state["approved"] and not state["maintenance_mode"]

    assert (
        evaluate_policy_assignment(
            ("approved", "maintenance_mode"),
            (True, False),
            may_deploy,
        )
        is True
    )
    assert (
        evaluate_policy_assignment(
            ("approved", "maintenance_mode"),
            (False, False),
            may_deploy,
        )
        is False
    )


def test_readme_single_flag_example() -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()

    assert (
        evaluate_policy_assignment(
            ("enabled",),
            (False,),
            lambda state: not state["enabled"],
        )
        is True
    )


def test_policy_receives_names_aligned_with_assignment_positions() -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()
    flag_names = ("first", "second", "third", "fourth")
    assignment = (True, False, False, True)

    def inspect_state(state: dict[str, bool]) -> bool:
        assert type(state) is dict
        assert state == {
            "first": True,
            "second": False,
            "third": False,
            "fourth": True,
        }
        return state["first"] and state["fourth"]

    assert evaluate_policy_assignment(flag_names, assignment, inspect_state) is True


def test_policy_receives_exactly_the_declared_names() -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()
    flag_names = ("False", "True", "feature-enabled")

    def inspect_names(state: dict[str, bool]) -> bool:
        assert set(state) == set(flag_names)
        return state["False"] != state["True"] or state["feature-enabled"]

    assert (
        evaluate_policy_assignment(
            flag_names,
            (False, True, False),
            inspect_names,
        )
        is True
    )


@pytest.mark.parametrize("flag_count", range(1, 7))
def test_alignment_works_for_every_supported_assignment_length(
    flag_count: int,
) -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()
    flag_names = tuple(f"flag_{index}" for index in range(flag_count))
    assignment = tuple(index % 2 == 0 for index in range(flag_count))
    expected_state = dict(zip(flag_names, assignment, strict=True))

    def inspect_state(state: dict[str, bool]) -> bool:
        assert state == expected_state
        return True

    assert evaluate_policy_assignment(flag_names, assignment, inspect_state) is True


@pytest.mark.parametrize("assignment", tuple(product((False, True), repeat=3)))
def test_result_follows_the_supplied_policy(
    assignment: tuple[bool, bool, bool],
) -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()
    flag_names = ("left", "middle", "right")

    result = evaluate_policy_assignment(
        flag_names,
        assignment,
        lambda state: state["left"] == (state["middle"] or state["right"]),
    )

    assert result is (assignment[0] == (assignment[1] or assignment[2]))


def test_different_policies_can_interpret_the_same_assignment() -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()
    flag_names = ("alpha", "beta", "gamma")
    assignment = (False, True, False)

    any_enabled = evaluate_policy_assignment(
        flag_names,
        assignment,
        lambda state: any(state.values()),
    )
    all_enabled = evaluate_policy_assignment(
        flag_names,
        assignment,
        lambda state: all(state.values()),
    )

    assert any_enabled is True
    assert all_enabled is False


@pytest.mark.parametrize(
    ("flag_names", "assignment"),
    (
        (("only",), (True,)),
        (("left", "right"), (False, True)),
        (("a", "b", "c", "d"), (True, False, True, False)),
    ),
)
def test_result_has_exact_bool_type(
    flag_names: tuple[str, ...],
    assignment: tuple[bool, ...],
) -> None:
    evaluate_policy_assignment = get_evaluate_policy_assignment()

    result = evaluate_policy_assignment(
        flag_names,
        assignment,
        lambda state: any(state.values()),
    )

    assert type(result) is bool
