import math


average_dose_per_day = int(input("Enter the average daily dose in mg/kg (10 or 15): "))
if average_dose_per_day in (10, 15):
    weight = float(input("Enter the weight of patient: "))
    days_treatment = int(input("Enter the number of days in the course of treatment: "))
    half_pill_per_day = 0
    pills_packs = 0
    if days_treatment > 0 and weight > 0:
        pill_per_day = weight * average_dose_per_day / 250
        half_pill_per_day = round(pill_per_day / 2, 1)
        if half_pill_per_day % 1 == 0:
            half_pill_per_day = int(half_pill_per_day)
        pills_packs = math.ceil(pill_per_day * days_treatment / 50)

    print(f"Patient needs to take {half_pill_per_day} pill(s) 2 times a day")
    print(
        f"Need {pills_packs} pack(s) of 50 pills (250 mg) for the entire course of treatment"
    )
else:
    print(
        "The daily dose is not 10 or 15 mg/kg! The other doses are not yet calculated!"
    )
