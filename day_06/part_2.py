from day_06.part_1 import solve


def main(puzzle_input: str) -> int:
    problems = parse_input(puzzle_input)

    return solve(problems)


def parse_input(puzzle_input: str) -> list[tuple[list[int], bool]]:
    char_grid = [list(line) for line in puzzle_input.split('\n') if line.strip()]

    empty_cols = []
    problems = []

    for j in range(len(char_grid[0])):

        if all(char_grid[i][j] == ' ' for i in range(len(char_grid))):
            empty_cols.append(j)

    for a, b in zip([0] + empty_cols, empty_cols + [len(char_grid[0]) - 1]):
        op = '+' in char_grid[-1][a:b + 1]
        numbers = []

        for j in range(a, b + 1):
            column_chars = [char_grid[i][j] for i in range(len(char_grid) - 1)]
            column_str = ''.join(column_chars).strip()

            if column_str:
                numbers.append(int(column_str))

        problems.append((numbers, op))

    return problems
