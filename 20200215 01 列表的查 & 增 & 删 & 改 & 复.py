# 列表

# 列表格式：[数据1, 数据2, 数据3, 数据4, 数据5, ···]
# - 可以存放不同类型的数据在同一个列表里
# - 尽可能将同一种类型的列表存放在一个列表里，便于操作 (未来职业)

# 列表的常用操作：查、增、删、改

# 1 查找

# 1.1 下标: 在列表中，每个单独数据为一个下标

name_list_one = ["小熊", "小呆", "小虎", "小萌"]
              #    0      1       2      3

print(name_list_one)
print(name_list_one[0])  # 输出：小熊
print(name_list_one[3])  # 输出：小萌
print(name_list_one[-1])  # 输出：小萌（倒数第一个）
print()

# 1.2 函数

# 1.2.1 .index()
# - .index()：返回指定数据所在的未知的下标
# - 语法：列表序列.index(数据, 开始位置下标, 结束位置下标)

name_list_two = ["小熊", "小呆", "小虎", "小萌"]
#    0      1       2      3

print(name_list_two.index("小呆"))  # 1
# print(name_list_two.index("小呆呆"))
# - 查找列表中不存在的数据，则：ValueError: '小呆呆' is not in list
print()

# 1.2.2 .count()
# - .count()：统计指定数据在当前列表中出现的次数
# - 语法：列表序列.count(数据)

name_list_three = ["小熊", "小呆", "小虎", "小萌", "小虎", "小熊", "小熊"]

print(name_list_three.count("小熊"))  # 3
print(name_list_three.count("小虎"))  # 2
print(name_list_three.count("小熊熊"))  # 0，查找列表中不存在的数据，显示 0
print()
name_list_three.append('小猪')
print(name_list_three)
name_list_three.insert(3, '小鸡')
print(name_list_three)
del name_list_three[3]  # 删除列表中的指定目标
print(name_list_three)
name_list_three.pop(3)  # 删除列表中的指定目标
print(name_list_three)
name_list_three.remove('小虎')  # 删除列表中的指定值
print(name_list_three)

# 1.2.3 len() - 公共函数
# len()：访问列表长度，即列表中数据的个数
# 语法：len(列表序列)

name_list_four = ["小熊", "小呆", "小虎", "小萌", "小熊", "小熊"]

print(len(name_list_four))  # 6
print()

# 1.3 判断存在 (布尔型) - 公共函数

# 1.3.1 in (未来工作：在列表中，无需注册，不在列表，新注册)
# - 语法：指定数据 in 列表序列

name_list_five = ["小熊", "小呆", "小虎", "小萌", "小熊", "小熊"]

print("小萌" in name_list_five)  # True
print("小二" in name_list_five)  # False
print()

# 1.3.2 not in
# - 语法：指定数据 not in 列表序列

print("小萌" not in name_list_five)  # False
print("小二" not in name_list_five)  # True
print()

# 体验案例
# 查找用户输入的名字是否存在 (基础版)
"""
name_list_five = ["tom", "lily", "lucy", "rose", "jack"]
name = input("请输入您需要注册邮箱的用户名：")

if name in name_list_five:
    print(f"您输入的 {name} 已经被注册！")

else:
    print(f"您输入的 {name} 未被注册，可以放心使用！")
print()


# 查找用户输入的名字是否存在 (升级版 - 自己研究)

name_list_five = ["tom", "lily", "lucy", "rose", "jack"]
name = input("请输入您需要注册邮箱的用户名：")

if name not in name_list_five:
    print(f"您输入的 {name} 未被注册，可以放心使用！")
    print("注册名已核验完成！")
else:
    while name in name_list_five:
        name_again = input("请您输入未被注册的用户名：")
        if name_again in name_list_five:
            print(f"您输入的 {name_again} 已经被注册！")
        else:
            print(f"您输入的 {name_again} 未被注册，可以放心使用！")
            print("注册名已核验完成！")
"""

# 2.增加

# 2.1 .append()
# - 列表结尾追加新数据，只增加 单个 的新数据
# - 语法：列表序列.append(新数据)

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
name_list_six.append("小坏蛋")

name_list_se7en = ["小熊", "小呆", "小虎", "小萌", "小明"]
name_list_se7en.append(["小疯子", "小傻子", "小坏蛋"])

print(name_list_six)
# - 原列表被改变了
# - 新数据 单独 被增加入原列表中，如下：
# - 输出：['小熊', '小呆', '小虎', '小萌', '小坏蛋']

print(name_list_se7en)
# - 原列表被改变了
# - 整个新列表作为 整体 被加入原列表中，如下：
# - 输出：['小熊', '小呆', '小虎', '小萌', '小明', ['小疯子', '小傻子', '小坏蛋']]

print()

# 2.2 .extend()
# - 列表尾追加数据，可以拆分字符串，拆分后的新数据在尾部逐一增加
# - 可以增加新列表 (即多个新数据)，可以拆分序列，差分后的新数据在尾部逐一增加
# - 语法：列表序列.extend(新数据)

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
name_list_six.extend("小坏蛋")

name_list_se7en = ["小熊", "小呆", "小虎", "小萌", "小明"]
name_list_se7en.extend(["小疯子", "小傻子", "小坏蛋"])

print(name_list_six)
# 拆分单独数据
# 输出：['小熊', '小呆', '小虎', '小萌', '小', '坏', '蛋']

