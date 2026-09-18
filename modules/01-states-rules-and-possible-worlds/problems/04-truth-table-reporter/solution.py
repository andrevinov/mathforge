from collections.abc import Callable


def build_truth_table(
    flag_names: tuple[str, ...],
    policy: Callable[[dict[str, bool]], bool],
) -> list[tuple[tuple[bool, ...], bool]]:
    table: list[tuple[bool, ...]] = [()]

    for _ in range(len(flag_names)):
        extended: list[tuple[bool, ...]] = []

        for line in table:
            extended.append(line + (False,))
            extended.append(line + (True,))

        table = extended

    result: list[tuple[tuple[bool, ...], bool]] = []

    for line in table:
        mapping = {k: v for k, v in zip(flag_names, line)}
        policy_value = policy(mapping)

        result.append((line, policy_value))

    return result
