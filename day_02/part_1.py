
def main(puzzle_input: str) -> int:
    id_ranges = parse_input(puzzle_input)
    total = 0

    for id_range in id_ranges:

        for product_id in id_range:
            product_id_str = str(product_id)

            if len(product_id_str) % 2:
                continue

            i = len(product_id_str) // 2

            if product_id_str[:i] == product_id_str[i:]:
                total += product_id

    return total


def parse_input(puzzle_input: str) -> list[range]:
    string_pairs = [range_str.split('-') for range_str in puzzle_input.strip().split(',')]

    return [range(int(str_1), int(str_2) + 1) for str_1, str_2 in string_pairs]
