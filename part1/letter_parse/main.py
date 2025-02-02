# Представьте, что вы делаете сайт по продаже автомобилей.
# На сайте есть форма, в которую люди вводят информацию о своих автомобилях,
# в том числе и номер машины. После отправки формы данные из нее
# отправляются менеджеру на почту. Менеджеру понадобилось собрать
# все номера машин и он поставил вам такую задачу:
# У вас есть множество писем. Нужно обработать
# каждое письма и найти все номера машины в этих письмах.
# Нужно написать функцию get_plates, которая на вход принимает список
# писем, на выходе формирует генератор (yield) автомобильных номеров (строки).
# Формат номера может быть: а111ан777 или ао250_78 (буквы могут быть в диапазоне а-я)
import re

letters = [
    "заявка от у444хн58 и ав333_78",
    "заявка на продажу от в836иа51",
]


def get_plates(letters):
    regex = re.compile(r"([а-я]{1,2}\d{3}[а-я_]{1,2}\d{2})")
    for letter in letters:
        match = regex.findall(letter)
        if not match:
            continue
        for res in match:
            yield res


if __name__ == "__main__":
    print([x for x in get_plates(letters)])
