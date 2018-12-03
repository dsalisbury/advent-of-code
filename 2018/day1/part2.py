from itertools import accumulate, islice


def looping_file(path):
    while True:
        yield from open(path)


if __name__ == '__main__':
    seen_frequencies = set()

    running_total = accumulate(map(int, looping_file("input")))
    val_and_seen = (
        (val, val in seen_frequencies, seen_frequencies.add(val))
        for val in running_total
    )
    already_seen_freqs = (val for val, seen, _ in val_and_seen if seen)
    first, = islice(already_seen_freqs, 1)
    print(first)
