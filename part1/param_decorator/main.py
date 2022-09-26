# Напишите декоратор @retry, который n раз повторяет вызов функции
# если она упала (произошло исключение). Если функция упала,
# но еще не превышен лимит падений, то выведете сообщение “exc_has_appeared”.
# Если лимит превышен, то нужно выбросить исключение, которые произошло в функции
# Количество повторов передается в декоратор с помощью параметра.
from functools import wraps


def retry(count):
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            counter = 0
            while True:
                try:
                    func(*args, **kwargs)
                    break
                except Exception as error:
                    counter += 1
                    if counter >= count:
                        raise error
                    print("exc_has_appeared")

        return _wrapper
    return wrapper



# Код для самопроверки
class Counter:
    v = 0

# Здесь функция, к которой мы применим декоратор
# срабатывает только на 3 раз.
# В тестах может быть другое значение.


@retry(5)
def test_func():
    Counter.v += 1
    if Counter.v < 3:
        raise ValueError
    print("test_func has finished")


# Запустите этот файл для проверки
if __name__ == "__main__":
    test_func()
