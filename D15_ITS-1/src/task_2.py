import copy
import json
from typing import Dict, Any, List, Tuple


def anonymize_patient(d: Dict[str, Any]) -> Dict[str, Any]:
    d.pop('Name')
    d.pop('Surname')
    d.pop('Patronymic')
    return d


def change_blood_type(d: Dict[str, Any]) -> Dict[str, Any]:
    blood = {
        "O+": "I+",
        "A+": "II+",
        "B+": "III+",
        "AB+": "IV+",
        "O-": "I-",
        "A-": "II-",
        "B-": "III-",
        "AB-": "IV-"
    }
    d['Blood group'] = blood[d['Blood group']]
    return d


def change_type_age(d: Dict[str, Any]) -> Dict[str, Any]:
    d['Age'] = int(d['Age'])
    return d


def process_patients(func, l_d: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    new_l_d: List[Dict[str, Any]] = copy.deepcopy(l_d)
    return [func(i) for i in new_l_d]


def main(path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    with open(path, encoding='utf-8') as file:
        l: List[Dict[str, Any]] = json.load(file)
    x: List[Dict[str, Any]] = process_patients(anonymize_patient, l)
    y: List[Dict[str, Any]] = process_patients(change_blood_type, l)
    z: List[Dict[str, Any]] = process_patients(change_type_age, l)
    return x, y, z


if __name__ == '__main__':
    path: str = 'materials/patients.json'
    main(path)
