from collections.abc import Callable


def find_line_value(
    flag_names: tuple[str, ...],
    line: tuple[bool, ...],
    policy: Callable[[dict[str, bool]], bool],
) -> bool:
    return policy({k: v for k, v in zip(flag_names, line)})

def generate_lines(nlines: int) -> tuple[tuple[bool, ...], ...]):
    for nline in enumerate(range(nlines)):
        
        
        

# def build_truth_table(
#     flag_names: tuple[str, ...],
#     policy: Callable[[dict[str, bool]], bool],
# ) -> list[tuple[tuple[bool, ...], bool]]:
#     # Calculate number of lines
#     nlines = 2 ** len(flag_names)

#     result = []

#     # Generate tuples and results
#     for line in enumerate(lines):
        


# def both_enabled(state: dict[str, bool]) -> bool:
#     return state["search_enabled"] and state["billing_enabled"]


# result = find_line_value(
#     ("search_enabled", "billing_enabled"), (False, False), both_enabled
# )

# print(str(result) + "\n")
