import csv
import tabulate
from typing import List, Any, Union


class ScheduleHospital:
    """Class for working with schedules of doctors"""

    def __init__(self, doctor_name: str, doctor_speciality: str, schedule_list: List[Union[str, Any]]) -> None:
        """A magic method that is called when an object is initialized."""

        self.doctor_name: str = doctor_name.title()
        self.doctor_speciality: str = doctor_speciality.title()
        self.schedule_list: List[Union[str, Any]] = schedule_list

    def print_schedule(self) -> None:
        """Function for beautiful display of the schedule on the screen

        This function checks if the schedule list is a list and then
        formats it nicely using the tabulate library.
        """
        if isinstance(self.schedule_list, list):
            print(tabulate.tabulate(self.schedule_list[1:], self.schedule_list[0], tablefmt="github"))

    def write_to_csv(self, path: str) -> None:
        """Function for writing a schedule to a file

        This method attempts to write the schedule list to a CSV file,
        named after the doctor's name and speciality. If the directory
        does not exist, it will raise a FileNotFoundError.
        """
        try:
            with open(f'{path}/{self.doctor_name} ({self.doctor_speciality}).csv',
                      'w', newline='', encoding='utf-8') as file:
                schedule_writer = csv.writer(file)
                schedule_writer.writerows(self.schedule_list)
        except FileNotFoundError:
            print('There is no such file!')


if __name__ == "__main__":
    sch = ScheduleHospital(
        "Ivanov Ivan Ivanovich", "Therapist", [["Column 1", "Column 2"], [1, 2]]
    )

    print(ScheduleHospital.__doc__)
    print(ScheduleHospital.__init__.__doc__)
    print(ScheduleHospital.print_schedule.__doc__)
    print(ScheduleHospital.write_to_csv.__doc__)
