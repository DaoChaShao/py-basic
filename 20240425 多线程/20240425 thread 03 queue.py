import threading
from queue import Queue

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


def square_number(prompt_list):
    '''
    计算输入的数字的平方
    :param prompt_list: 输入的数字列表
    :return: 计算结果列表
    '''
    for num in range(len(prompt_list)):
        result = num ** 2


def multiple_threads():
    '''
    多线程计算数字的平方
    :return:
    '''
    prompt_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_list = []
    queue = Queue()
    for num in prompt_list:
        queue.put(num)
    for i in range(4):
        t = threading.Thread(target=square_number, args=(queue,))
        t.start()
    for i in range(len(prompt_list)):
        result_list.append(queue.get())
    print(result_list)


if __name__ == '__main__':
    pass
