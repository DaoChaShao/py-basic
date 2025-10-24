
# 信息输入

# input("内容")

# 当程序执行到input，等待用户输入后，输入完成之后才继续向下执行
# 在PY中，input接受用户输入后，一般存储到变量，方便使用
# 在PY中，input会把接收到的任意用户输入都当做字符(string)处理


password = input("请输入您的密码：")
print(f"您输入的密码是：{password}")
print()
print(type(password))
print()




# 转换数据类型

# int(x, [base]) - 将 x 转换为一个整数
# float(x) - 将 x 转换为一个浮点数
# str(x) - 将 x 转换为字符串
# eval(str) - 用来计算在字符串中的有效PY表达式，并返回一个对象
# tuple(s) - 将序列 s 转换为一个元组
# list(s) - 将序列 s 转换为一个列表

"""
流程：

1. 键入：input
2. 检测input数据类型str
3. int() 转换数据类型
4. 检测是否转换成功
"""

# 1.int()
num = input("请输入数字：")
print(num)
print()
print(type(num)) #str
print()
print(type(int(num))) #int
print()

# 2.float()
num = 1
str_one = "10"

print(float(num)) # 1.0
print()
print(type(float(num)))
print()

print(float(str_one)) # 10.0
print()
print(type(float(str_one)))
print()

# 3.str()
print(str(num))
print()
print(type(str(num)))
print()

# 4.tuple() * 元组是小括号，序列是中括号
list_one = [10, 20, 30]

print(tuple(list_one))
print()
print(type(tuple(list_one)))
print()

# 5.list()
tuple_one = (100, 200, 300)

print(list(tuple_one))
print()
print(type(list(tuple_one)))
print()

# 6.eval() * 转换的必须是字符串
# - 将字符串 当成 有效的表达式 来求值 并 返回计算结果

# 6.1 基本的数学计算
variable = eval("1 + 1")
print(variable) # 输出：2
print()

# 6.2 字符串重复
lines = eval("'*' * 27")
print(lines) # 输出：***************************
print()

# 6.3 将字符串转换为数字
str_two = "1"
str_three = "1.1"

print(eval(str_two)) # 输出：1
print()
print(type(eval(str_two))) # 输出：<class 'int'>
print()

print(eval(str_three)) # 输出：1.1
print()
print(type(eval(str_three))) # 输出：<class 'float'>
print()

# 6.4 将字符串转换为元组
str_four = "(1000, 2000, 3000)"

print(eval(str_four)) # 输出：(1000, 2000, 3000)
print()
print(type(eval(str_four))) # 输出：<class 'tuple'>
print()

# 6.5 将字符串转换为列表
str_five = "[1000, 2000, 3000]"

print(eval(str_five)) # 输出：[1000, 2000, 3000]
print()
print(type(eval(str_five))) # 输出：<class 'list'>
print()

# 6.6 将字符串转换为字典
str_six = "{'name':'Jerry','age':18}"

print(eval(str_six)) # 输出：{'name': 'Jerry', 'age': 18}
print()
print(type(eval(str_six))) # 输出：<class 'dict'>
print()

# 6.7 案例演练

input_str = input("请输入一道算术题：")
    # 输入：(2 + 5) * 8

print(eval(input_str))
    # 输出：56
print()

# 6.8 注意事项
# - 在开发时，不要用 eval() 直接转换 input() 的结果
# -- 可以在 input 的输入窗口，通过调用函数内部方法，修改内置文件或目录
# -- 内部函数距离：__import__('os').system('ls')
# --- 确认后，可以显示向前目录下的所有后台文件
