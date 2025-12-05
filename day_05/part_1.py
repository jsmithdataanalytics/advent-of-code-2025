
def main(puzzle_input: str) -> int:
    fresh_ranges, ingredient_ids = parse_input(puzzle_input)
    count = 0

    for ingredient_id in ingredient_ids:
        for fresh_range in fresh_ranges:

            if ingredient_id in fresh_range:
                count += 1

                break

    return count


def parse_input(puzzle_input: str) -> tuple[list[range], list[int]]:
    section_1, section_2 = puzzle_input.strip().split('\n\n')

    bounds = [list(map(int, line.strip().split('-'))) for line in section_1.strip().split('\n')]
    fresh_ranges = [range(lb, ub + 1) for lb, ub in bounds]

    ingredient_ids = [int(line.strip()) for line in section_2.strip().split('\n')]

    return fresh_ranges, ingredient_ids
