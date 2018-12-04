from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
import re

from shapely.geometry import Point, box
from shapely.ops import cascaded_union

INPUT_LINE_RE = re.compile(
    r"#(?P<number>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)"
)


@dataclass(eq=True, frozen=True)
class Region:
    number: int
    x: int
    y: int
    w: int
    h: int

    @property
    def xw(self) -> int:
        return self.x + self.w

    @property
    def yh(self) -> int:
        return self.y + self.h

    @classmethod
    def from_input(cls, line):
        m = INPUT_LINE_RE.match(line)
        if not m:
            raise ValueError(line)
        inty = {k: int(v) for k, v in m.groupdict().items()}
        return cls(**inty)

    def __bool__(self):
        return self.xw > 0 and self.yh > 0

    def __and__(self, other):
        return self.as_box().intersection(other.as_box())

    def overlaps(self, other):
        this_box = self.as_box()
        other_box = other.as_box()
        # the intersection counts even if the boxes touch but don't overlap in any way, so need to
        # check that
        return this_box.intersects(other_box) and not this_box.touches(other_box)

    def as_box(self):
        return box(self.x, self.y, self.xw, self.yh)


if __name__ == "__main__":
    with open("input") as f:
        regions = [Region.from_input(line) for line in f]
    overlapping_pairs = filter(
        lambda pair: pair[0].overlaps(pair[1]), combinations(regions, 2)
    )
    regions_of_overlaps = [a & b for a, b in overlapping_pairs]
    union = cascaded_union(regions_of_overlaps)
    print(int(union.area))
