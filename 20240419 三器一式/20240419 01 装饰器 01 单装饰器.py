
import time


def decorator_timer(func):
    '''
    装饰器：打印函数执行时间
    :param func: 被装饰的函数
    :return: 被装饰函数的返回值
    '''
    def wrapper(*args, **kwargs):
        time_start = time.time()  # 被装饰函数之前运行的代码
        result = func(*args, **kwargs)  # 被装饰函数的运行代码，并获取返回值
        time_end = time.time()  # return之前，被装饰函数之后运行的代码
        time_elapsed = time_end - time_start
        print(f'函数 {func.__name__} 执行耗时 {time_elapsed:.2f} 秒')
        return result  # 返回被装饰函数的返回值
    return wrapper  # 返回装饰器函数


def decorator_example(func):
    '''
    装饰器：说明
    :param func: 被装饰的函数
    :return: 被装饰函数的返回值
    '''
    def wrapper(*args, **kwargs):
        while True:  # 循环条件不满足时，继续执行
            if func(*args, **kwargs):
                time_start = time.time()  # 被装饰函数之前运行的代码
                result = func(*args, **kwargs)  # 被装饰函数的运行代码，并获取返回值
                time_end = time.time()  # return之前，被装饰函数之后运行的代码
                time_elapsed = time_end - time_start
                print(f'函数 {func.__name__} 执行耗时 {time_elapsed:.2f} 秒')
                return result  # 返回被装饰函数的返回值
            else:
                print(f'函数 {func.__name__} 条件不满足，继续执行')
    return wrapper  # 返回装饰器函数


@decorator_timer
def processing_bar():
    time_u_need = 1000
    for i in range(time_u_need):
        for j in range(time_u_need):
            k = i * j
            print('Processing,'
                  f'|{"|" * ((i + 1) * 50 // time_u_need):50}|'
                  f'{(i + 1) * 100 // time_u_need}%',
                  end='\r')


processing_bar()
