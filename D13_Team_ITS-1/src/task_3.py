from typing import Dict, Optional, List, Any

def comparison_dict_and_list(d: Dict[str, str], string_list: List[str]) -> Optional[bool]:
    if type(d) != dict or type(string_list) != list or len([1 for k, v in d.items() if type(k) != str or type(v) != str]) > 0:
        return None

    for i in string_list:
        if i in d.values():
            return True
    return False

def get_user_info(l_d: List[Dict[str, Any]], some_string: str) -> Optional[Dict[str, Any]]:
    if type(some_string) != str or type(l_d) != list:
        return None

    # Проверка
    for i in l_d:
        if isinstance(i, dict):
            if len([1 for j in i if not isinstance(j, str)]) > 0:
                return None
        elif not isinstance(i, dict):
            return None

    for i in l_d:
        if isinstance(i, dict) and some_string in i.values():
            return i
    return None