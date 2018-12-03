from itertools import accumulate, dropwhile, islice


def looping_file(path):
    while True:
        with open(path) as f:
            yield from f


class TruthyAddySet(set):
    def add(self, value):
        if value in self:
            return False
        super().add(value)
        return True


if __name__ == '__main__':
    seen_frequencies = TruthyAddySet()

    running_total = accumulate(map(int, looping_file("input")))
    already_seen_freqs = dropwhile(
        seen_frequencies.add,
        running_total)
    first, = islice(already_seen_freqs, 1)
    print(first)
