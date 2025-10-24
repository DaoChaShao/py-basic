
# 数据类型

# 1.数据输入
# - 语法：变量名称 = 赋值

# 定义一个变量 - 记录 QQ 号码
qq_num = "1234567"

# 定义一个变量 - 记录 QQ 密码
qq_password = "123"


# 2.数据输出

# 如果希望通过解释器的方式，输出变量的内容，需要使用 print() 函数
print(qq_num) # 输出：1234567
print(qq_password) # 输出：123
print()

# 3.键盘输入(input()函数)

#input("请输出银行密码：") 输出：123<class 'int'>
password = input("请输出银行密码：")
print(password)
print()

# 4.案例体验

# 苹果定价
price = 8.5
# 苹果重量
weight = 7.5
# 苹果总价
money = price * weight

print(money) # 输出：63.75
print()

# 买苹果，返5元
money = money - 5

print(money) # 输出：58.75
print()

# 5.数据类型
# - 定义变量时，不需要指定变量的类型
# - 运行变量是，解释器会根据赋值语句等号右侧的数据，自动推导变量保存数据时的准确类型

name = "小明"
age = 18 # 18岁
gender = True # 是 一个男生
height = 1.75 # 1.75米
weight = 75 # 75公斤

print(name) # 输出：小明
print(type(name)) # 输出：<class 'str'>
print(age) # 输出：18
print(type(age)) # 输出：<class 'int'>
print(gender) # 输出：True
print(type(gender)) # 输出：<class 'bool'>
print(height) # 输出：1.75
print(type(height)) # 输出：<class 'float'>
print(weight) # 输出：75
print(type(weight)) # 输出：<class 'int'>
print()

number_1 = 1
number_2 = 2 ** 64
number_3 = 1.1
phrase_1 = "hello world"
bool_1 = True # Ture = 1, False = 0
list_1 = [10, 20, 30]
tuple_1 = (10, 20, 30)
set_1 = {10, 20, 30}
dict_1 = {"name": "tom", "age": 18}

print(type(number_1))  # 输出：<class 'int'> - 整型
print(type(number_2))  # 输出：<class 'int'> - 长整型 (PY3.0 前为：long)
print(type(number_3))  # 输出：<class 'float'> - 浮点
print(type(phrase_1))  # 输出：<class 'str'> - 字符串
print(type(bool_1))  # 输出：<class 'bool'> - 布尔
print(type(list_1))  # 输出：<class 'list'> - 列表
print(type(tuple_1))  # 输出：<class 'tuple'> - 元组
print(type(set_1))  # 输出：<class 'set'> - 集合
print(type(dict_1))  # 输出：<class 'dict'> - 字典--键值对
print()

# 6.数据转换 (详细的在第 005 课)
# - 6.1 int() - 整数转换
# - 6.2 float() - 小数转换

info = "123"

print(info) # 输出：123
print(type(info)) # 输出：<class 'str'>
print()

print(int(info)) # 输出：123
print(type(int(info))) # 输出：<class 'int'>
print()

print(float(info)) # 输出：123.0
print(type(float(info))) # 输出：<class 'float'>
print()

# - 6.3 案例体验
# -- 字符串之间不可以进行乘法计算

price_str = input("请输入苹果的单价：") # 输入：7.4
price = float(price_str) # 将价格转换为小数

weight_str = input("请输入苹果的重量：") # 输入：6.5
weight = float(weight_str) # 将价格转换为小数

money = price * weight

print(money) # 输出：48.1
print(type(money)) # 输出：<class 'float'>
print()
