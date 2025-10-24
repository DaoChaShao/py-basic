""""
自定义资源上下文管理器（context manager）
1.实现__enter__方法，返回资源对象
2.实现__exit__方法，释放资源
3.使用with语句调用上下文管理器，自动调用__enter__和__exit__方法

例子（常规方法）：
file = open("data_context_manager.txt", "w")
file.write("Hello, world!")
file.close()

"""


class FileManager(object):
    def __init__(self, filename: str, mode: str) -> None:
        self.file_name = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file  # 返回资源对象

    def __exit__(self,
                 exc_type,  # 异常类型
                 exc_val,  # 异常值
                 exc_tb  # 异常追踪信息
                 ):
        if self.file:  # 释放资源
            self.file.close()


class FileOperation(object):
    @staticmethod
    def file_write():
        with FileManager("data_context_manager.txt", "w") as file:
            file.write("Hello, world!")

    @staticmethod
    def file_read():
        with FileManager("data_context_manager.txt", "r") as file:
            content = file.read()
            print(content)


if __name__ == "__main__":
    FileOperation.file_write()
    FileOperation.file_read()
