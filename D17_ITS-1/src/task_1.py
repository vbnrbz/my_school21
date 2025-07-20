class Patient:
    def __init__(self, name, age, id_):
        self.name = name
        self.age = age
        self.id_ = id_
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_records(self):
        return self.records


def create_patient(name, age, id_):
    return Patient(name, age, id_)


def add_patient_record(patient, record):
    patient.add_record(record)


def get_patient_records(patient):
    return patient.get_records()


if __name__ == '__main__':
    patient = create_patient('Ivanov Ivan Ivanovich', 30, '125678')
    add_patient_record(patient, 'Blood group: II+')
    add_patient_record(patient, 'Ultrasound: normal')
    records = get_patient_records(patient)
    print(f"The patient {patient.name} has the following records: {records}")
