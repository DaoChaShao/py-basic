# 函数

# 1.函数的作用
# - 将 一段具有独特功能的代码块 整合到一个整体并命名，在需要的位置 调用这个名称 即可完成对应的需求
# - 在开发的过程汇总，可以更高效的实现 代码重用

# - 顺序：先 定义 函数，再 调用 函数 - 否则会报错
# - 函数调用流程： 调用时，回到定义函数地方，执行缩进的代码 - 定义函数时，函数定义时的缩进代码并没有执行

# - 定义函数的语法：
#       def 函数名(参数)： - 不同需求中，参数可有可无
#           代码 1
#           代码 2
#           ···

# - 调用函数的语法：
#       函数名(参数)

# 2.案例体验 - 需求复现ATM取钱功能

# 2.1 框架搭建

"""
 - 密码正确登陆 - print("恭喜您登陆成功")
 - 显示“功能界面”
 - 查询余额完毕 - print("您的余额为：100000000")
 - 显示“功能界面”
 - 取款成功 - print("您取了：100 元")
 - 显示“功能界面”
"""

# 2.2 确定功能界面内容

"""
 - 查询余额 - print("显示余额")
 - 存款 - print("存款")
 - 取款 - print("取款")
"""


# 2.3 封装函数

def sel_func():  # 定义函数：仅表示函数封装了一段代码而已
    print("显示余额")
    print("存款")
    print("取款")


# 2.4 在需要的位置调用函数

print("恭喜您登陆成功")  # 非 def 缩进内的代码，不受 def 限制
sel_func()  # 调用函数：如果不主动调用，函数是不会主动运行的
print()

print("您的余额为：100000000")
sel_func()  # 调用函数：如果不主动调用，函数是不会主动运行的
print()

print("您取了：100 元")
sel_func()  # 调用函数：如果不主动调用，函数是不会主动运行的
print()


# 3.函数的参数作用

# - 让函数变得更加灵活，实现互动


# 3.1 一个函数完成两个数 1 和 2 的加法运算 (固定数字)

# 定义函数
def add_num1():
    result = 1 + 2
    print(result)


# 调用函数
add_num1()


# 常规写法
def sum_2_num():
    """两个数求和"""

    num_1 = 10
    num_2 = 20

    result = num_1 + num_2

    print(f"{num_1} + {num_2} = {result}")


sum_2_num()
print()


# 形参和实参写法
def sum_two_num(num_1, num_2):
    """两个数求和"""

    result = num_1 + num_2

    print(f"{num_1} + {num_2} = {result}")


sum_two_num(10, 20)
print()


# 形参和实参写法 - 进阶
def sum_two_num(num_1, num_2):
    """两个数求和"""

    result = num_1 + num_2

    print(f"{num_1} + {num_2} = {result}")


sum_two_num(int(input("请输入第一个数：")), int(input("请输入第二个数：")))
print()


# 3.2 一个函数完成两个数的加法运算 (非固定数字)

# 定义函数时，同时定义了接受用户数据的参数 a 和 b，a 和 b 是形式参数 (形参)
def add_num2(a, b):
    result = a + b
    print(result)


# 调用函数时，传入了真实的数据 10 和 20，真实数据为实际参数 (实参)
add_num2(10, 20)
print()


# 4.函数的返回值和返回值的作用
# - 在函数中，如果需要返回结果给用户，就需要使用函数的返回值

def buy():
    return ("烟")
    # - 负责返回值
    # - 退出当前函数：导致 return 下方的的所有 (函数体内部) 的代码 不执行
    print("OK")  # 不输出任何结果


# 使用变量保存函数返回值
goods = buy()
print(goods)  # 输出：烟
###print(buy())
print()


# 5.应用 - 返回值

def sum_num(a, b):
    return a + b


result = sum_num(1, 2)
print(result)
print()


# 形参和实参写法 - 进阶
def sum_two_num(num_1, num_2):
    """两个数求和 - 返回值"""

    result = num_1 + num_2
    return result


sum_result = sum_two_num(int(input("请输入第一个数：")), int(input("请输入第二个数：")))
# 这部分为调用函数，并让 sum_result 存储函数调用的值
# 顶格写是因为存储值和函数定义没有关系

print(f"两个数之和为：{sum_result}")
print()


# 形参和实参写法 - 进阶
def sum_two_num(num_1, num_2):
    """两个数求和 - 返回值"""

    return num_1 + num_2  # 合并以上的两行代码


sum_result = sum_two_num(int(input("请输入第一个数：")), int(input("请输入第二个数：")))
# 这部分为调用函数，并让 sum_result 存储函数调用的值
# 顶格写是因为存储值和函数定义没有关系

print(f"两个数之和为：{sum_result}")
print()

# 6.函数的说明文档

# 6.1 注释

# 6.2 函数的说明文档 (文档说明)

# 6.2.1 内置函数的函数说明文档

help(len)


# - help() 查看函数的说明文档 (函数的说明的信息)
# - 输出：Help on built-in function len in module builtins:
#
# len(obj, /)
# Return the number of items in a container.

# 6.2.2 自定义函数的函数说明文档
# - 语法：def 函数(参数):
#       """ 说明文档的位置"""
#       代码 1
#       代码 2
#       ···

def sum_num(a, b):
    """求和函数"""
    return a + b


help(sum_num)  # help(函数名)


# 6.3 函数说明文档的高级使用

def sum_num1(a, b):  # 在 Param 中，文档里直接 回车，文档会被分段，类似以下内容：
    """
    求和函数sum_num1 - 空
    :prarm a：参数 1 - :prarm a：
    :prarm b：参数 2 - :prarm b：
    :return：返回值  - :return：
    """
    return a + b


help(sum_num1)
