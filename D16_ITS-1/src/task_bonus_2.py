import logging
from typing import Callable, Any


def log_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='src/execution_log_2.log', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO, format='%(asctime)s - %(message)s')
        try:
            res = func(*args, **kwargs)
            logging.info(f'Function {func.__name__} was executed with the following arguments: args={args}, kwargs={kwargs}')
            return res
        except TypeError as te:
            logging.error(type(te), exc_info=True)
            return None
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
    print(stub_add_to_schedule('2024-02-13'))
    print(stub_add_to_schedule(day='2024-02-13', time_='13:00', room='402'))
