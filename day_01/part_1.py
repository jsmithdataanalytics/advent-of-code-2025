import re


def main(puzzle_input: str) -> int:
    turns = parse_input(puzzle_input)
    dial_position = 50
    count = 0

    for turn in turns:
        dial_position = (dial_position + turn) % 100

        if dial_position == 0:
            count += 1

    return count


def parse_input(puzzle_input: str) -> list[int]:
    instructions = re.findall(r'([LR])(\d+)', puzzle_input)
    turns = [int(num_clicks) * (-1 if direction == 'L' else 1) for direction, num_clicks in instructions]

    return turns
