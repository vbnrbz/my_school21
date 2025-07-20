import json
from typing import Dict, Any


def main(path: str) -> int:
    with open(path, encoding='utf-8') as file:
        x: Dict[str, Any] = json.load(file)
    return recursive_counter(x, 0)


def recursive_counter(x: Dict[str, Any], k: int) -> int:
    for i in x.values():
        if isinstance(i, int):
            k += i
        else:
            k += recursive_counter(i, 0)
    return k


if __name__ == '__main__':
    path = 'materials/number_of_visits.json'
    main(path)
