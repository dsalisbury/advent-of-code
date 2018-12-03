from itertools import accumulate, dropwhile, islice


def looping_file(path):
    while True:
        with open(path) as f:
            yield from f


if __name__ == '__main__':
    seen_frequencies = set()

    def not_seen(value):
        if value in seen_frequencies:
            return False
        seen_frequencies.add(value)
        return True

    running_total = accumulate(map(int, looping_file("input")))
    already_seen_freqs = dropwhile(
        not_seen,
        running_total)
    first, = islice(already_seen_freqs, 1)
    print(first)
