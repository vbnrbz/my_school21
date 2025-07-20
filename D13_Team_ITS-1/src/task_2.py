from typing import List, Union, Tuple, Optional


def number_of_differences(l1: List[Union[int, str, bool]], l2: List[Union[int, str, bool]]) -> Optional[int]:
    if type(l1) != list or type(l2) != list:
        return None

    k: int = 0
    for i in l2:
        if isinstance(i, (int, str, bool)) and i not in l1:
            k += 1
    return k


def calculate_area(s: str, cort: Union[Tuple[float, float], float]) -> Optional[float]:
    if s == 'rectangle' and isinstance(cort, tuple) and len(cort) == 2:
        if isinstance(cort[0], float) and isinstance(cort[1], float):
            return round(cort[0] * cort[1], 2)
    elif s == 'circle' and isinstance(cort, float):
        return round(3.14159 * cort * cort, 2)
    else:
        return None
