from typing import List


def has_negatives(a: List[int]) -> List[int]:
    positives = {}
    negatives = {}

    for i in a:
        if i > 0:
            positives[i] = True
        elif i < 0:
            negatives[i] = True

    return [i for i in positives if negatives.get(-i)]


def main() -> None:
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


if __name__ == '__main__':
    main()
