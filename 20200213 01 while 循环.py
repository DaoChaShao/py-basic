# while 循环

# 引入
# print("女朋友，我错了！" * 100)

# while 语法
# while 条件:
#   条件成立重复执行的代码 1
#   条件成立重复执行的代码 2
#   处理计数器

# 人类写法
times = 1

while times <= 5:
    print("媳妇，我错了！")
    times += 1

print("行了，原谅你了")

# 计算机写法
times = 0

while times < 5:
    print("媳妇，我错了！")
    times += 1

print("行了，原谅你了")

# 1-100累加

"""
1. 准备数字： 1 - 100
2. 准备变量，保存将来的结果
3. 循环做加法运算
4. 打印结果
5. 验证结果正确性
"""

# 如果是求:1 + 2 + 3 + 4 + 5的结果

# 计算机思维：求5个数，实际上就是 + 5 次
# num(resule - 变量的基础定义值) + times = result
# 0                           + 1     = 1
# 1                           + 2     = 3
# 3                           + 3     = 6
# 6                           + 4     = 10
# 10                          + 5     = 15

times = 1
result = 0

while times <= 5:
    result = result + times  # result += times
    times += 1

print(result)  # 输出5050 (5的累加，输出：15)

# 如果是求:1 + 2 + 3 + 4 + 5的结果

# 根据计算机推导的人类(我)的思维：求5个数，实际上 + 4 次
# num(resule - 变量的基础定义值) + times = result
# 1                           + 2     = 3
# 3                           + 3     = 6
# 6                           + 4     = 10
# 10                          + 5     = 15

times = 2
result = 1

while times <= 5:
    result = result + times  # result += times
    times += 1

print(result)  # 输出5050 (5的累加，输出：15)

# 如果是求:1 + 2 + 3 + 4 + 5的结果

# 人类(我)的思维：求5个数，实际上 + 4 次  (?????)
# num(resule - 变量的基础定义值) +       = result     times
# 1                           + 2     = 3          1
# 3                           + 3     = 6          2
# 6                           + 4     = 10         3
# 10                          + 5     = 15         4

times = 1
result = 1
num = 5

while times <= (num - 1):
    result = result + times  # result += times
    times += 1

print(result)  # 输出5050 (5的累加，输出：15)

# 100以内的偶数累加
# 思路：
# 1. %2 除2取余为0
# 2. 数与数之间的增量为2

# 方法一
times = 1  # 数值的起始值为 1 (第 1 次)
result = 0

while times <= 100:  # 循环 100 以内的数
    if times % 2 == 0:  # 筛选 100 以内的偶数(思路 1)
        result += times  # 加法运算 (times 是满足%2)
    times += 1  # 数与数之间的增量为 1

print(result)  # 输出2550

