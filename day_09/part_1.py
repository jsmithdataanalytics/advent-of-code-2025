from itertools import combinations
from dataclasses import dataclass


@dataclass
class Position:
    i: int
    j: int


def main(puzzle_input: str) -> int:
    positions = parse_input(puzzle_input)
    max_area = 0

    for p1, p2 in combinations(positions, 2):
        max_area = max(max_area, (abs(p2.i - p1.i) + 1) * (abs(p2.j - p1.j) + 1))

    return max_area


def parse_input(puzzle_input: str) -> list[Position]:
    lines = [line.strip().split(',') for line in puzzle_input.strip().split('\n') if line.strip()]
    positions = [Position(int(str1), int(str2)) for str1, str2 in lines]

    return positions
