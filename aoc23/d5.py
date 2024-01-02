from .helpers import load_data

seed_chunk, *rest = load_data(5).split("\n\n")
seeds = [int(x) for x in seed_chunk.split(": ")[1].split(" ")]

mappings: list[list[tuple[range, int]]] = [[]]

for chunk in rest:
    for mapping in chunk.split("\n")[1:]:
        dest_start, source_start, n = (int(x) for x in mapping.split(" "))
        offset = dest_start - source_start
        mappings[-1].append((range(source_start, source_start + n), offset))
    mappings.append([])

results = []
for x in seeds:
    for mapping in mappings:
        for span, offset in mapping:
            if x in span:
                x += offset
                break
    results.append(x)

print("p1", min(results))


seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]


def compute_overlap(a: range, b: range) -> tuple[range | None, range | None, range | None]:
    overlap = range(max(a.start, b.start), min(a.stop, b.stop))
    left = range(a.start, overlap.start)
    right = range(overlap.stop, a.stop)

    return left or None, overlap or None, right or None


for mapping in mappings:
    next_ranges = []
    while seed_ranges:
        seed = seed_ranges.pop()
        for m, offset in mapping:
            left, overlap, right = compute_overlap(seed, m)
            if overlap:
                next_ranges.append(range(overlap.start + offset, overlap.stop + offset))
                # add back the left and right subranges if they exist (since they can potentially still be mapped)
                if left:
                    seed_ranges.append(left)
                if right:
                    seed_ranges.append(right)
                break
        else:
            next_ranges.append(seed)
    seed_ranges = next_ranges

print("p2", min(s.start for s in seed_ranges))
