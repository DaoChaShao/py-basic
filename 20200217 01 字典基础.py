# 字典

# 体验案例 - 在列表数据中找到 tom (姓名)

list_one = ["tom", 20, "female"]
list_two = ["female", 20, "tom"]

print(list_one[0])  # 输出：tom
print(list_one.index("tom"))  # 输出：0
print(list_one[list_one.index("tom")])  # 输出：tom
print()

print(list_two[0])  # 输出：female - 列表数据变化后，找不到指定列表
print(list_two.index("tom"))  # 输出：2
print(list_two[list_two.index("tom")])  # 输出：tom
# 所以，最终.index()也可以在变动的列表中找到指定数据

print()

# 1.字典的特点和创建

# 1.1 字典的特点
# - 符号为：{} - 集合也是：{}
# - 数据为：键值对 形式出现
#   - 形式：key & value
#   - 语法："name": "tom"
# - 各个键值对之间用 , 隔开 (英文逗号)

# 1.2 字典的创建

# 1.2.1 有数据的字典

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one)  # 输出：{'name': 'tom', 'age': 20, 'gender': '男'}
print(type(dict_one))  # 输出：<class 'dict'>
print()

# 1.2.2 无数据的字典

dict_two = {}
dict_three = dict()

print(type(dict_two))  # 输出：<class 'dict'>
print()

print(type(dict_three))  # 输出：<class 'dict'>
print()

# 2 字典的常见操作

# - 字典是个无序的数据类型
# - 字典为可变类型数据
# - 字典不支持下标

# 2.1 增
# - 语法：字典序列[key] = 值 - [key] = value
# - 如果 key 已存在，则是修改 value
# - 如果 key 不存在，则是增加 value

dict_one = {"name": "tom", "age": 20, "gender": "男"}

# 新增不存在 key， id 为 110
dict_one["id"] = 110

print(dict_one)  # 输出：{'name': 'tom', 'age': 20, 'gender': '男', 'id': 110}
print(type(dict_one))  # 输出:<class 'dict'>
print()

dict_one = {"name": "tom", "age": 20, "gender": "男"}

# 修改已存在 key， tom 改为 jerry
dict_one["name"] = "jerry"

print(dict_one)  # 输出：{'name': 'jerry', 'age': 20, 'gender': '男'}
print(type(dict_one))  # 输出：<class 'dict'>
print()

# 2.2 删 和 改

# 2.2.1 del() 或 del
# - 删除字典或删除字典中指定的键值对
# - 语法：del 字典序列[key]

# 删除字典
dict_one = {"name": "tom", "age": 20, "gender": "男"}

###del(dict_one)

###print(dict_one) # 输出：NameError: name 'dict_one' is not defined
print()

# 删除字典中的键值对
dict_one = {"name": "tom", "age": 20, "gender": "男"}
dict_two = {"name": "tom", "age": 20, "gender": "男"}

del dict_one["gender"]
###del dict_two["ages"]
print()

print(dict_one)  # 输出：{'name': 'tom', 'age': 20}
###print(dict_two) # 输出：KeyError: 'ages'
print()

# 2.2.2 .clear()
# - 清空字典
# - 语法：字典序列.clear()

dict_one = {"name": "tom", "age": 20, "gender": "男"}

dict_one.clear()

print(dict_one)  # 输出：{}
print()

# 2.2.3 .pop()
# - 删除相关键值对

dict_one = {"name": "tom", "age": 20, "gender": "男"}

dict_one.pop("name")

print(dict_one)  # 输出：{'age': 20, 'gender': '男'}
print()

# 2.3 查

# 2.3.1 key 查找
# - 语法：字典序列[key]
# - 如果 key 已存在，则返回 value
# - 如果 key 不存在，则报错

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one["name"])  # 输出:tom
###print(dict_one["names"]) # 输出：KeyError: 'names'
###print(dict_one["id"]) # 输出：KeyError: 'id'
print()

# 2.3.2 函数 .get() 查找
# - 语法：字典序列.get(key, 默认值)
# - 如当前 key 不存在，则返回第二个参数 (默认值)，如省略第二个参数，则返回 None
# -

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one.get("age"))  # 输出：20
print(dict_one.get("ages"))  # 输出：None - 如当前 key 不存在，且省略第二个参数，则返回 None
print(dict_one.get("id", 110))  # 输出：110 - 如当前 key 不存在，则返回第二个参数 (默认值)
print(dict_one.get("id"))  # 输出：None - 如当前 key 不存在，且省略第二个参数，则返回 None
print()

# 2.3.3 函数 .keys() 查找
# - 语法：字典序列.keys()
# - 作用：查找字典中所有的 key，返回 可迭代对象 (可用 for 遍历的对象)

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one.keys())  # dict_keys(['name', 'age', 'gender'])
print()

# 2.3.4 函数 .values() 查找
# - 语法：字典序列.values()
# - 作用：查找字典中所有的 value，返回 可迭代对象

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one.values())  # 输出：dict_values(['tom', 20, '男'])
print()

# 2.3.5 函数 .items() 查找
# - 语法：字典序列.items()
# - 作用：查找字典中所有的 键值对，返回 可迭代对象
# -- 里面的数据是类型是元组，元组1是字典的 key，元组2是字典的 value

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(dict_one.items())  # 输出：dict_items([('name', 'tom'), ('age', 20), ('gender', '男')])
print()

# 2.3.5 函数 len() 统计键值对数量

dict_one = {"name": "tom", "age": 20, "gender": "男"}

print(len(dict_one))  # 输出：3
print()

# 2.3.6 函数 .update() 合并字典 ?????

dict_one = {"name": "tom", "age": 20, "gender": "男"}
temp_dict = {"height": 1.75}

new_dict = dict_one.update(temp_dict)

print(new_dict)  # 输出：3
print()

# 3.随机数测试字典kvp
import random

num = random.randint(1, 3)
num_dict = {1: "石头",
            2: "剪刀",
            3: "布子"}

print(num)
print(num_dict)
print(num_dict[num])
