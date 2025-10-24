
import logging

# filename：文件名
# format：数据的格式化输出，最终在日志文件中的样子
# 时间-名称-级别-模块：具体的错误信息

# datefmt：时间的格式化输出
# level：日志的级别，有debug、info、warning、error、critical五个级别
# stream：日志输出到控制台还是文件，默认输出到控制台

logging.basicConfig(  # 基础配置
    filename='example.log',  # 日志文件名
    level=logging.DEBUG,  # 日志级别，（或者设置为 0 ，表示记录的最低等级）还包括：logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL
    stream=None,  # 日志输出到控制台还是文件，默认输出到控制台
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',  # 日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式
)

# 日志级别
logging.critical('我是一个最高级的错误')  # 记录一个严重错误，50分
logging.error('我是一个普通的错误')  # 记录一个错误，40分
logging.warning('我是一个警告的信息')  # 记录一个警告，30分
logging.info('我是一个普通的信息')  # 记录一些信息，20分
logging.debug('我是一个调试的信息')  # 记录一些调试信息，10分

# logging.ERROR  # ctrl + 点击

# 多系统开发的日志记录
# 系统一
file_handler_system_01 = logging.FileHandler('example.log', 'a', encoding='utf-8')  # 日志文件输出
file_handler_system_01.setLevel(logging.ERROR)  # 日志级别
file_handler_system_01.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))  # 日志格式

logger_system_01 = logging.Logger('system_01', level=logging.ERROR)  # 日志名称
logger_system_01.addHandler(file_handler_system_01)  # 日志输出

# 系统二
file_handler_system_02 = logging.FileHandler('example.log', 'a', encoding='utf-8')  # 日志文件输出
file_handler_system_02.setLevel(logging.INFO)  # 日志级别
file_handler_system_02.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s'))  # 日志格式

logger_system_02 = logging.Logger('system_02', level=logging.INFO)  # 日志名称
logger_system_02.addHandler(file_handler_system_02)  # 日志输出

# 系统一
logger_system_01.error('系统一发生了一个错误')

# 系统二
logger_system_02.info('系统二发生了一个信息')

