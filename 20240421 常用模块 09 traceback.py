
# 异常处理：通过tracback模块可以捕获并分析程序运行时发生的异常，并提供详细的错误信息。
import traceback
import logging

'''
try:
    print(1/0)
except ZeroDivisionError as z:
    print("You can't divide by zero!", z)
    traceback.print_exc()  # 打印异常信息  # 系统红字显示
    # print(f"The traceback info is stored in the variable {traceback.format_exc()}")  # 系统白字显示
finally:  # 无论是否有异常，最终终会执行
    print("This code will always run, regardless of any exceptions.")
'''

# 异常捕获与日志记录
logging.basicConfig(  # 基础配置
    filename='log_traceback_example.txt',  # 日志文件名
    level=logging.DEBUG,  # 日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式
)

try:
    print(1/0)
except ZeroDivisionError as z:
    print("You can't divide by zero!", z)
    logging.error(traceback.format_exc())  # 异常信息记录在日志文件中
