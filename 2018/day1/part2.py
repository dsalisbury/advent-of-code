from itertools import accumulate, dropwhile, islice
class LoopingFile:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self._f = open(self.path)
        return self

    def __exit__(self, exc_type, value, traceback):
        self._f.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._f)
        except StopIteration:
            self._f.seek(0)
            return next(self._f)


if __name__ == '__main__':
    seen_frequencies = set()

    def not_seen(value):
        if value in seen_frequencies:
            return False
        seen_frequencies.add(value)
        return True

    with LoopingFile("input") as f:
        running_total = accumulate(map(int, f))
        already_seen_freqs = dropwhile(
            not_seen,
            running_total)
        first, = islice(already_seen_freqs, 1)
        print(first)
