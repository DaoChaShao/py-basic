# 元组和元组遍历

# 一个元组可以存储多个数据，且元组内的 单纯的元组数据 是不能修改的 (列表可以修改)
# 案例:身份证号是不能轻易修改的，所以最好放在元组里储存

# 初始体验
# - 在一个元组中可以存储多个不同类型的数据，但最好可以存储成一类数据，方便后期操作

tuple_one = (10, 20, 30)

print(tuple_one)  # 输出：(10, 20, 30)
print(type(tuple_one))  # 输出：<class 'tuple'>
print()

# 1.定义元组

# 1.1 定义多个数据的元组

tuple_one = (10, 20, 30)

print(tuple_one)  # 输出：(10, 20, 30)
print(type(tuple_one))  # 输出：<class 'tuple'>
print()

# 1.2 定义多个数据的元组
# - 逗号 非常重要
# - 没有逗号，则数据是什么类型，“元组”就是什么类型

tuple_two = (10,)
tuple_three = (10)
tuple_four = ("abc",)
tuple_five = ("abc")

print(tuple_two)  # 输出：(10,)
print(type(tuple_two))  # 输出：<class 'tuple'>
print()

print(tuple_three)  # 输出：10
print(type(tuple_three))  # 输出：<class 'int'>
print()

print(tuple_four)  # 输出：('abc',)
print(type(tuple_four))  # 输出：<class 'tuple'>
print()

print(tuple_five)  # 输出：abc
print(type(tuple_five))  # 输出:<class 'str'>
print()

# 2 元组的常见操作 (与列表和字符串一致)
# - 由于不能修改，所以元组数据不支持增、删和改的操作
# - 元组只支持 查找 操作

# 2.1 按下标查找数据

tuple_six = ("小熊", "小呆", "小虎", "小萌")
          #    0      1       2      3

print(tuple_six[1])  # 输出：小呆
print(type(tuple_six))  # 输出：<class 'tuple'>
print()

# 2.2 .index() 查找某个数据，如果数据存在，则返回对应下标，否则则报错 (和列表、字符串同理)
# - 语法：元组.index(需要查找的数据)

tuple_six = ("小熊", "小呆", "小虎", "小萌")
          #    0      1       2      3

print(tuple_six.index("小熊"))  # 输出：0 - 下标对应的位置
print(type(tuple_six))  # 输出：<class 'tuple'>
print()
###print(tuple_six.index("小熊仔")) # 输出：ValueError: tuple.index(x): x not in tuple
print()

# 2.3 .count() 统计某个数据出现在当前元组中的次数
# - 语法：语法：元组.count(需要统计出现次数的数据)

tuple_se7en = ("小熊", "小呆", "小虎", "小萌", "小呆", "小呆", "小呆", "小熊")

print(tuple_se7en.count("小呆"))  # 输出：4
print(tuple_se7en.count("小熊"))  # 输出：2
print(tuple_se7en.count("小熊仔"))  # 输出：0 - 因为不存在该数据，所以显示为 0
print()

# 2.4 len() 统计元组的长度，即统计元组中数据的个数

tuple_se7en = ("小熊", "小呆", "小虎", "小萌", "小呆", "小呆", "小呆", "小熊")

print(len(tuple_se7en))  # 输出：8
print(type(tuple_se7en))  # 输出：<class 'tuple'>
print(type(len(tuple_se7en)))  # 输出：<class 'int'>
print()

# 3 元组数据的修改

tuple_six = ("小熊", "小呆", "小虎", "小萌")
          #    0      1       2      3

###tuple_six[0] = "小熊仔"
# - 给元组中的第一个数据 重新赋值
# - 输出：TypeError: 'tuple' object does not support item assignment

tuple_eight = ("小熊", "小呆", "小虎", ["lily", "lucy", "rose"])
            #    0      1       2                3
            #                           0        1       2

print(tuple_eight[3][2])
# - 找到元组的列表中的 rose
# 输出：rose

tuple_eight[3][2] = "tom"  # 给元组中的列表的中的数据 重新赋值

print(tuple_eight)
# - 原元组已经被修改
# - 元组中的列表被修改
# - 输出：('小熊', '小呆', '小虎', ['lily', 'lucy', 'tom'])
print()

# 4.元组循环遍历 - 通常不用元组遍历 - 不能使用格式字符串拼接临时变量
tuple_nine = ("小熊", 18, 165)
           #    0     1   2

for i in tuple_nine:  # 通常情况下，元组中存储的数据类型不一致

    print(i)  # 不能使用格式字符串(f，%d，%s等)拼接 i(临时变量)
    # 输出：小熊
    #      18
    #      165
print()

# 5.其他操作

# 5.1 格式化字符串
tuple_ten = ("小熊", 18, 1.65)

print("名字：%s，年龄：%03d岁，身高：%.2f米" % tuple_ten)
# 输出：名字：小熊，年龄：018岁，身高：1.65米
print()

info = "名字：%s，年龄：%03d岁，身高：%.2f米" % tuple_ten

print(info)  # 输出：名字：小熊，年龄：018岁，身高：1.65米
print()

# 5.2 列表与元组的转换

# 语法：
# - list(元组)
# - typle(列表)

tuple_ten = ("小熊", 18, 1.65)
list_ten = ["小呆", 20, 1.80]

list_exchange = list(tuple_ten)
tuple_exchange = tuple(list_ten)

print(type(tuple_ten))  # 输出：<class 'tuple'>
print(type(list_exchange))  # 输出：<class 'list'>
print(list_exchange)  # 输出：['小熊', 18, 1.65]
print()

print(type(list_ten))  # 输出：<class 'list'>
print(type(tuple_exchange))  # 输出：<class 'tuple'>
print(tuple_exchange)  # 输出：('小呆', 20, 1.8)
print()
