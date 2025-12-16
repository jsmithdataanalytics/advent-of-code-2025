from itertools import product

from day_10.part_1 import parse_input, Button, State

Machine = tuple[list[Button], State]


class NoSolution(Exception):
    pass


cache = {}


def main(puzzle_input: str) -> int:
    machines = [(buttons, joltages) for _, buttons, joltages in parse_input(puzzle_input)]
    total = 0

    for i, machine in enumerate(machines):
        cache.clear()

        print(f'solving machine {i}')
        total += solve_machine(machine)
        print(f'solved machine {i}')

    return total


def solve_machine(machine: Machine) -> int:
    buttons, joltages_goal = machine

    if joltages_goal in cache:
        return cache[joltages_goal]

    if all(joltage == 0 for joltage in joltages_goal):
        return 0

    lights_goal = tuple(joltage % 2 for joltage in joltages_goal)

    parity_solutions_without_dupes = {}

    for pattern in product([True, False], repeat=len(buttons)):
        pattern = tuple(pattern)
        state = (0,) * len(joltages_goal)

        for i, is_button_pressed in enumerate(pattern):
            button = buttons[i]

            if is_button_pressed:
                state = tuple(state[j] + int(j in button) for j in range(len(state)))

        lights = tuple(joltage % 2 for joltage in state)

        if lights == lights_goal:
            parity_solutions_without_dupes[pattern] = state

    pattern_best_possible_costs = []

    for pattern, state in parity_solutions_without_dupes.items():
        pattern_cost = sum(pattern)
        new_state = tuple(joltages_goal[i] - state[i] for i in range(len(state)))
        new_state = tuple(joltage / 2 for joltage in new_state)
        new_machine = buttons, new_state

        if all(joltage >= 0 for joltage in new_state):

            try:
                new_machine_best_possible_cost = solve_machine(new_machine)

            except NoSolution:
                pass

            else:
                pattern_best_possible_cost = pattern_cost + 2 * new_machine_best_possible_cost
                pattern_best_possible_costs.append(pattern_best_possible_cost)

    if not pattern_best_possible_costs:
        raise NoSolution()

    answer = min(pattern_best_possible_costs)

    cache[joltages_goal] = answer

    return answer
