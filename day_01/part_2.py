from day_01.part_1 import parse_input


def main(puzzle_input: str) -> int:
    turns = parse_input(puzzle_input)
    dial_position = 50
    count = 0

    for turn in turns:

        if turn >= 0:
            count += turn // 100
            count += int(dial_position + (turn % 100) >= 100)

        else:
            count += abs(turn) // 100
            count += int(dial_position - (abs(turn) % 100) <= 0 < dial_position)

        dial_position = (dial_position + turn) % 100

    return count
