"""
Пример кода с ошибкой №2

Не забудь изучить операции со строками — "+" и "*".
"""


string_1 = 'I do not know if you noticed or not, but strings can be written using three types of quotes'
string_2 = "The previous line is written in single quotes, and this one is in double quotes."
string_3 = """
And what kind of monster is this?
Yes, a multi-line string... It is written using triple quotes.
"""

string_4 = "As one of my friends used to say about"

# Внутри строки цитата, она должна быть обернута какими-то кавычками.
string_5 = ' quotes in Python: "What difference does it make which ones you use? What could possibly go wrong?"'

string_6 = string_4 + string_5

# А это пример многострочных строк. Текст здесь двигать не нужно.
string_7 = """
And in general I agree with him.
It seems that there should not be any problems.
"""

string_8 = '-' * 50
string_9 = string_8 + string_7

print(string_6)
print(string_9)
