import re

letters = [
    "заявка от у444хн58 и ав333_78",
    "заявка на продажу от в836иа51",
]


def get_plates(letters):
    for item in letters:
        for p in re.findall(r"[а-я]\d{3}[а-я]{2}\d{2,3}", item):
            yield p
        for p in re.findall(r"[а-я]{2}\d{3}_\d{2,3}", item):
            yield p


if __name__ == "__main__":
    print([x for x in get_plates(letters)])
