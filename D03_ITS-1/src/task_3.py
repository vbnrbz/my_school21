"""
Пример кода с ошибкой №3
"""


string = 'I like administration of hospital   '

exclamation_point = '!'
exclamation_point *= 3  # О, кстати, популярный метод записи операций — '*=', '+=', '-=' и т.д. Изучи такие записи.

string = string.strip()  # И не стесняйся гуглить неизвестные методы.
string = string[:12].upper()

print(f'{string}{exclamation_point} Oh, this is so unexpected and nice.')
