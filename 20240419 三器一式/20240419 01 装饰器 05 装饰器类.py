class CustomisedDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result


class Timer(object):
    """ Timer """

    def __init__(self, precision: int = 6):
        self._precision = precision

    from functools import wraps

    def __call__(self, func):
        from time import perf_counter
        @self.__class__.wraps(func)
        def wrapper(*args, **kwargs):
            print("*" * 50)
            print(f"Function {func.__name__} is starting...")
            print("-" * 50)
            _start = perf_counter()
            result = func(*args, **kwargs)
            _end = perf_counter()
            print(result)
            print("-" * 50)
            print(f"Function {func.__name__} has ended.")
            print("-" * 50)
            print(f"Time elapsed: {(_end - _start):.{self._precision}f} seconds")
            print("*" * 50)
            return result

        return wrapper


@Timer(6)
def my_function(x, y):
    return x + y


my_function(2, 3)  # Output: Before calling the function 5 After calling the function
