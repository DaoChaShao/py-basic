

def decorator_01(func):
    def wrapper(*args, **kwargs):
        print('装饰器 01 开始装饰')
        result = func(*args, **kwargs)
        print('装饰器 01 结束装饰')
        return result
    return wrapper


def decorator_02(func):
    def wrapper(*args, **kwargs):
        print('装饰器 02 开始装饰')
        result = func(*args, **kwargs)
        print('装饰器 02 结束装饰')
        return result
    return wrapper


def decorator_03(func):
    def wrapper(*args, **kwargs):
        print('装饰器 03 开始装饰')
        result = func(*args, **kwargs)
        print('装饰器 03 结束装饰')
        return result
    return wrapper


@decorator_01
@decorator_02
@decorator_03
def normal_func():
    print('这是正常函数')


normal_func()
