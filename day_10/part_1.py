import re

State = tuple[int, ...]
Button = set[int]
Machine = tuple[State, list[Button], State]


def main(puzzle_input: str) -> int:
    machines = parse_input(puzzle_input)

    return sum(solve_machine(machine) for machine in machines)


def solve_machine(machine: Machine) -> int:
    lights, buttons, joltages = machine
    goal = lights
    initial_state = (0,) * len(goal)

    cards: dict[State, int] = {initial_state: 0}
    solved: set[State] = set()

    while True:
        solved_state = min(cards, key=lambda k: cards[k])

        shortest_path = cards.pop(solved_state)
        solved.add(solved_state)

        if solved_state == goal:
            break

        for button in buttons:
            new_state = press_button(solved_state, button)

            if new_state not in solved:
                new_state_path = shortest_path + 1
                cards[new_state] = min(cards.get(new_state, new_state_path), new_state_path)

    return shortest_path


def press_button(state: State, button: Button) -> State:
    return tuple(((n + 1) % 2 if i in button else n) for i, n in enumerate(state))


def parse_input(puzzle_input: str) -> list[Machine]:
    lines = [line.strip() for line in puzzle_input.strip().split('\n') if line.strip()]
    lines.sort(key=len)
    machines = []

    for line in lines:
        part_1, part_2, part_3 = re.fullmatch(r'\[(.+)] (.+) \{(.+)}', line).groups()

        lights = tuple(int(char == '#') for char in part_1)
        buttons = [set(map(int, s.split(','))) for s in re.findall(r'\(([0-9,]+)\)', part_2)]
        joltages = tuple(int(s) for s in part_3.split(','))

        machine = (lights, buttons, joltages)

        machines.append(machine)

    return machines
