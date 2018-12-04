from itertools import combinations

from part1 import Region


if __name__ == "__main__":
    with open("input") as f:
        regions = {Region.from_input(line) for line in f}
    has_overlap = set()
    for a, b in combinations(regions, 2):
        if a.overlaps(b):
            has_overlap |= {a, b}
    print(regions - has_overlap)
