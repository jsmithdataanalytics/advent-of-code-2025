from abc import ABC
from dataclasses import dataclass
from itertools import combinations

from day_09.part_1 import Position, parse_input


@dataclass
class LineSegment(ABC):
    start: Position
    length: int

    def __len__(self):
        return self.length


class HorizontalLineSegment(LineSegment):

    @property
    def i(self):
        return self.start.i

    @property
    def j_range(self):
        return range(self.start.j, self.start.j + self.length)

    @property
    def end(self):
        return Position(self.i, self.j_range[-1])

    def __contains__(self, item: Position):

        if not isinstance(item, Position):
            raise TypeError('item must be a Position')

        return item.i == self.i and item.j in self.j_range


class VerticalLineSegment(LineSegment):

    @property
    def j(self):
        return self.start.j

    @property
    def i_range(self):
        return range(self.start.i, self.start.i + self.length)

    @property
    def end(self):
        return Position(self.i_range[-1], self.j)

    def __contains__(self, item: Position):

        if not isinstance(item, Position):
            raise TypeError('item must be a Position')

        return item.i in self.i_range and item.j == self.j


def main(puzzle_input: str) -> int:
    red_positions = parse_input(puzzle_input)
    white_line_segments = get_white_line_segments(red_positions)
    max_area = 0

    for p1, p2 in combinations(red_positions, 2):
        p3 = Position(p1.i, p2.j)
        p4 = Position(p2.i, p1.j)

        rectangle_sides = [
            HorizontalLineSegment(start=Position(i=p1.i, j=min(p1.j, p3.j)), length=abs(p1.j - p3.j) + 1),
            HorizontalLineSegment(start=Position(i=p2.i, j=min(p2.j, p4.j)), length=abs(p2.j - p4.j) + 1),
            VerticalLineSegment(start=Position(i=min(p1.i, p4.i), j=p1.j), length=abs(p1.i - p4.i) + 1),
            VerticalLineSegment(start=Position(i=min(p2.i, p3.i), j=p2.j), length=abs(p2.i - p3.i) + 1),
        ]

        rectangle_area = rectangle_sides[0].length * rectangle_sides[2].length

        for side in rectangle_sides:
            is_side_valid = all(not do_lines_intersect(side, wls) for wls in white_line_segments)

            if not is_side_valid:
                break

        else:
            max_area = max(max_area, rectangle_area)

    return max_area


def get_white_line_segments(red_positions: list[Position]):
    green_line_segments = get_line_segments(red_positions)
    white_positions = []

    start_n, leftmost_red_position = min(enumerate(red_positions), key=lambda t: (t[1].j, t[1].i))

    for offset in range(len(red_positions)):
        n = (start_n + offset) % len(red_positions)

        if offset == 0:
            white_positions.append(Position(leftmost_red_position.i - 1, leftmost_red_position.j - 1))

        else:
            red_position, gls_1, gls_2 = red_positions[n], green_line_segments[n - 1], green_line_segments[n]
            previous_white_position = white_positions[-1]

            if isinstance(gls_1, HorizontalLineSegment):
                i_offset = previous_white_position.i - red_position.i

                if red_position == gls_1.end:

                    if red_position == gls_2.start:
                        j_offset = -i_offset

                    else:
                        j_offset = i_offset

                else:

                    if red_position == gls_2.start:
                        j_offset = i_offset

                    else:
                        j_offset = -i_offset

            else:
                j_offset = previous_white_position.j - red_position.j

                if red_position == gls_1.end:

                    if red_position == gls_2.start:
                        i_offset = -j_offset

                    else:
                        i_offset = j_offset

                else:

                    if red_position == gls_2.start:
                        i_offset = j_offset

                    else:
                        i_offset = -j_offset

            white_positions.append(Position(red_position.i + i_offset, red_position.j + j_offset))

    return get_line_segments(white_positions)


def get_line_segments(positions: list[Position]):
    segments = []

    for n, p1 in enumerate(positions):
        m = (n + 1) % len(positions)
        p2 = positions[m]

        if p1.i == p2.i:
            start = Position(p1.i, min(p1.j, p2.j))
            length = abs(p2.j - p1.j) + 1
            line_segment = HorizontalLineSegment(start, length)

        else:
            start = Position(min(p1.i, p2.i), p1.j)
            length = abs(p2.i - p1.i) + 1
            line_segment = VerticalLineSegment(start, length)

        segments.append(line_segment)

    return segments


def do_lines_intersect(
    line_1: HorizontalLineSegment | VerticalLineSegment,
    line_2: HorizontalLineSegment | VerticalLineSegment,
) -> bool:

    if isinstance(line_1, HorizontalLineSegment):

        if isinstance(line_2, HorizontalLineSegment):
            return line_1.start in line_2 or line_2.start in line_1

        else:
            return line_1.i in line_2.i_range and line_2.j in line_1.j_range

    elif isinstance(line_2, VerticalLineSegment):
        return line_1.start in line_2 or line_2.start in line_1

    return line_2.i in line_1.i_range and line_1.j in line_2.j_range
