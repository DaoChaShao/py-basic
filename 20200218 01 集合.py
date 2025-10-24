# 集合


# 1.集合基本特点

# 1.1 数据特点
# - 集合是可变类型的数据
# - 集合内的数据不重复，即集合数据有 去重 功能
# - 输出顺序和输入顺序不一致
# - 集合不支持下标

# 1.2 集合形式
# - 创建空集合，只能用 set()
# - {} 用来创建字空字典


# 2.集合的创建

# 2.1 建立已有数据集合

set_one = {10, 20, 30, 40, 50, 60}
set_two = {10, 30, 20, 10, 30, 40, 30, 50}
set_three = set("abcdefg")

print(set_one)  # 输出：{40, 10, 50, 20, 60, 30} - 输出顺序和输入顺序不一致
print(type(set_one))  # 输出：<class 'set'>
print()

print(set_two)  # 输出：{40, 10, 50, 20, 30} - 重复数据没有出现，即 去重
print(type(set_two))  # ：输出:<class 'set'>
print()

print(set_three)  # 输出：{'e', 'f', 'c', 'a', 'g', 'd', 'b'}
print(type(set_three))  # 输出：<class 'str'>
print()

# 2.2 建立空集合

set_four = set()
set_five = {}

print(set_four)  # 输出：set()
print(type(set_four))  # 输出：<class 'set'>
print()

print(set_five)  # 输出：{} - {} 用来创建字空字典
print(type(set_five))  # 输出：<class 'dict'>
print()

# 3.集合常见操作

# 3.1 增加数据

# 3.1.1 .add()
# - 追加的数据是 数据
# - 如果增加的数据是集合中已经存在的，则不进行任何操作 - 去重
# 语法：集合序列.add()

# 追加单一数据
set_one = {10, 20, 30, 40, 50, 60}

set_one.add(100)
set_one.add(100)

print(set_one)  # 输出：{100, 40, 10, 50, 20, 60, 30}
# - 追加数据随机出现在任意位置
# - 没有增加第二个 100 - 集合有去重功能，追加重复数据，则不进行任何操作

print()

# 追加列表
set_one = {10, 20, 30, 40, 50, 60}

###set_one.add([10, 20, 30])

###print(set_one) # 输出：TypeError: unhashable type: 'list'
print()

# 3.1.2 .update()
# - 追加的数据是 序列
# 语法：集合序列.update()

set_one = {10, 20, 30, 40, 50, 60}

set_one.update([10, 20, 70, 80, 90])

print(set_one)  # 输出：{70, 40, 10, 80, 50, 20, 90, 60, 30}
# - 对 已存在数据 不进行 操作
# - 对 不存在数据 进行 操作

###set_one.update(100)

###print(set_one) # 输出：TypeError: 'int' object is not iterable
print()

# 3.2 删除函数

# 3.2.1 .remove()
# - 删除集合中的指定数据，如果数据不存在，则报错
# 语法:集合序列.remove()

# 删除已存在数据
set_one = {10, 20, 30, 40, 50, 60}

set_one.remove(60)

print(set_one)  # 输出：{40, 10, 50, 20, 30}
print()

# 删除不存在数据
set_one = {10, 20, 30, 40, 50, 60}

###set_one.remove(70)

###print(set_one) # 输出：KeyError: 70
print()

# 3.2.2 .discard()
# - 删除集合中的指定数据，如果数据不存，则不会报错
# - 语法：集合序列.discard()

# 删除已存在数据
set_one = {10, 20, 30, 40, 50, 60}

set_one.discard(50)

print(set_one)  # 输出：{40, 10, 20, 60, 30}
print()

# 删除不存在数据
set_one = {10, 20, 30, 40, 50, 60}

set_one.discard(10)
set_one.discard(10)

print()  # 输出： - 空
print()

# 3.2.3 .pop()
# - 随机删除集合中的某个数据，并返回该数据
# 语法：集合序列.pop()

set_one = {10, 20, 30, 40, 50, 60}

del_set = set_one.pop()

print(del_set)  # 输出：40
print(set_one)  # 输出：{10, 50, 20, 60, 30}
print()

# 3.3 查找数据

# 3.3.1 in 判断数据在集合序列
# - 语法：数据 in 集合序列

set_one = {10, 20, 30, 40, 50, 60}

print(10 in set_one)  # 输出：True
print()

# 3.3.2 not in 判断数据不在集合序列
# - 语法：数据 not in 集合序列

set_one = {10, 20, 30, 40, 50, 60}

print(10 not in set_one)  # 输出：False
print()
