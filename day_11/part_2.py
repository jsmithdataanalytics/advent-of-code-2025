from collections import deque

from day_11.part_1 import parse_input as part_1_parse_input

DeviceMap = dict[str, tuple[set[str], set[str]]]


def main(puzzle_input: str) -> int:
    devices = parse_input(puzzle_input)

    leg_1 = solve(devices, start='svr', end='fft')
    leg_2 = solve(devices, start='fft', end='dac')
    leg_3 = solve(devices, start='dac', end='out')

    return leg_1 * leg_2 * leg_3


def solve(devices: DeviceMap, start: str, end: str) -> int:
    start_descendants = get_descendants(devices, start)
    queue = deque([start])
    solutions = {}

    while True:
        device_name = queue.popleft()
        children, parents = devices[device_name]

        if device_name == start:
            solutions[device_name] = 1

        else:
            solutions[device_name] = sum(solutions[parent] for parent in parents if parent in start_descendants)

        if device_name == end:
            break

        for child_device_name in children:
            _, child_device_parents = devices[child_device_name]

            if all(p in solutions or p not in start_descendants for p in child_device_parents):
                queue.append(child_device_name)

    return solutions[end]


_get_descendants_cache = {}


def get_descendants(devices: DeviceMap, start: str) -> set[str]:

    if start in _get_descendants_cache:
        return _get_descendants_cache[start]

    descendants = {start}
    children, _ = devices.get(start, (set(), set()))

    for child in children:
        descendants.update(get_descendants(devices, child))

    _get_descendants_cache[start] = descendants

    return descendants


def parse_input(puzzle_input: str) -> DeviceMap:
    d = part_1_parse_input(puzzle_input)
    devices = {name: (set(children), {n for n, c in d.items() if name in c}) for name, children in d.items()}
    devices['out'] = (set(), {n for n, (c, _) in devices.items() if 'out' in c})

    return devices
