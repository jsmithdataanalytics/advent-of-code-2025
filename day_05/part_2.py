from day_05.part_1 import parse_input


def main(puzzle_input: str) -> int:
    fresh_ranges, _ = parse_input(puzzle_input)
    partitions = set()

    for fresh_range in fresh_ranges:
        segments = set()

        for partition in partitions:
            a, b, c, d = sorted([fresh_range.start, fresh_range.stop, partition.start, partition.stop])
            segment_1, segment_2, segment_3 = range(a, b), range(b, c), range(c, d)

            if a in partition and a not in fresh_range:
                segments.add(segment_1)

            if b in partition and b not in fresh_range:
                segments.add(segment_2)

            if c in partition and c not in fresh_range:
                segments.add(segment_3)

        partitions = segments
        partitions.add(fresh_range)

    return sum(len(partition) for partition in partitions)
