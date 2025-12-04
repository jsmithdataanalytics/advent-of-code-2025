
def main(puzzle_input: str) -> int:
    grid = parse_input(puzzle_input)

    return len(find_accessible_rolls(grid))


def find_accessible_rolls(grid: list[list[bool]]) -> set[tuple[int, int]]:
    accessible_rolls = set()

    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i, row in enumerate(grid):
        for j, roll_found in enumerate(row):

            if roll_found:
                neighbours = [(i + a, j + b) for a, b in offsets]
                neighbours = [(c, d) for c, d in neighbours if c in range(len(grid)) and d in range(len(row))]
                num_neighbours_with_paper = len([(c, d) for c, d in neighbours if grid[c][d]])

                if num_neighbours_with_paper < 4:
                    accessible_rolls.add((i, j))

    return accessible_rolls


def parse_input(puzzle_input: str) -> list[list[bool]]:
    return [[char == '@' for char in line.strip()] for line in puzzle_input.strip().split('\n')]
