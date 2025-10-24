
# 转义字符(反斜杠)
# \n：换行
# \t：制表符，一个tab(4个空格 - 8个字符)的距离

# 常规写法
print("hello") # 输出：hello
print("python") # 输出：python

# 转义字符写法(\n)
print("hello\npython")
    # 输出：hello
    #      python

# 转义字符写法(\t)
print("\thello python") # 输出：	hello python

name = "Tom"
age = 17
weight = 70.5
stu_id = 12

# 1.我的名字是x, 今年x岁 (f 写法)
print(f"我的名字是：{name},\n今年：{age}岁")
    # 输出：我的名字是：Tom,
    #      今年：17岁
print()

# 2.我的名字是x, 今年x岁 (f 写法)
print(f"\t我的名字是：{name},\n\t今年：{age}岁,\n\t明年：{age + 1}岁")
    # 输出：	我的名字是：Tom,
    #	        今年：17岁,
    #	        明年：18岁
print()

# print结束符
# print("输出内容"， end = "\n")
# print("输出内容"， end = "") - end = "" = end = "\n" - 默认取消换行

#常规写法
print("hello")
print("python")
print("hello")
print("python")
    # 输出：hello
    #      python
    #      hello
    #      python
print()

#结束符写法(\n)
print("hello", end = "\n")
print("python", end = "\n")
print("hello", end = "\n")
print("python", end = "\n")
    # 输出：hello
    #      python
    #      hello
    #      python
print()

#结束符写法(\t)
print("hello", end = "\n")
print("python", end = "\t")
print("hello", end = "\n")
print("python", end = "\n")
    # 输出：hello
    #      python	hello
    #      python
print()

#其他结束符号(例:···)
print("hello", end = "\n")
print("python", end = "\t")
print("hello", end = "···")
print("python", end = "\n")
    # 输出：hello
    #      python	hello···python
print()
