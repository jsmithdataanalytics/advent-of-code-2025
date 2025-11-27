
def solve(puzzle_input: str) -> int:
    list_1, list_2 = parse_input(puzzle_input)

    return sum(abs(a - b) for a, b in zip(sorted(list_1), sorted(list_2)))


def parse_input(puzzle_input: str) -> tuple[list[int], list[int]]:
    lines = [line for line in puzzle_input.split('\n') if line.strip()]

    list_1, list_2 = [], []

    for line in lines:
        str_1, str_2 = line.split()

        list_1.append(int(str_1))
        list_2.append(int(str_2))

    return list_1, list_2
