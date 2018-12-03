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
    frequency = 0
    with LoopingFile("input") as f:
        for change in f:
            frequency += int(change)
            if frequency in seen_frequencies:
                print(frequency)
                break
            seen_frequencies.add(frequency)
