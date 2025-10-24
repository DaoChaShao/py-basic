# for 循环

# 1.for 循环语法
# for 临时变量 in 序列:
#   重复执行的代码 1 (注意tap缩进)
#   重复执行的代码 2 (注意tap缩进)
#   ······

# 体验案例

str_one = "PYTHON"
for i in str_one:
    print(i)
    # 输出：P
    #      Y
    #      T
    #      H
    #      O
    #      N
print()

"""
1.准备一个序列
2.for
"""

str_two = "YONG"

for i in str_two:
    print(i)
    # 输出：Y
    #      O
    #      N
    #      G
print()

# 2.完整 for 循环
# - for 部分循环完毕后，执行 else 中的代码
# - 如果 for 部分有 break，不执行 else 中的代码
# - 语法：
#       for 变量 in 集合:
#           循环体代码
#       else:
#           没有通过 break 退出循环，循环结束后，会执行的代码

# 2.1 for 循环
for i in [1, 2, 3]:
    print(i)

print("循环结束")
# 输出：1
#      2
#      3
#      循环结束
print()

# 2.2 for-else 循环
for i in [1, 2, 3]:

    print(i)

else:
    print("循环结束后，会执行么？")

print("循环结束")
# 输出：1
#      2
#      3
#      循环结束后，会执行么？
#      循环结束
print()

# 2.3 for-break-else 循环
for i in [1, 2, 3]:

    print(i)

    if i == 2:
        break

else:
    print("循环结束后，会执行么？")

print("循环结束")
# 输出：1
#      2
#      循环结束
print()

# 3.循环案例 - 查找人物

# 基础
students = [
    {"name": "阿土"},
    {"name": "小美"},
    {"name": "春丽"}
]
target_name = "小美"  # 想要查找的姓名

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == target_name:
        # 如果字典中的姓名和查找人姓名一致

        print()
        print(f"我们找到：{target_name}")
        # 输出：{'name': '阿土'}
        #
        #      我们找到：阿土 - 找到了
        #      {'name': '小美'} - 但是继续遍历后面的数据

print()
print("查看结束！")
print()

# 升级 - 不需遍历 无效 数据
students = [
    {"name": "阿土"},
    {"name": "小美"},
    {"name": "春丽"}
]
target_name = "小美"  # 想要查找的姓名

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == target_name:
        # 如果字典中的姓名和查找人姓名一致

        print()
        print(f"我们找到：{target_name}")

        # 如果已经找到，应该直接退出循环，而不再遍历后面的内容
        break

        # 输出：{'name': '阿土'}
        #
        #      我们找到：阿土

print()
print("查看结束！")
print()

# 进阶 - 查找不存在人物
students = [
    {"name": "阿土"},
    {"name": "小美"},
    {"name": "春丽"}
]
target_name = "王哥"  # 想要查找的姓名

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == target_name:
        # 如果字典中的姓名和查找人姓名一致

        print()
        print(f"我们找到：{target_name}")

        # 如果已经找到，应该直接退出循环，而不再遍历后面的内容
        break

        # 输出：{'name': '阿土'}
        #
        #      我们找到：阿土
else:
    print()
    print(f"抱歉！没有找到{target_name}！")

print()
print("查看结束！")
print()
