from src.schedule_1 import Schedule


def main():
    name_1 = input('Enter the full name of the first doctor: ').title()
    spec_1 = input('Enter the speciality of the first doctor: ').title()
    name_2 = input('Enter the full name of the second doctor: ').title()
    spec_2 = input('Enter the speciality of the second doctor: ').title()

    medic_1 = Schedule()
    medic_1.doctor_name = name_1
    medic_1.doctor_speciality = spec_1

    medic_2 = Schedule()
    medic_2.doctor_name = name_2
    medic_2.doctor_speciality = spec_2

    print(Schedule.description)
    print(medic_1.doctor_name)
    print(medic_1.doctor_speciality)
    print(medic_2.doctor_name)
    print(medic_2.doctor_speciality)

    return medic_1, medic_2

if __name__ == '__main__':
    main()