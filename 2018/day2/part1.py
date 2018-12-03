from collections import Counter


if __name__ == "__main__":
    two_counts = 0
    three_counts = 0
    with open("input") as f:
        for id_line in f:
            box_id = id_line.strip()
            letter_frequencies = Counter(box_id)
            if any(count == 2 for count in letter_frequencies.values()):
                two_counts += 1
            if any(count == 3 for count in letter_frequencies.values()):
                three_counts += 1
    print(two_counts * three_counts)
