from itertools import combinations


def count_differences(a, b):
    return sum(1 for val_a, val_b in zip(a, b) if val_a != val_b)


if __name__ == '__main__':
    with open("input") as f:
        box_ids = [id_line.strip() for id_line in f]
    pairings = combinations(box_ids, 2)
    single_differences = filter(lambda pair: count_differences(*pair) == 1, pairings)
    box1, box2 = next(single_differences)
    print(''.join(val_a for val_a, val_b in zip(box1, box2) if val_a == val_b))
