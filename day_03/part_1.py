
def main(puzzle_input: str) -> int:
    return solve(puzzle_input, num_batteries_per_bank=2)


def solve(puzzle_input: str, num_batteries_per_bank: int) -> int:
    banks = parse_input(puzzle_input)
    total_joltage = 0

    for bank in banks:
        bank_joltage = 0
        start = 0

        for exponent in reversed(range(num_batteries_per_bank)):
            end = len(bank) - exponent
            digit = max(bank[start:end])
            start += bank[start:].index(digit) + 1

            bank_joltage += digit * (10 ** exponent)

        total_joltage += bank_joltage

    return total_joltage


def parse_input(puzzle_input: str) -> list[list[int]]:
    return [list(map(int, line)) for line in puzzle_input.strip().split('\n')]
