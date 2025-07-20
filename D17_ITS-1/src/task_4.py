def main() -> None:
    """Add patients to a queue and manage their removal."""
    limit = 4
    dict_patients = {}

    while len(dict_patients) < limit:
        option = input(
            "-" * 50 + "\n"
            "Enter:\n"
            " - 1, if you want to add a patient to the queue;\n"
            " - 2, if you want to remove a patient from the queue;\n"
            " - 3, if you want to see the current queue;\n"
            " - 4, if you want to stop the program and see the resulting queue.\n"
            + "-" * 50 + "\n"
        )
        if option == "1":
            time_patient = input(
                "Enter the time and the full name of patient "
                "(separated by a comma and a space - '08:00, Ivanov A.A.'): "
            )
            time_patient = time_patient.title()
            time, patient = time_patient.split(", ")

            if time in dict_patients:
                print("This time is already taken!")
            elif patient in dict_patients.values():
                print("There is already such a patient on the queue!")
            else:
                dict_patients[time] = patient
        elif option == "2":
            time = input(
                "Enter the time of the patient you want to remove from the queue (e.g. 08:00 or 10:15): "
            )

            try:
                dict_patients.pop(time)
            except KeyError:
                print("This time is free")
        elif option == "3":
            if dict_patients:
                print(f"Current queue - {dict_patients}")
            else:
                print("The queue is empty!")
        elif option == "4":
            break
    else:
        print("The queue is full!")

    if dict_patients:
        print(f"Current queue - {dict_patients}")
    else:
        print("The queue is empty!")


if __name__ == "__main__":
    main()
