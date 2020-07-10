import itertools
from typing import List


def intersection(arrays: List[List[int]]) -> List[int]:
    """
    YOUR CODE HERE
    """

    count = {}
    result = []

    for i in itertools.chain(*arrays):
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1
        else:
            if count[i] == len(arrays):
                result.append(i)

    return result


def main() -> None:
    arrays = [list(range(1000000, 2000000)) + [1, 2, 3], list(range(2000000, 3000000)) + [1, 2, 3],
              list(range(3000000, 4000000)) + [1, 2, 3]]

    print(intersection(arrays))


if __name__ == "__main__":
    main()
