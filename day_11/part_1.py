import re
from collections import deque

Path = tuple[str, set[str]]


class LoopingPathError(Exception):
    pass


def main(puzzle_input: str) -> int:
    return solve(puzzle_input)


def solve(puzzle_input: str, start: str = 'you', end: str = 'out') -> int:
    devices = parse_input(puzzle_input)
    count = 0
    queue: deque[Path] = deque([(start, {start})])

    while queue:
        current_device_name, devices_visited = queue.popleft()

        if current_device_name == end:
            count += 1

            continue

        if current_device_name == 'out':
            continue

        next_step_options = devices[current_device_name]

        for device_name in next_step_options:

            if device_name in devices_visited:
                raise LoopingPathError()

            new_path = (device_name, devices_visited.union({device_name}))
            queue.append(new_path)

    return count


def parse_input(puzzle_input: str) -> dict[str, list[str]]:
    group_matches = re.findall(r'([a-z]{3}):((?: [a-z]{3})+)', puzzle_input)
    devices = {name: outputs_str.split() for name, outputs_str in group_matches}

    return devices
