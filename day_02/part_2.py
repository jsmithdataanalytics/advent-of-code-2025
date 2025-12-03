import re

from day_02.part_1 import parse_input


def main(puzzle_input: str) -> int:
    id_ranges = parse_input(puzzle_input)
    total = 0

    for id_range in id_ranges:

        for product_id in id_range:
            product_id_str = str(product_id)

            if re.fullmatch(r'(\d+)\1+', product_id_str):
                total += product_id

    return total
