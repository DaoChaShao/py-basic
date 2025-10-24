from random import randint


class Calculation(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def decorator_beautifier(func):
        def wrapper(*args, **kwargs):
            if args and hasattr(args[0], "__class__") and isinstance(args[0], Calculation):
                class_name = args[0].__class__.__name__.upper()
            else:
                class_name = "independent function".upper()
            result = func(*args, **kwargs)
            decorator_output = (
                f"{'*' * 50}\n"
                f"The function {func.__name__.upper()} of "
                f"the class {class_name}\n"
                f"{'-' * 50}\n"
                f"The result is:\n"
                f"{result}\n"
                f"{'-' * 50}\n"
                f"The function {func.__name__.upper()} is Completed\n"
                f"{'*' * 50}"
            )
            return decorator_output

        return wrapper

    @decorator_beautifier
    def addition(self) -> int:
        return self.x + self.y

    decorator_beautifier = staticmethod(decorator_beautifier)


@Calculation.decorator_beautifier
def subtraction(x: int, y: int) -> int:
    return x - y


def main():
    x: int = randint(1, 100)
    y: int = randint(1, 100)
    cal = Calculation(x, y)
    print(cal.addition())

    print(subtraction(x, y))


if __name__ == "__main__":
    main()
