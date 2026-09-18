from __future__ import annotations

import importlib.util
from collections.abc import Callable
from itertools import product
from pathlib import Path
from types import ModuleType

SOLUTION_PATH = Path(__file__).resolve().parents[1] / "solution.py"

Policy = Callable[[dict[str, bool]], bool]
AuditResult = tuple[bool, tuple[bool, ...] | None]


def load_solution() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "policy_implication_auditor_solution",
        SOLUTION_PATH,
    )
    assert spec is not None, f"Could not create an import spec for {SOLUTION_PATH}"
    assert spec.loader is not None, f"Could not load {SOLUTION_PATH}"

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_audit_policy_implication() -> Callable[
    [tuple[str, ...], Policy, Policy],
    AuditResult,
]:
    module = load_solution()
    function = getattr(module, "audit_policy_implication", None)
    assert callable(function), (
        "solution.py must define a callable named audit_policy_implication "
        "with the interface specified in README.md"
    )
    return function


def expected_assignments(flag_count: int) -> list[tuple[bool, ...]]:
    return list(product((False, True), repeat=flag_count))


def make_policy(
    flag_names: tuple[str, ...],
    truth_values: tuple[bool, ...],
) -> Policy:
    assignments = expected_assignments(len(flag_names))
    lookup = dict(zip(assignments, truth_values))

    def policy(state: dict[str, bool]) -> bool:
        assignment = tuple(state[name] for name in flag_names)
        return lookup[assignment]

    return policy


def test_required_interface_exists() -> None:
    get_audit_policy_implication()


def test_readme_implication_that_holds() -> None:
    audit_policy_implication = get_audit_policy_implication()

    def approved_and_tested(state: dict[str, bool]) -> bool:
        return state["approved"] and state["tested"]

    def tested(state: dict[str, bool]) -> bool:
        return state["tested"]

    assert audit_policy_implication(
        ("approved", "tested"),
        approved_and_tested,
        tested,
    ) == (True, None)


def test_readme_implication_that_fails() -> None:
    audit_policy_implication = get_audit_policy_implication()

    assert audit_policy_implication(
        ("approved", "tested"),
        lambda state: state["approved"],
        lambda state: state["tested"],
    ) == (False, (True, False))


def test_a_never_satisfied_premise_does_not_produce_a_counterexample() -> None:
    audit_policy_implication = get_audit_policy_implication()

    assert audit_policy_implication(
        ("enabled", "override"),
        lambda state: False,
        lambda state: False,
    ) == (True, None)


def test_an_always_satisfied_conclusion_makes_the_implication_hold() -> None:
    audit_policy_implication = get_audit_policy_implication()

    assert audit_policy_implication(
        ("enabled", "override"),
        lambda state: state["enabled"] != state["override"],
        lambda state: True,
    ) == (True, None)


def test_implication_is_directional() -> None:
    audit_policy_implication = get_audit_policy_implication()
    flag_names = ("approved", "tested")

    approved_and_tested = lambda state: state["approved"] and state["tested"]
    approved = lambda state: state["approved"]

    assert audit_policy_implication(
        flag_names,
        approved_and_tested,
        approved,
    ) == (True, None)
    assert audit_policy_implication(
        flag_names,
        approved,
        approved_and_tested,
    ) == (False, (True, False))


def test_first_counterexample_uses_required_assignment_order() -> None:
    audit_policy_implication = get_audit_policy_implication()

    assert audit_policy_implication(
        ("alpha", "beta", "gamma"),
        lambda state: state["alpha"] or state["beta"],
        lambda state: state["gamma"],
    ) == (False, (False, True, False))


def test_policy_state_uses_names_aligned_with_assignment_positions() -> None:
    audit_policy_implication = get_audit_policy_implication()
    flag_names = ("False", "True", "override")

    def premise_policy(state: dict[str, bool]) -> bool:
        assert type(state) is dict
        assert set(state) == set(flag_names)
        assert all(type(value) is bool for value in state.values())
        return state["False"] and not state["True"]

    def conclusion_policy(state: dict[str, bool]) -> bool:
        assert type(state) is dict
        assert set(state) == set(flag_names)
        assert all(type(value) is bool for value in state.values())
        return state["override"]

    assert audit_policy_implication(
        flag_names,
        premise_policy,
        conclusion_policy,
    ) == (False, (True, False, False))


def test_six_flags_are_exhaustively_audited_when_implication_holds() -> None:
    audit_policy_implication = get_audit_policy_implication()
    flag_names = tuple(f"flag_{index}" for index in range(6))
    observed_assignments: set[tuple[bool, ...]] = set()

    def conclusion_policy(state: dict[str, bool]) -> bool:
        observed_assignments.add(tuple(state[name] for name in flag_names))
        return True

    assert audit_policy_implication(
        flag_names,
        lambda state: True,
        conclusion_policy,
    ) == (True, None)
    assert observed_assignments == set(expected_assignments(6))


def test_all_one_and_two_flag_policy_pairs_match_the_definition() -> None:
    audit_policy_implication = get_audit_policy_implication()

    for flag_count in (1, 2):
        flag_names = tuple(f"flag_{index}" for index in range(flag_count))
        assignments = expected_assignments(flag_count)
        truth_tables = list(product((False, True), repeat=len(assignments)))

        for premise_values in truth_tables:
            premise_policy = make_policy(flag_names, premise_values)

            for conclusion_values in truth_tables:
                conclusion_policy = make_policy(flag_names, conclusion_values)
                counterexample = next(
                    (
                        assignment
                        for assignment, premise_value, conclusion_value in zip(
                            assignments,
                            premise_values,
                            conclusion_values,
                        )
                        if premise_value and not conclusion_value
                    ),
                    None,
                )
                expected = (counterexample is None, counterexample)

                assert audit_policy_implication(
                    flag_names,
                    premise_policy,
                    conclusion_policy,
                ) == expected


def test_result_uses_the_required_exact_types() -> None:
    audit_policy_implication = get_audit_policy_implication()

    successful_result = audit_policy_implication(
        ("enabled",),
        lambda state: state["enabled"],
        lambda state: state["enabled"],
    )
    failing_result = audit_policy_implication(
        ("enabled",),
        lambda state: state["enabled"],
        lambda state: not state["enabled"],
    )

    for result in (successful_result, failing_result):
        assert type(result) is tuple
        assert len(result) == 2
        holds, counterexample = result
        assert type(holds) is bool

        if counterexample is not None:
            assert type(counterexample) is tuple
            assert all(type(value) is bool for value in counterexample)

    assert successful_result == (True, None)
    assert failing_result == (False, (True,))
