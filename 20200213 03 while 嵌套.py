# while 嵌套

# while 嵌套语法：
# while 条件 1:
#   while 条件 2:
#       print(条件 2 成立执行的代码)
#   print(条件 1 成立执行的代码)


# 家庭惩罚套餐

i_one = 1

while i_one <= 3:
    i_two = 1
    while i_two <= 3:
        print(f"第{i_two}遍：媳妇，我错了！")
        i_two += 1
    print("表现还可以，滚去刷碗吧！")
    print("本套惩罚结束了！")
    i_one += 1

# 1.打印正方形(星号)

# 1.1简单方法

print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)

# 1.2嵌套方法
# 五行星星

column = 0

while column < 5:
    row = 0
    while row < 5:  # 重复 5 次打出单个 *
        print("*", end="")  # 打出单个 *，且不换行
        row += 1  # 子循环增量为 1
    print()  # 实现换行，print()自带默认换行
    column += 1  # 父循环增量为 1

# 2.打印三角形(星号)
# 每行星星的个数和行号相等

# 2.1 方法一
row = 1

while row <= 5:
    print("*" * row)  # 每一行打印的星星和行数是一致的

    row += 1

print()

# 2.2 方法二
row = 1  # 定义行的计数

while row <= 5:  # 五行星星

    col = 1  # 定义列的计数
    while col <= row:  # 行数的星星个数与列上的星星个数一致
        print("*", end="")  # 输出星星，去掉换行

        col += 1  # 定义列的计数器
    print("")  # 在每行星星输出后，在结尾添加换行

    row += 1  # 定义行的计数器
print()

# 2.3 方法三
column = 0

while column < 5:
    row = 0
    while row <= column:  # 每行 * 的个数，该数字和行号相等
        print("*", end="")  # 打出单个 *，且不换行
        row += 1  # 子循环增量为 1
    print()  # 实现换行，print()自带默认换行
    column += 1  # 父循环增量为 1
print()

# 九九乘法表

# 方法一
row = 1

while row <= 9:

    col = 1
    while col <= row:
        print(f"{row} * {col} = {row * col}", end="\t")

        col += 1

    print("")

    row += 1
print()

# 方法二

"""
1.打印一个表达式：x * x = x
2.一行打印多个表达式：一行表达式的个数和行数相等 --- 循环:一个表达式 -- 不换行
3.打印多行表达式 --- 循环：一行表达式
4.注意事项：一行表达式的个数和行数相等
"""

column = 1

while column <= 9:
    # 一行表达式开始
    row = 1
    while row <= column:  # 一行打出多 (9) 个表达式, 行和列要有联动关系
        print(f"{row} * {column} = {row * column}", end="\t")  # 打出一个表达式，且不换行，\t：制表符
        row += 1  # 一行内的的增量为 1
    # 一行表达式结束
    print()  # 强制换行
    column += 1
