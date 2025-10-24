
# 1.f"{表达式}"

name = "Tom"
age = 17
weight = 70.5
stu_id = 12

# 1.1 我的名字是x, 今年x (常规3.6写法)
print("我的名字是：%s, 今年：%d岁" % (name, age))
print()

# 1.2 我的名字是x, 今年x岁 (f 写法)
print(f"我的名字是：{name}, 今年：{age}岁")
print()

# 1.3 我的名字是x, 今年x岁,明年x岁 (常规3.6写法)
print("我的名字是：%s, 今年：%d岁, 明年：%d岁" % (name, age, age + 1))
print()

# 1.4 我的名字是x, 今年x岁 (f 写法)
print(f"我的名字是：{name}, 今年：{age}岁, 明年：{age + 1}岁")
print()


# 1.5 我的名字是x, 我今年x岁, 体重是x公斤, 学号是x
print(f"我的名字是：{name}, 我今年：{age}岁, 体重是：{weight}公斤, 学号是：{stu_id}")
print()

# 2. .format()

# 2.1 我的名字是x, 我今年x岁, 体重是x公斤, 学号是x
message = ("我的名字是：{}, 我今年：{}岁, 体重是：{}公斤, 学号是：{}".format(
    name, age, weight, stu_id))

print(message)
print()
