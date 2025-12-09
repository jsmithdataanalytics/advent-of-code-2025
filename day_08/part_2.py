from day_08.part_1 import parse_input, make_connections_until_one_circuit


def main(puzzle_input: str) -> int:
    connections, circuits = parse_input(puzzle_input)
    _, final_connection = make_connections_until_one_circuit(connections, circuits)

    (x1, _, _), (x2, _, _) = final_connection

    return x1 * x2
