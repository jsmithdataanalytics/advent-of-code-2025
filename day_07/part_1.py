
def main(puzzle_input: str) -> int:
    start_j, num_iterations, splitter_positions = parse_input(puzzle_input)
    beams = {start_j}
    count = 0

    for i in range(num_iterations):
        new_beams = set()

        for beam_j in beams:

            if (i + 1, beam_j) in splitter_positions:
                new_beams.add(beam_j - 1)
                new_beams.add(beam_j + 1)

                count += 1

            else:
                new_beams.add(beam_j)

        beams = new_beams

    return count


def parse_input(puzzle_input: str) -> tuple[int, int, set[tuple[int, int]]]:
    char_grid = [list(line.strip()) for line in puzzle_input.strip().split('\n') if line.strip()]
    start_j = 0
    lowest_splitter_i = 0
    splitter_positions = set()

    for i in range(len(char_grid)):
        for j in range(len(char_grid[0])):

            if char_grid[i][j] == 'S':
                start_j = j

            elif char_grid[i][j] == '^':
                splitter_positions.add((i, j))
                lowest_splitter_i = i

    return start_j, lowest_splitter_i, splitter_positions
