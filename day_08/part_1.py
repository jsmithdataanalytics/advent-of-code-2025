from itertools import combinations
from math import prod

Position = tuple[int, int, int]
Connection = tuple[Position, Position]
Circuit = set[Position]


def main(puzzle_input: str) -> int:
    connections, circuits = parse_input(puzzle_input)
    circuits, _ = make_connections_until_one_circuit(connections[:1000], circuits)
    biggest_circuits = sorted(circuits, key=lambda s: len(s), reverse=True)[:3]

    return prod(len(circuit) for circuit in biggest_circuits)


def make_connections_until_one_circuit(
    connections: list[Connection],
    circuits: list[Circuit],
) -> tuple[list[Circuit], Connection | None]:

    for box_position_1, box_position_2 in connections:
        circuit_1 = next(circuit for circuit in circuits if box_position_1 in circuit)
        circuit_2 = next(circuit for circuit in circuits if box_position_2 in circuit)

        if circuit_1 != circuit_2:
            circuit_1.update(circuit_2)
            circuit_2.clear()

            circuits = [circuit for circuit in circuits if circuit]
            
            if len(circuits) == 1:
                return circuits, (box_position_1, box_position_2)

    return circuits, None


def get_connections(box_positions: list[Position]) -> list[Connection]:
    connections = {}

    for connection in combinations(box_positions, 2):
        (x1, y1, z1), (x2, y2, z2) = connection
        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

        connections[connection] = distance

    return sorted(connections, key=lambda c: connections[c])


def parse_input(puzzle_input: str) -> tuple[list[Connection], list[Circuit]]:
    lines = [line.strip().split(',') for line in puzzle_input.strip().split('\n') if line.strip()]
    box_positions = [(int(x_str), int(y_str), int(z_str)) for x_str, y_str, z_str in lines]

    connections = get_connections(box_positions)
    circuits = [{box_position} for box_position in box_positions]

    return connections, circuits
