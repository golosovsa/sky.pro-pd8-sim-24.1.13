from functools import wraps


def logger(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        exc_has_appeared = False
        try:
            func(*args, **kwargs)
        except:
            exc_has_appeared = True
        finally:
            print(func.__name__)
            if exc_has_appeared:
                print("exc_has_appeared")
    return _wrapper
