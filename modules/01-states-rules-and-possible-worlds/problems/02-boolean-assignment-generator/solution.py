def generate_boolean_assignments(
    position_count: int,
) -> list[tuple[bool, ...]]:
    assignments: list[tuple[bool, ...]] = [()]

    for _ in range(position_count):
        extended_assignments: list[tuple[bool, ...]] = []

        for assignment in assignments:
            extended_assignments.append(assignment + (False,))
            extended_assignments.append(assignment + (True,))

        assignments = extended_assignments

    return assignments


generate_boolean_assignments(3)
