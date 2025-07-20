from datetime import datetime, timedelta


class Schedule:
    description = 'Class for working with schedules of doctors'

    def __init__(self, doctor_name, doctor_speciality, time_start, time_end, duration):
        self.doctor_name = doctor_name
        self.doctor_speciality = doctor_speciality
        self.time_start = time_start
        self.time_end = time_end
        self.duration = duration

    def get_list_timestamps_for_schedule(self):
        my_list = []
        self.time_start = datetime.strptime(self.time_start, '%H:%M')
        self.time_end = datetime.strptime(self.time_end, '%H:%M')

        while self.time_start <= self.time_end:
            my_list.append(self.time_start.strftime('%H:%M'))
            self.time_start += timedelta(minutes=self.duration)

        return my_list

