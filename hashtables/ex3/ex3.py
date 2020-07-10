from functools import reduce
from typing import List


def intersection(arrays: List[List[int]]) -> List[int]:
    return list(reduce(lambda x, y: x & y, [{i: True for i in a}.keys() for a in arrays]))


def main() -> None:
    arrays = [list(range(1000000, 2000000)) + [1, 2, 3], list(range(2000000, 3000000)) + [1, 2, 3],
              list(range(3000000, 4000000)) + [1, 2, 3]]

    print(intersection(arrays))


if __name__ == "__main__":
    main()
