from day_01.part_1 import parse_input


def solve(puzzle_input: str) -> int:
    list_1, list_2 = parse_input(puzzle_input)

    score = 0

    for num in list_1:
        score += num * list_2.count(num)

    return score
