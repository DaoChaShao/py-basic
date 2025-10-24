'''
多任务
1.并发：多个任务轮流执行
2.并行：多个任务同时执行
'''

import threading
import time

from utils.decorator import beautifier
from utils.highlighter import lines


@beautifier
def current_thread_check():
    '''
    产看当前正在运行的线程数量
    :return:
    '''
    print(f'现在正在运行的线程数量： {threading.active_count()}')  # 输出当前正在运行的线程数量
    lines()
    print(f'当前线程运行的所有线程： {threading.enumerate()}')  # 输出当前运行的所有线程
    lines()
    print(f'当前线程的名称：{threading.current_thread().name}')  # 输出当前线程的名称


@beautifier
def branch_thread_func_01():
    print(f'延时线程：{threading.current_thread().name} 已经开始')
    print(f'当前线程运行的所有线程： {threading.enumerate()}')  # 输出当前运行的所有线程
    lines()
    for i in range(10):
        time.sleep(0.1)
    lines()
    print(f'延时线程：{threading.current_thread().name} 已经结束')
    print(f'当前线程运行的所有线程： {threading.enumerate()}')  # 输出当前运行的所有线程


def main():
    current_thread_check()  # 调用函数查看当前线程数量

    # 创建新线程，并将新线程功能与线程名称绑定（有点儿像pyside6的信号槽）
    new_thread = threading.Thread(target=branch_thread_func_01, name='延时线程')
    new_thread.start()  # 启动新线程
    print(f'主线程结束')


if __name__ == '__main__':
    main()
