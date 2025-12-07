from day_07.part_1 import parse_input

solutions: dict[tuple[int, int], int] = {}


def main(puzzle_input: str) -> int:
    start_j, lowest_splitter_i, splitter_positions = parse_input(puzzle_input)
    solutions.clear()

    return _count_timelines((0, start_j), lowest_splitter_i, splitter_positions)


def _count_timelines(
    start: tuple[int, int],
    lowest_splitter_i: int,
    splitter_positions: set[tuple[int, int]],
) -> int:

    if start in solutions:
        return solutions[start]

    start_i, start_j = start

    if start_i == lowest_splitter_i:
        num_timelines = 1

    elif (start_i + 1, start_j) in splitter_positions:
        num_timelines = (
                _count_timelines((start_i + 1, start_j - 1), lowest_splitter_i, splitter_positions) +
                _count_timelines((start_i + 1, start_j + 1), lowest_splitter_i, splitter_positions)
        )

    else:
        num_timelines = _count_timelines((start_i + 1, start_j), lowest_splitter_i, splitter_positions)

    solutions[start] = num_timelines

    return num_timelines
