import math


biohim_analysis = input('Insert test results: ').lower()
alt_index = biohim_analysis.find('alt') + 6
alt = biohim_analysis[alt_index:alt_index + 4]
ast_index = biohim_analysis.find('ast') + 6
ast = biohim_analysis[ast_index:ast_index + 4]
print('-' * 50)
print(f'ALT - {alt}\nAST - {ast}')
print('-' * 50)

average_dose_per_day = int(input('Enter the average daily dose in mg/kg (10 or 15): '))
if average_dose_per_day not in (10, 15):
    print('-' * 50)
    print('The daily dose is not 10 or 15 mg/kg! The other doses are not yet calculated!')
else:
    weight = float(input('Enter the weight of patient: '))
    days_treatment = int(input('Enter the number of days in the course of treatment: '))
    pill_per_day = 0

    if average_dose_per_day == 10:
        if 0 < weight < 36:
            pill_per_day = 1
        elif 36 <= weight < 61:
            pill_per_day = 2
        elif 61 <= weight < 86:
            pill_per_day = 3
        elif weight >= 86:
            pill_per_day = 4
    else:
        if 0 < weight < 41:
            pill_per_day = 2
        elif 41 <= weight < 56:
            pill_per_day = 3
        elif 56 <= weight < 71:
            pill_per_day = 4
        elif 71 <= weight < 91:
            pill_per_day = 5
        elif 91 <= weight < 106:
            pill_per_day = 6
        elif weight >= 106:
            pill_per_day = 7

    print('-' * 50)

    if pill_per_day % 2:
        half_pill_per_day_morning = pill_per_day // 2
        half_pill_per_day_evening = pill_per_day // 2 + 1
        print(f'Patient needs to take {half_pill_per_day_morning} of the pill(s) in the morning and {half_pill_per_day_evening} of the pill(s) in the evening')
    else:
        half_pill_per_day = pill_per_day / 2
        if half_pill_per_day % 1 == 0:
            half_pill_per_day = int(half_pill_per_day)
        print(f'Patient needs to take {half_pill_per_day} pill(s) 2 times a day')

    pills_packs = math.ceil(pill_per_day * days_treatment / 50)
    print(f'Need {pills_packs} pack(s) of 50 pills (250 mg) for the entire course of treatment')
