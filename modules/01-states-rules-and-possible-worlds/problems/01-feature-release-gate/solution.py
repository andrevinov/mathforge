def can_release(
    approved: bool,
    tests_passed: bool,
    maintenance_mode: bool,
    emergency_override: bool,
) -> bool:
    return approved and tests_passed and (maintenance_mode or emergency_override)
