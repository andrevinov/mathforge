def can_release(
    approved: bool,
    tests_passed: bool,
    maintenance_mode: bool,
    emergency_override: bool,
) -> bool:
    return tests_passed and not maintenance_mode and (approved or emergency_override)
