from datetime import datetime
from typing import Callable, Any


def log_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with open('src/execution_log_1.log', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Function {func.__name__} was executed with the following arguments: args={args}, kwargs={kwargs}\n')
        return func(*args, **kwargs)
    return wrapper


@log_execution_time
def stub_write_recipe(
    signature_name: str,
    signature_speciality: str = 'Doctor-therapist'
) -> str:
    return f"""Example of a prescription.
Pum-pum-pum 2 times a day for 5 days.
Tam-tam-tam 3 times a day before meals for 3 days.
Dum-dum-dum 1 time per day for 10 days.

{signature_name}
{signature_speciality}"""


@log_execution_time
def stub_add_to_schedule(day: str, time_: str) -> str:
    return f"The patient has an appointment with a doctor on {day}, at {time_}"


if __name__ == '__main__':
    print(stub_write_recipe(signature_name='Ivanov Ivan Ivanovich', signature_speciality='Doctor-surgeon'))
    print(stub_add_to_schedule('2024-02-13', '13:00'))
