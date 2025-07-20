import tabulate
import csv


class ScheduleHospital:
    description = 'Class for working with schedules of doctors'

    def __init__(self, doctor_name, doctor_speciality, schedule_list):
        self.doctor_name = doctor_name.title()
        self.doctor_speciality = doctor_speciality.title()
        self.schedule_list = schedule_list

    def print_schedule(self):
        if isinstance(self.schedule_list, list):
            print(tabulate.tabulate(self.schedule_list[1:], self.schedule_list[0], tablefmt="github"))

    def write_to_csv(self, path):
        try:
            with open(f'{path}/{self.doctor_name} ({self.doctor_speciality}).csv',
                      'w', newline='', encoding='utf-8') as file:
                schedule_writer = csv.writer(file)
                schedule_writer.writerows(self.schedule_list)
        except FileNotFoundError:
            print('There is no such file!')


if __name__ == '__main__':
    sch = ScheduleHospital('Ivanov Ivan Ivanovich', 'Therapist', [['Column 1', 'Column 2'], [1, 2]])
    sch.print_schedule()
    sch.write_to_csv('src')
