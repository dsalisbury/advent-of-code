from operator import methodcaller
from itertools import combinations


def has_one_difference(a, b):
    found_difference = False
    for val_a, val_b in zip(a, b):
        if val_a != val_b:
            if found_difference:
                # already had one difference and found a second
                return False
            found_difference = True
    return found_difference


if __name__ == '__main__':
    with open("input") as f:
        pairings = combinations(map(methodcaller('strip'), f), 2)
    single_differences = filter(lambda pair: has_one_difference(*pair), pairings)
    box1, box2 = next(single_differences)
    print(''.join(val_a for val_a, val_b in zip(box1, box2) if val_a == val_b))
