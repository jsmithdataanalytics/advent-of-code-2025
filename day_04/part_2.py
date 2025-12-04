from day_04.part_1 import parse_input, find_accessible_rolls


def main(puzzle_input: str) -> int:
    grid = parse_input(puzzle_input)
    num_rolls_removed = 0

    while True:
        accessible_rolls = find_accessible_rolls(grid)

        if not accessible_rolls:
            break

        for i, j in accessible_rolls:
            grid[i][j] = False

        num_rolls_removed += len(accessible_rolls)

    return num_rolls_removed
