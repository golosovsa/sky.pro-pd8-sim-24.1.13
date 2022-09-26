
# Напишите функцию find_date, которая находит в
# тексте даты заданного формата.
# Формат даты: "20/May/2015:21:05:28".
# На вход функция принимает строку,
# на выходе возвращает список дат заданного формата.

import re
from operator import itemgetter


def find_date(txt):
    regex = re.compile(r"(\d{2}/\w+/\d{4}(:\d{2}){3})")
    match = regex.findall(txt)
    return list(map(itemgetter(0), match))


if __name__ == "__main__":
    text = """
           63.140.98.80 - - [20/May/2015:21:05:28 +0000] 
           63.140.98.80 - - [20/May/2015:21:05:50 +0000] 
           66.249.73.135 - - [20/May/2015:21:05:00 +0000] 
           180.76.6.56 - - [20/May/2015:21:05:56 +0000] 
           """
    print(find_date(text))

