#!/usr/bin/env python3
import collections

def log_and_count(key=None, counts=None):
    def _log_and_count_decorator(func):
        def wrapper(*args, **kwargs):
            if key:
                counts[key] += 1
            else:
                counts[func.__name__] += 1

            result = func(*args, **kwargs)
            print(f"called {func.__name__} with {args} and {kwargs}")
            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__  = func.__doc__
        return wrapper

    return _log_and_count_decorator


my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b


@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b


@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b


f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5, 4)

# a vypíše postupně:
# called f1 with (2,) and {}
# called f2 with (2,) and {'b': 4}
# called f1 with () and {'a': 2, 'b': 4}
# called f2 with (4,) and {}
# called f2 with (5,) and {}
# called f3 with (5,) and {}
# called f3 with (5, 4) and {}

# a po:
print(my_counter)
# vypíše
# Counter({'basic functions': 5, 'f3': 2})