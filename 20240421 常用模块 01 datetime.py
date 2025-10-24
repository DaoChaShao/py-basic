
from datetime import (datetime,
                      date,
                      timedelta)

now = datetime.now()  # 获取当前（系统）时间
print(date.today())
print(now)

time_01 = datetime(1985, 10, 27, 12, 0, 0)
time_02 = datetime(2024, 5, 1, 23, 50, 45)
date_elapsed = time_02 - time_01

print(type(date_elapsed))
print(date_elapsed)

print(f'相差：{date_elapsed.days} 天')
print(f'纯秒差：{date_elapsed.seconds} 秒')  # 纯秒差
print(f'相差：{date_elapsed.total_seconds()} 秒')  # 秒数
print(f'相差：{date_elapsed.total_seconds() / 3600:.2f} 小时')  # 小时数
print(f'相差：{date_elapsed.total_seconds() / 60} 分钟')  # 分钟数
print()

# 格式化时间
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.strftime('%Y/%m/%d %H:%M:%S'))
print(now.strftime('%Y年%m月%d日（全年的第%j天） %a（%A） %b（%B） 星期%w 全年第%U周 %H时%M分%S秒'))
print()

# 将输入的字符串时间转换为datetime对象
input_str = input('请输入时间（格式：2024-05-01 23:50:45）：')
input_time = datetime.strptime(input_str, '%Y-%m-%d %H:%M:%S')  # p：parse
print(input_time)

input_str_01 = input('请请输入时间（格式：YYYY-mm-dd HH:MM:SS）')
input_str_02 = input('请请输入时间（格式：YYYY-mm-dd HH:MM:SS）')
time_03 = datetime.strptime(input_str_01, '%Y-%m-%d %H:%M:%S')
time_04 = datetime.strptime(input_str_02, '%Y-%m-%d %H:%M:%S')
print(time_04 - time_03)
