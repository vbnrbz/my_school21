import json
from typing import Dict, Any, Callable


def stub_write_recipe() -> str:
    return """Example of a prescription.
Pum-pum-pum 2 times a day for 5 days.
Tam-tam-tam 3 times a day before meals for 3 days.
Dum-dum-dum 1 time per day for 10 days."""


def stub_add_to_schedule() -> str:
    return "The patient has an appointment with a doctor for this day, at this time"


def check_login_password(func: Callable[[], Any], d: Dict[str, Dict[str, str]]) -> Callable[[], str]:
    login: str = input('Enter login: ')
    password: str = input('Enter password: ')

    if login in d and d[login]['password'] == password:
        return func()
    else:
        raise PermissionError('Incorrect login or password!')


if __name__ == '__main__':
    with open('materials/users.json', encoding='utf-8') as file:
        x: Dict[str, Dict[str, str]] = json.load(file)
    print(check_login_password(stub_write_recipe, x))
    print(check_login_password(stub_add_to_schedule, x))
