
# 推到式 (或称为 生成式
# 目的：为了简化代码
# 适用范围：列表、字典和集合
# 比较有风格的函数书写表达方式


# 列表推导式
# - 用一个表达式创建一个 有规律的列表 或 控制一个有规律的列表

# 1.体验案例 - 需求创建一个 0-10 的列表

# 1.1 while (非推导式)

# 准备空列表
list_one = []

# 书写循环，准备数字
i = 0

while i <= 10:
    list_one.append(i) # 往列表里面添加数字

    i += 1

# 输出列表
print(list_one) # 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1.2 for (非推导式)

list_two = []

for i in range(11):
    list_two.append(i)

print(list_two) # 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1.3 列表 推导式

list_three = [i for i in range(11)]
    # - 第一个 i 是整个列表推导式里面要返回的数据，即 i 作为返回值
    # - 第二个 i 是 range(11) 里面所取的数据
    # - 第二个 i 的数据将返回第一个 i

print(list_three) # 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2 带 if 的列表推导式 - 需求：创建 0-10 的偶数列表

# 思路一：
list_four = [i for i in range(0, 11, 2)]

print(list_four) # 输出：[0, 2, 4, 6, 8, 10]

list_add_one = []

for i in range(11): # 传统写法
    if i % 2 == 0:
        list_add_one.append(i)

print(list_add_one) # 输出:[0, 2, 4, 6, 8, 10]


# 思路二：
list_five = [i for i in range(11) if i % 2 == 0]

print(list_five) # 输出：[0, 2, 4, 6, 8, 10]


# 3 多个 for 循环实现列表推导式
# - 需求：创建列表如下：
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

list_six = [(i, j) for i in range(1, 3) for j in range(3)]

print(list_six) # 输出：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 传统写法分析

list_add_two = [] # 准备一个空列表

for i in range(1, 3): # 准备第一部分数据：1 和 2
    for j in range(3): # 准备第二部分数据： 0， 1， 2
        list_add_two.append((i, j)) # 准备往空列表里面添加元组，元组 ()

print(list_add_two) # 输出：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 多 for 的列表推导式等同于 for 循环嵌套


# 4 字典推导式
# - 作用：快速合并列表为字典 或 提取字典中目标数据

# 4.1 创建一个字典：字典 key 是 1-5 数字，value是这个数字的 2 次方

dict_one = {i : i ** 2 for i in range(1, 6)}

print(dict_one) # 输出：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 4.2 快速合并列表为字典

list_one = ["name", "age", "gender"]
list_tow = ["tom", "30", "man"]

dict_one = {list_one[i] : list_tow[j] for i in range(len(list_one))}
    # - 如果长度一致，那么统计谁的长度都可以
    # - 如果长度不一致，那么统计长的，则会报错
    # - 如果长度不一致，那么统计短的，则不会报错

print(dict_one) # 输出：{'name': 'man', 'age': 'man', 'gender': 'man'}


# 4.3 提取字典中目标数据 - 需求电脑数量 大于等于 200 的字典数据

count = {"mbp" : 268, "hp" : 125, "dell" : 201, "lenovo" : 199, "acer" : 99}

count_one = {key : value for key, value in count.items() if value >= 200}

print(count_one) # 输出：{'mbp': 268, 'dell': 201}

# 5.集合推导式 - 需求：常见一个集合，数据为下方列表的 2 次方

list_one = [1, 1, 2]

set_one = {i ** 2 for i in list_one}

print(set_one) # 输出：{1, 4} - 去重
