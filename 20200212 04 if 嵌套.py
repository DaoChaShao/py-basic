
# if 嵌套语法
# if 条件 1:
#    条件成立执行的代码 1 # 注意tab键缩进
#    条件成立执行的代码 2 # 注意tab键缩进
#   if 条件 2:
#       条件成立执行的代码 3 # 注意tab键缩进
#       条件成立执行的代码 4 # 注意tab键缩进


#上车和找座位 (基础判断)

money = True # true：有钱，false:没钱
seat = True # true：有座位，false：没座位

if money == True:
    print("您是有钱的大爷，您请上车！")
    if seat == True:
        print("真幸运，有老弱病残孕专座可以坐！")
    else:
        print("真够衰，没座位！")
else:
    print("没钱别上车，请您跟车跑，跑快点儿！")

if money == True:
    print("您是有钱的大爷，您请上车！")
    if seat == False:
        print("真幸运，有老弱病残孕专座可以坐！")
    else:
        print("真够衰，没座位！")
else:
    print("没钱别上车，请您跟车跑，跑快点儿！")

if money == False:
    print("您是有钱的大爷，您请上车！")
    if seat == True:
        print("真幸运，有老弱病残孕专座可以坐！")
    else:
        print("真够衰，没座位！")
else:
    print("没钱别上车，请您跟车跑，跑快点儿！")


# 上车和找座位 (交互判断)

intro = print("车车到了，您准备上车，所以···")
money = input("您是否带钱(请输入：是 或 否)：")

if money == "是":
    print("您是有钱的大爷，您请上车！")

    seat = input("您是否看到空座(请输入：是 或 否)：")
    if seat == "是":
        print("真幸运，有老弱病残孕专座可以坐！")
    else:
        print("真够衰，没座位！")
else:
    print("没钱别上车，请您跟车跑，跑快点儿！")


# 猜拳游戏 (玩家 - 电脑)

# 思维逻辑
# 1. 出拳
# 1.1 玩家出拳
# 1.2 电脑出拳
# 1.2.1 电脑固定出拳
# 1.2.2 电脑随机出拳
# 2. 判断
# 2.1 玩家获胜
# 2.2 双方平局
# 2.3 电脑获胜


# 固定
intro = print("马上进行石头剪刀布的比赛,\n石头：0，剪刀：1，布子：2")
player = int(input("请输出出拳数字："))
computer = 1

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("真尿性，玩家获胜！")
elif player == computer:
    print("挺厉害，双方平局！")
else:
    print("呵呵呵，电脑获胜！")


# 随机数的扩展
# 1. 导入import random模块
# 2. 使用模块中的randint功能
# 3. 语法：random.randint(开始, 结束)
# 3.1 开始：包括开始部分
# 3.2 结束：包括结束部分
# 3.3 例子：import.randint(1，5) - 随机出现1，2，3，4，5中的任意一个数


# 随机 (BUG)

import random

intro = print("马上进行石头剪刀布的比赛,\n石头：0，剪刀：1，布子：2")
player = int(input("请输出出拳数字："))
computer = int(random.randint(0, 2))

print(computer) # 显示电脑随机数

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("真尿性，玩家获胜！")
elif player == computer:
    print("挺厉害，双方平局！")
else: # 未考虑到输入0，1，2以外的数字，其他数字均为：电脑获胜
    print("呵呵呵，电脑获胜！")


# 三目运算符 (三元表达式)

# 语法
# 条件成立的表达式 if 条件 else 条件不成立要执行的表达式

# 举例
a = 1
b = 2

c = a if a > b else b
#    如果 a > b，则是a， 如果a < b， 则是b
print(c)

aa = 10
bb = 6

cc = aa - bb if aa > bb else bb - aa
print(cc)

