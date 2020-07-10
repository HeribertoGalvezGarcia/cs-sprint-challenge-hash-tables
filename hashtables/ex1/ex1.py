from typing import List, Tuple, Optional


def get_indices_of_item_weights(weights: List[int], length: int, limit: int) -> Optional[Tuple[int, int]]:
    if length == 2 and sum(weights) == limit:
        return 1, 0

    weights = {item: i for i, item in enumerate(weights)}

    for item, i in weights.items():
        try:
            j = weights[limit - item]
        except KeyError:
            continue
        else:
            return (i, j) if i > j else (j, i)

    return None
