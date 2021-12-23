from functools import wraps

from functools import wraps


def retry(n):
    def decor(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            counter = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("exc_has_appeared")
                    counter += 1
                    if counter > n:
                        raise e

        return _wrapper
    return decor


class Counter:
    v = 0


@retry(5)
def test_func():
    Counter.v += 1
    if Counter.v < 3:
        raise ValueError
    print("test_func has finished")