print(name_list_se7en)
# 拆分序列
# 输出：['小熊', '小呆', '小虎', '小萌', '小明', '小疯子', '小傻子', '小坏蛋']

print()

# 2.3 .insert() - 俗称：插队
# - 指定位置增加新数据
# - 语法：列表序列.insert(位置下标, 新数据)

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
#    0      1       2      3
name_list_six.insert(1, "小坏蛋")

name_list_se7en = ["小熊", "小呆", "小虎", "小萌", "小明"]
#    0      1       2      3       4
name_list_se7en.insert(3, ["小疯子", "小傻子", "小坏蛋"])

print(name_list_six)
# - 占据下标的位置，原下标的数据顺势后延
# - 输出：['小熊', '小坏蛋', '小呆', '小虎', '小萌']
#           0        1       2      3       4

print(name_list_se7en)
# - 占据下标的位置，原下标的数据顺势后延
# - 输出：['小熊', '小呆', '小虎', ['小疯子', '小傻子', '小坏蛋'], '小萌', '小明']
#           0       1      2                  3                 4      5

print()

# 3.删除

# 3.1 del - 把变量从内存中删除

# 3.1.1 删除列表
# - 语法：del 目标 或者 del(目标)

name_list_six = ["小熊", "小呆", "小虎", "小萌"]

del name_list_six[1]
print(name_list_six)  # 输出：['小熊', '小虎', '小萌']
print()

###del name_list_six
###del(name_list_six)

###print(name_list_six) # 输出：NameError: name 'name_list_six' is not defined


# 3.1.2 删除指定数据
# - 语法：del 列表序列[下标]

name_list_night = ["小熊", "小呆", "小虎", "小萌", "小熊"]
#    0      1       2      3       4

print(name_list_night)  # 输出：['小熊', '小呆', '小虎', '小萌']
print()

# 3.2 .pop()
# - 删除指定下表的数据 (默认为最后一个)，并返回数据
# - 语法：列表序列.pop(下标)

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
#    0      1       2      3

del_name_one = name_list_six.pop()

print(name_list_six)  # 输出：['小熊', '小呆', '小虎'] - 默认删除最后一个
print(del_name_one)  # 输出:小萌 - 返回数据，也就是可以出现新的变量
print()

# 3.3 .remove()
# - 移除列表中某个数据的第一个匹配项
# - 语法：列表序列.remove(指定数据)

name_list_night = ["小熊", "小呆", "小虎", "小萌", "小熊"]

name_list_night.remove("小熊")

print(name_list_night)
# - 有相同的数据，从左到右依次删除
# - 输出：['小呆', '小虎', '小萌', '小熊']

print()

# 3.4 .clear()
# - 清空列表内的所有数据
# - 语法：列表序列.clear()

name_list_six = ["小熊", "小呆", "小虎", "小萌"]

name_list_six.clear()

print(name_list_six)  # 输出：[]
print()

# 4.修改

# 4.1 修改指定下标数据
# - 语法：列表序列[下标]

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
name_list_six[1] = "小混蛋"  # 找到数据，重新赋值

print(name_list_six)
# - 原列表已被修改
# - 输出：['小熊', '小混蛋', '小虎', '小萌']

print()

# 4.2 逆置数据
# - .reverse()：单纯把数据反过来
# - 语法：列表序列.reverse()

num_list = [2, 8, 5, 3]
name_list_six = ["小熊", "小呆", "小虎", "小萌"]

num_list.reverse()
name_list_six.reverse()

print(num_list)  # 输出：[3, 5, 8, 2]
print(name_list_six)  # 输出：['小萌', '小虎', '小呆', '小熊']
print()

# 4.3 数据排序
# - .sort()：排序
# - 语法：列表序列.sort(key=None, reverse=False) - key 在 dict 中排序才需要使用
# - 注意：reverse = True 表示：降序，reverse = False 表示：升序(默认)

num_list_one = [2, 8, 5, 3, 7]
num_list_two = [2, 8, 5, 3, 7]
num_list_three = [2, 8, 5, 3, 7]
word_list = ["c", "k", "g", "z", "e"]
name_list_six = ["小熊", "小呆", "小虎", "小萌"]
name_list_six_copy = ["小熊", "小呆", "小虎", "小萌"]

num_list_one.sort()
num_list_two.sort(reverse=False)
num_list_three.sort(reverse=True)
word_list.sort()
name_list_six.sort()
name_list_six_copy.sort(reverse=True)

print(num_list_one)  # 输出：[2, 3, 5, 8] - 默认升序排列
print(num_list_two)  # 输出：[2, 3, 5, 7, 8] - False：0，相当于：0-2-3-5-7-8
print(num_list_three)  # 输出：[8, 7, 5, 3, 2]
print(word_list)  # 输出：['c', 'e', 'g', 'k', 'z']
print(name_list_six)  # 输出：['小呆', '小熊', '小萌', '小虎'] - 按照？？？排列
print(name_list_six_copy)  # 输出：['小虎', '小萌', '小熊', '小呆'] - 按照？？？排列
print()

# 5.复制 .copy()
# - 语法：列表序列.copy()

name_list_six = ["小熊", "小呆", "小虎", "小萌"]
new_name_list = name_list_six.copy()

print(name_list_six)
print(new_name_list)
print()
