# 公共符号和公共操作

# 1.运算符

# 1.1 合并 - +
# - 支持容器类型：字符串、列表、元组

str_one = ("小熊", "小呆")
str_two = ("tom", "jerry")

list_one = [1, 2]
list_two = [10, 20]

tuple_one = (1, 2)
tuple_two = (10, 20)

dict_one = {"name": "python"}
dict_two = {"年龄": 30}

print(str_one + str_two)  # 输出：('小熊', '小呆', 'tom', 'jerry')
print(type(str_one + str_two))  # 输出：<class 'tuple'>
print()

print(list_one + list_two)  # 输出：[1, 2, 10, 20]
print(type(list_one + list_two))  # 输出：<class 'list'>
print()

print(tuple_one + tuple_two)  # 输出：(1, 2, 10, 20)
print(type(tuple_one + tuple_two))  # 输出：<class 'tuple'>
print()

###print(dict_one + dict_two) # 输出：TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# dict 不支持 + 的合并运算

print()

# 1.2 复制 - *
# - 支持容器类型：字符串、列表、元组

str_three = ("小熊")

list_three = ["python"]

tuple_three = ("pthhon",)

dict_one = {"name": "python"}

print(str_three * 10)  # 输出：小熊小熊小熊小熊小熊小熊小熊小熊小熊小熊
print(type(str_three * 10))  # 输出：<class 'str'>
print()

print(
    list_three * 10)  # 输出：['python', 'python', 'python', 'python', 'python', 'python', 'python', 'python', 'python', 'python']
print(type(list_three * 10))  # 输出：<class 'list'>
print()

print(
    tuple_three * 10)  # 输出：('pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon', 'pthhon')
print(type(tuple_three * 10))  # 输出：<class 'tuple'>
print()

###print(dict_one * 10) # 输出：TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# dict 不支持 * 的复制运算
print()

# 1.3 成员运算符 - 元素是否存在 - in
# - 支持容器类型：字符串、列表、元组、字典、集合

str_four = ("小熊", "小呆", "tom", "jerry")

list_four = [10, 20, 30, 40]

tuple_four = (100, 200, 300, 400)

dict_four = {"name": "python", "age": 30}

set_one = {"大", "小", "多", "少"}

print("小熊" in str_four)  # 输出：True
print("小花" in str_four)  # 输出：False
print()

print(30 in list_four)  # 输出：True
print(50 in list_four)  # 输出：False
print()

print(400 in tuple_four)  # 输出：True
print(500 in tuple_four)  # 输出：False
print()

print("age" in dict_four)  # 输出：True
print("age" in dict_four.keys())  # 输出：True
print("age" in dict_four.values())  # 输出：False
print("id" in dict_four)  # 输出：False
print()

print(type(set_one))  # 输出：<class 'set'>
print("多" in set_one)  # 输出：True
print("高" in set_one)  # 输出：False
print()

# 1.4 成员运算符 - 元素是否存在 - not in
# - 支持容器类型：字符串、列表、元组、字典、集合

str_four = ("小熊", "小呆", "tom", "jerry")

list_four = [10, 20, 30, 40]

tuple_four = (100, 200, 300, 400)

dict_four = {"name": "python", "age": 30}

set_one = {"大", "小", "多", "少"}

print("小熊" not in str_four)  # 输出：False
print("小花" not in str_four)  # 输出：True
print()

print(30 not in list_four)  # 输出：False
print(50 not in list_four)  # 输出：True
print()

print(400 not in tuple_four)  # 输出：False
print(500 not in tuple_four)  # 输出：True
print()

print("age" not in dict_four)  # 输出：False
print("age" not in dict_four.keys())  # 输出：False
print("age" not in dict_four.values())  # 输出：True
print("id" not in dict_four)  # 输出：True
print()

print(type(set_one))  # 输出：<class 'set'>
print("多" not in set_one)  # 输出：False
print("高" not in set_one)  # 输出：True
print()

# 2.公共方法 - 公共函数

# 2.1 len()
# - 计算容器中元素个数
# - 语法：len(序列)

str_four = ("小熊", "小呆", "tom", "jerry")

list_four = [10, 20, 30]

tuple_four = (100, 200, 300, 400, 500)

dict_four = {"name": "python", "age": 30}

set_one = {"贰货", }

print(len(str_four))  # 输出：4
print()

print(len(list_four))  # 输出：3
print()

print(len(tuple_four))  # 输出：5
print()

print(len(dict_four))  # 输出：2：
print()

print(len(set_one))  # 输出：1
print()

# 2.2 del 或 del()
# - 删除
# - 语法：del 或 del(容器[下标])

str_four = ("小熊", "小呆", "tom", "jerry")

list_four = [10, 20, 30]

