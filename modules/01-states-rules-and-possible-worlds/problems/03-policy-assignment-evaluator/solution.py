from collections.abc import Callable


def evaluate_policy_assignment(
    flag_names: tuple[str, ...],
    assignment: tuple[bool, ...],
    policy: Callable[[dict[str, bool]], bool],
) -> bool:
    mapping = {k: v for k, v in zip(flag_names, assignment)}

    return policy(mapping)
