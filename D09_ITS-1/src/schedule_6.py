from datetime import datetime, timedelta
from tabulate import tabulate
import csv

class Schedule:
    description = 'Class for working with schedules of doctors'

    def __init__(self, doctor_name, doctor_speciality, time_start, time_end, duration):
        self.doctor_name = doctor_name
        self.doctor_speciality = doctor_speciality
        self.time_start = time_start
        self.time_end = time_end
        self.duration = duration
        self.schedule_list = self.__create_schedule()

    def __get_list_timestamps_for_schedule(self):
        my_list = []
        self.time_start = datetime.strptime(self.time_start, '%H:%M')
        self.time_end = datetime.strptime(self.time_end, '%H:%M')

        while self.time_start <= self.time_end:
            my_list.append(self.time_start.strftime('%H:%M'))
            self.time_start += timedelta(minutes=self.duration)

        return my_list

    def __create_schedule(self):
        full_list = [['Time', 'Patient', 'The patient visited the doctor']]
        times = self.__get_list_timestamps_for_schedule()
        for i in range(len(times)):
            l = []
            l.extend([times[i], '', 'No'])
            full_list.append(l)
        return full_list

    def print_schedule(self):
        print(tabulate(self.schedule_list, headers='firstrow', tablefmt='github'))

    def write_to_csv(self):
        new_name = self.doctor_name.replace(' ', '_') + '_' + self.doctor_speciality
        with open(f'src/{new_name}.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(self.schedule_list)

    def add_patient_to_schedule(self, time, pacient):
        k = 0
        for i in range(len(self.schedule_list)):
            if time in self.schedule_list[i]:
                k += 1
                self.schedule_list[i][1] = pacient
        if k == 0:
            print('This time is not on the schedule!')