tuple_four = (100, 200, 300, 400, 500)

dict_four = {"name": "python", "age": 30}

set_two = {"贰", "货"}

###del(str_four)
###print(str_four) # 输出：NameError：name 'xxx' is not defind
print()

###print(del list_four) # 输出：NameError：name 'xxx' is not defind
del (list_four[0])
print(list_four)  # 输出：[20, 30]
print()

###del(tuple_four)
###print(tuple_four) # 输出：NameError：name 'xxx' is not defind
print()

###print(del dict_four) # 输出：NameError：name 'xxx' is not defind
del (dict_four["name"])
print(dict_four)  # 输出：{'age': 30}
print()

###del(set_two)
###print(set_two) # 输出：NameError：name 'xxx' is not defind
print()

# 2.3 max() 和 mix()
# - 返回容器中元素的最大值
# - 语法：max(容器) 和 min(容器)

str_five = ("abcdefgh")

list_four = [10, 20, 30, 40]

dict_ten = {"a": "z", "b": "y", "c": "x"}

print(max(str_five))  # 输出：h
print(min(str_five))  # 输出：a
print()

print(max(list_four))  # 输出：40
print(min(list_four))  # 输出：10
print()

print(max(dict_ten))  # 输出：c - 仅针对 key 排序，不对 value 排序
print(min(dict_ten))  # 输出：a - 仅针对 key 排序，不对 value 排序
print()

# 2.4 range()
# - 语法：range(start, end, step)
# - 生成从 start 到 end 的数字，步长为 step， 供 for 循环使用
# - end 值 不包含
# - step 不写，则默认为 1
# - start 不写，则默认为 0

# 需求：1 2 3 4 5 6 7 8 9
for i in range(1, 10, 1):
    print(i, end=" ")  # 输出：1 2 3 4 5 6 7 8 9
print()

# 需求：1 3 5 7
for i in range(1, 8, 2):
    print(i, end=" ")  # 输出:1 3 5 7
print()

# 需求:0 1 2 3 4 5 6 7 8 9
for i in range(0, 10, 1):  # 也可以写成：for i in range(10):
    print(i, end=" ")  # 输出：0 1 2 3 4 5 6 7 8 9
print()

# 2.5 enumerate()
# - 用于将一个可遍历的数据对象 (如：列表、元组或字符串) 组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环中
# - 语法：enumerate(可遍历对象, start = 0)
# - 注意：start 参数用来设置 遍历数据 的下标起始值，默认为 0

list_se7en = ["a", "b", "c", "d", "e", "f"]

for i in enumerate(list_se7en):  # enumerate 返回的结果是元组 (tuple)
    print(i)  # 输出：(0, 'a')
    #      (1, 'b')
    #      (2, 'c')
    #      (3, 'd')
    #      (4, 'e')
    #      (5, 'f')
    #      下标 数据
    # 元组第一格数据是：原迭代数据对应的下标， 第二个数据是：原迭代数据

print()

for i in enumerate(list_se7en, start=2):  # 原迭代数据的下标初始值被重新 定义更改
    print(i)  # 输出：(2, 'a')
    #      (3, 'b')
    #      (4, 'c')
    #      (5, 'd')
    #      (6, 'e')
    #      (7, 'f')

print()

# 3.容器类型转换

# 3.1 tuple() - 将某个序列转换成元组

list_eight = [10, 20, 30, 20, 40, 50]

tuple_eight = ("a", "b", "c", "d", "e")

set_eight = {100, 300, 200, 400}

print(tuple(list_eight))  # 输出：(10, 20, 30, 20, 40, 50)
print(type(tuple(list_eight)))  # 输出：<class 'tuple'>
print()

print(tuple(set_eight))  # 输出：(200, 100, 400, 300)
print(type(tuple(set_eight)))  # 输出：<class 'tuple'>
print()

# 3.2 list() - 将某个序列转换成列表

list_eight = [10, 20, 30, 20, 40, 50]

tuple_eight = ("a", "b", "c", "d", "e")

set_eight = {100, 300, 200, 400}

print(list(tuple_eight))  # 输出：['a', 'b', 'c', 'd', 'e']
print(type(list(tuple_eight)))  # 输出：<class 'list'>
print()

print(list(set_eight))  # 输出：[200, 100, 400, 300]
print(type(list(set_eight)))  # 输出：<class 'list'>
print()

# 3.3 set() - 将某个序列转换成集合

list_eight = [10, 20, 30, 20, 40, 50]

tuple_eight = ("a", "b", "c", "d", "e")

set_eight = {100, 300, 200, 400}

print(set(list_eight))  # 输出：{40, 10, 50, 20, 30}
print()

print(set(tuple_eight))  # 输出：{'d', 'e', 'c', 'b', 'a'}
print()
