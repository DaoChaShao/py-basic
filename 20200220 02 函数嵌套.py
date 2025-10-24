# 函数的嵌套 和 应用

# 1.函数的嵌套

def testB():  # 4、回到 函数B 定义的部分后，执行缩进代码
    print("--- testB start ---")
    print("这里是testB函数执行的代码")
    print("--- testB end ---")


def testA():  # 2、回到 函数A 定义的部分后，执行缩进代码
    print("--- testA start ---")
    testB()  # 3、调用 函数B ，且回到 函数B 的定义部分
    print("--- testA end ---")  # 5、调用完被嵌套的 函数B 后，执行 函数A 的剩余代码


testA()  # 1、先调用 函数A ，且回到 函数A 的定义部分
# 输出:
# --- testA start ---
# --- testB start ---
# 这里是testB函数执行的代码···(省略)···
# --- testB end ---
# --- testA end ---

print()


# 2.函数的应用 - 应用案例

# 2.1 打印图形

# 2.1.1 打印一条横线

def print_line():  # 定义函数的 名称
    print("-" * 20)  # 定义函数的 内容


print_line()  # 调用函数
# 输出：--------------------

print()


# 应用
def test_one():
    """打印 *"""

    print("*" * 15)  # 执行 1 的执行内容 和 执行 3 的执行内容


test_one()  # 执行 1
print()


# 形参和实参写法 - 进阶
def test_two():
    """打印 -"""

    print("-" * 15)  # 执行 2 的执行内容

    test_one()  # 执行 3

    print("+" * 15)  # 执行 4


test_two()  # 执行 2
print()


# 2.1.2 打印多条横线

# 单纯打印分隔线
def print_line_one():
    """使用 * 打印分隔线"""

    print("*" * 15)


print_line_one()
print()


# 使用任意字符打印分隔线
def print_line_two(char):
    """使用任意字符打印分隔线"""

    return char * 15


print_line_char = print_line_two(input("请输入打印分割线的字符："))
print(print_line_char)
print()


# 使用任意字符和打印任意次数的分隔线
def print_line_three(char, times):
    """使用任意字符打印分割线"""

    return char * times


print_line_char_times = print_line_three(input("请输入打印分割线的字符："), int(input("请输入打印分割线的次数：")))
print(print_line_char_times)
print()


# 分隔线需要打五行，且需要满足上一个分隔线的打印需求 - 嵌套
def print_line_four(char, times):
    """使用任意字符打印分割线"""

    print(char * times)


def print_line_five(char, times):
    """每行使用任意字符打印任意次数的分隔线，需打 5 行"""

    row = 0
    while row < 5:
        print_line_four(char, times)

        row += 1


print_line_five(input("请输入打印分割线的字符："), int(input("请输入打印分割线的次数：")))
print()


# 嵌套打印分隔线
def print_one_line():
    print("-" * 5)


def print_lines(num):  # 定义外套的函数名称，并定义参数 - 形参
    i = 0
    while i < num:
        print_one_line()
        i += 1


print_lines(5)
# -----
# -----
# -----
# -----
# -----

print()


# 2.2 函数计算

# 2.2.1 求三个数值和

def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)

print(result)  # 6


# 2.2.2 求三个数的平均值

def average_num(a, b, c):
    sumResult = sum_num(a, b, c)  # 先求和
    return sumResult / 3


average_result = average_num(1, 2, 3)
print(average_result)  # 2.0
print()
