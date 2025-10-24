

def decorator(name):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f'Before calling the function，{name} is here')
            result = func(*args, **kwargs)
            print(f'After calling the function, {name} leave(s)')
            return result
        return inner
    return wrapper


@decorator('John')
def hello():
    print('Hello World!')


hello()
