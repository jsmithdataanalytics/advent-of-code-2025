from math import prod


def main(puzzle_input: str) -> int:
    problems = parse_input(puzzle_input)

    return solve(problems)


def solve(problems: list[tuple[list[int], bool]]) -> int:
    solutions = [sum(numbers) if op else prod(numbers) for numbers, op in problems]

    return sum(solutions)


def parse_input(puzzle_input: str) -> list[tuple[list[int], bool]]:
    grid = [line.strip().split() for line in puzzle_input.strip().split('\n')]

    problems = []

    for j in range(len(grid[0])):
        numbers = [int(grid[i][j]) for i in range(len(grid) - 1)]
        op = grid[-1][j] == '+'

        problems.append((numbers, op))

    return problems
