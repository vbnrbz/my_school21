import json
from typing import Dict, Callable

with open('materials/users.json', encoding='utf-8') as file:
    DICT_USERS: Dict[str, Dict[str, str]] = json.load(file)
IS_AUTHORIZED: bool = False


def check_login_password(func):
    def wrapper():
        global DICT_USERS, IS_AUTHORIZED

        if IS_AUTHORIZED is False:
            login: str = input('Enter login: ')
            password: str = input('Enter password: ')
            if login in DICT_USERS and DICT_USERS[login]['password'] == password:
                IS_AUTHORIZED = True
                return func()
            else:
                raise PermissionError('Incorrect login or password!')
        else:
            return func()
    return wrapper


@check_login_password
def stub_write_recipe() -> str:
    return """Example of a prescription.
Pum-pum-pum 2 times a day for 5 days.
Tam-tam-tam 3 times a day before meals for 3 days.
Dum-dum-dum 1 time per day for 10 days."""


@check_login_password
def stub_add_to_schedule() -> str:
    return "The patient has an appointment with a doctor for this day, at this time"


if __name__ == '__main__':
    print(stub_write_recipe())
    print(stub_add_to_schedule())
