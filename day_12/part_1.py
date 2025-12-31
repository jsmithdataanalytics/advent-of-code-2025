import re

Rectangle = tuple[int, int]
PresentCounts = list[int]
PresentAreas = PresentCounts
Problem = tuple[Rectangle, PresentCounts]


def main(puzzle_input: str) -> int:
    present_areas, problems = parse_input(puzzle_input)
    count = 0

    for (height, width), present_counts in problems:
        available_area = height * width
        area_lower_bound = sum(count * present_areas[i] for i, count in enumerate(present_counts))
        area_upper_bound = 9 * sum(present_counts)

        assert (available_area < area_lower_bound) or (available_area >= area_upper_bound)

        count += int(available_area >= area_upper_bound)

    return count


def parse_input(puzzle_input: str) -> tuple[PresentAreas, list[Problem]]:
    *shape_defs, problems_string = puzzle_input.strip().split('\n\n')
    shape_areas = [shape_def.count('#') for shape_def in shape_defs]
    lines = [line.strip() for line in problems_string.strip().splitlines() if line.strip()]
    matches = [re.fullmatch(r'(\d+)x(\d+): (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)', line).groups() for line in lines]
    problem_nums = [list(map(int, groups)) for groups in matches]
    problems = [((nums[0], nums[1]), nums[2:]) for nums in problem_nums]

    return shape_areas, problems
