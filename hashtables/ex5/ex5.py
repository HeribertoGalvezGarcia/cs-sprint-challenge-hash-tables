from collections import defaultdict
from typing import List


def finder(files: List[str], queries: List[str]) -> List[str]:
    """
    YOUR CODE HERE
    """

    paths = defaultdict(list)

    for full in files:
        for path in full.split('/'):
            if path:
                paths[path].append(full)

    return [full for path in queries if (full_paths := paths.get(path)) is not None for full in full_paths]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
