
# 字典的遍历

# 1. .keys() 的遍历

dict_one = {"name": "tom", "age" : 20, "gender" : "男"}

for key in dict_one.keys():
    print(key)
    # 输出：name
    #      age
    #      gender
print()

for k in dict_one.keys():
    print(k)
    # 输出：name
    #      age
    #      gender
print()

for key in dict_one:
    print(key)
    # 输出：name
    #      age
    #      gender
print()


# 自我拓展
i = 0

key = dict_one.keys()

while i < len(dict_one):
    print(tuple(key)[i])

    i += 1
print()


# 2. .values() 的遍历

dict_one = {"name": "tom", "age" : 20, "gender" : "男"}

for value in dict_one.values():
    print(value)
    # 输出：tom
    #      20
    #      男
print()


# 自我拓展
i = 0

value = dict_one.values()

while i < len(dict_one):
    print(tuple(value)[i])

    i += 1
print()


# 3. .items() 的遍历 - 遍历字典的元素
# -- 里面的数据是类型是元组，元组1是字典的 key，元组2是字典的 value

dict_one = {"name": "tom", "age" : 20, "gender" : "男"}

for item in dict_one.items():
    print(item)
    # 输出：('name', 'tom')
    #      ('age', 20)
    #      ('gender', '男')
print()


# 自我拓展
i = 0

item = dict_one.items()

while i < len(dict_one):
    print(tuple(item)[i])

    i += 1
print()


# 4.遍历字典的 键值对 - 俗称：拆包

dict_one = {"name": "tom", "age" : 20, "gender" : "男"}

for key, value in dict_one.items(): # 元组内有2个参数，所以可以有两个临时变量
    print(f"{key} = {value}")
    # 输出：name = tom
    #      age = 20
    #      gender = 男
print()


# 自我拓展一
dict_one = {"name": "tom", "age" : 20, "gender" : "男"}

for key in dict_one:
    print(f"{key} ~ {dict_one[key]}")
        # 输出：name ~ tom
        #      age ~ 20
        #      gender ~ 男

# 自我拓展二
i = 0

while i < len(dict_one):
    key = tuple(dict_one.keys())[i]
    value = tuple(dict_one.values())[i]
    print(f"{key} = {value}")

    i += 1
print()

print()

# 自我拓展 三
# 把多个字典放在一个列表中，再进行遍历

card_list = [
    {"name":"张三",
     "qq":"12345",
     "phone":"110"},
    {"name":"李四",
     "qq":"67890",
     "phone":"10086"}
    ]

for card_info in card_list:

    print(card_info)
