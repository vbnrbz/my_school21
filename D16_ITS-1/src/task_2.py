import json
from typing import Dict, Callable

with open('materials/users.json', encoding='utf-8') as file:
    DICT_USERS: Dict[str, Dict[str, str]] = json.load(file)


def stub_write_recipe() -> str:
    return """Example of a prescription.
Pum-pum-pum 2 times a day for 5 days.
Tam-tam-tam 3 times a day before meals for 3 days.
Dum-dum-dum 1 time per day for 10 days."""


def stub_add_to_schedule() -> str:
    return "The patient has an appointment with a doctor for this day, at this time"


def check_login_password(func: Callable[[], str]) -> Callable[[], str]:
    global DICT_USERS

    login: str = input('Enter login: ')
    password: str = input('Enter password: ')

    if login in DICT_USERS and DICT_USERS[login]['password'] == password:
        print('Signal from function')
        return func
    else:
        raise PermissionError('Incorrect login or password!')


if __name__ == '__main__':
    stub_write_recipe: Callable[[], str] = check_login_password(stub_write_recipe)
    stub_add_to_schedule: Callable[[], str] = check_login_password(stub_add_to_schedule)

    print('-' * 50)
    print('Signal before the main call')
    print('-' * 50)
    print(stub_write_recipe())
    print(stub_add_to_schedule())
