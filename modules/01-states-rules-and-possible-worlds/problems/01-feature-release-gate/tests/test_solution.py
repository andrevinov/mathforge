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
        "feature_release_gate_solution",
        SOLUTION_PATH,
    )
    assert spec is not None, f"Could not create an import spec for {SOLUTION_PATH}"
    assert spec.loader is not None, f"Could not load {SOLUTION_PATH}"

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_can_release() -> Callable[[bool, bool, bool, bool], bool]:
    module = load_solution()
    function = getattr(module, "can_release", None)
    assert callable(function), (
        "solution.py must define a callable named can_release with the interface "
        "specified in README.md"
    )
    return function


ALL_BOOLEAN_STATES = tuple(product((False, True), repeat=4))

EXPECTED_DECISIONS = {
    (False, False, False, False): False,
    (False, False, False, True): False,
    (False, False, True, False): False,
    (False, False, True, True): False,
    (False, True, False, False): False,
    (False, True, False, True): True,
    (False, True, True, False): False,
    (False, True, True, True): False,
    (True, False, False, False): False,
    (True, False, False, True): False,
    (True, False, True, False): False,
    (True, False, True, True): False,
    (True, True, False, False): True,
    (True, True, False, True): True,
    (True, True, True, False): False,
    (True, True, True, True): False,
}


def test_required_interface_exists() -> None:
    get_can_release()


@pytest.mark.parametrize(
    ("approved", "tests_passed", "maintenance_mode", "emergency_override"),
    ALL_BOOLEAN_STATES,
)
def test_every_boolean_state_has_the_expected_decision(
    approved: bool,
    tests_passed: bool,
    maintenance_mode: bool,
    emergency_override: bool,
) -> None:
    can_release = get_can_release()
    state = (approved, tests_passed, maintenance_mode, emergency_override)

    assert can_release(*state) is EXPECTED_DECISIONS[state]


@pytest.mark.parametrize("state", ALL_BOOLEAN_STATES)
def test_every_result_has_exact_bool_type(state: tuple[bool, bool, bool, bool]) -> None:
    can_release = get_can_release()

    assert type(can_release(*state)) is bool


@pytest.mark.parametrize(
    ("approved", "emergency_override"),
    ((True, False), (False, True), (True, True)),
)
def test_either_or_both_authorizations_are_accepted_when_other_requirements_hold(
    approved: bool,
    emergency_override: bool,
) -> None:
    can_release = get_can_release()

    assert can_release(approved, True, False, emergency_override) is True


@pytest.mark.parametrize(
    ("approved", "maintenance_mode", "emergency_override"),
    tuple(product((False, True), repeat=3)),
)
def test_failed_tests_always_block_release(
    approved: bool,
    maintenance_mode: bool,
    emergency_override: bool,
) -> None:
    can_release = get_can_release()

    assert can_release(approved, False, maintenance_mode, emergency_override) is False


@pytest.mark.parametrize(
    ("approved", "tests_passed", "emergency_override"),
    tuple(product((False, True), repeat=3)),
)
def test_maintenance_mode_always_blocks_release(
    approved: bool,
    tests_passed: bool,
    emergency_override: bool,
) -> None:
    can_release = get_can_release()

    assert can_release(approved, tests_passed, True, emergency_override) is False
