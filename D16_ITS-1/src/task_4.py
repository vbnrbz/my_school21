import json
from typing import Dict, Any, Optional, Callable, List

with open('materials/users.json', encoding='utf-8') as file:
    DICT_USERS: Dict[str, Dict[str, str]] = json.load(file)
IS_AUTHORIZED: bool = False
USER_ROLE: Optional[str] = None


def check_login_password(func: Callable[[], Any]) -> Callable[[], Any]:
    def wrapper() -> Any:
        global DICT_USERS, IS_AUTHORIZED, USER_ROLE

        if IS_AUTHORIZED is False:
            login: str = input('Enter login: ')
            password: str = input('Enter password: ')
            if login in DICT_USERS and DICT_USERS[login]['password'] == password:
                IS_AUTHORIZED = True
                USER_ROLE = DICT_USERS[login]['role']
                return func()
            else:
                raise PermissionError('Incorrect login or password!')
        else:
            return func()
    return wrapper


def has_permission(permission: List[str]):
    def decorator(func: Callable[[], Any]) -> Callable[[], Any]:
        def wrapper() -> Any:
            global USER_ROLE
            if USER_ROLE in permission:
                return func()
            else:
                raise PermissionError(f'The {USER_ROLE} does not have the right to perform the function {func.__name__}!')

        return wrapper
    return decorator


@check_login_password
@has_permission(['doctor'])
def stub_write_recipe() -> str:
    return """Example of a prescription.
Pum-pum-pum 2 times a day for 5 days.
Tam-tam-tam 3 times a day before meals for 3 days.
Dum-dum-dum 1 time per day for 10 days."""


@check_login_password
@has_permission(['doctor', 'nurse'])
def stub_add_to_schedule() -> str:
    return "The patient has an appointment with a doctor for this day, at this time"


if __name__ == '__main__':
    print(stub_write_recipe())
    print('-' * 50)
    print(stub_add_to_schedule())
