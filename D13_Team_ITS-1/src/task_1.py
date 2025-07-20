from typing import List, Dict, Tuple, Optional


def process_numbers(some_list: List[int]) -> Optional[Tuple[int, int, float]]:
    if type(some_list) == list and len([1 for i in some_list if type(i) != int]) == 0:
        return min(some_list), max(some_list), round(sum(some_list)/len(some_list), 1)
    return None


def find_item(d: Dict[str, int], s: str) -> Optional[int]:
    if type(d) == dict:
        return d.get(s, None)
    return None