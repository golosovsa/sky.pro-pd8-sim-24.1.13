import re


def clock_checker(input_str):
    regex = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    m = regex.match(input_str)
    return bool(m)


if __name__ == "__main__":
    value = "2021-12-31 23:45:20 "
    print(value, clock_checker(value))  # Ожидаем True
    value = "20211231 23:45:20 "
    print(value, clock_checker(value))  # Ожидаем False
    value = "2021-01-03 17:30:20 "
    print(value, clock_checker(value))  # Ожидаем True
