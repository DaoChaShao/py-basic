# if 语法
# if 条件:
#    条件成立执行的代码 1 # 注意tab键缩进
#    条件成立执行的代码 2 # 注意tab键缩进


# 1.单条件判断
if True:
    print("条件成立执行的代码 1")  # 执行的代码与if成立有关
    print("条件成立执行的代码 2")  # 执行的代码与if成立有关
print()
print("代码 3")  # 执行的代码与if成立无关

if False:
    print("条件成立执行的代码 1")  # 执行的代码与if成立有关
    print("条件成立执行的代码 2")  # 执行的代码与if成立有关
print()
print("代码 3")  # 执行的代码与if成立无关

age = 20

if age >= 18:  # type：int
    print(f"您的年龄是：{age}岁，\n您已成年，可以开车！")
print()
print("核验结束，系统关闭！")
print()

age = int(input("请输入您的年龄："))  # str数据转化为int， 否则报错

if age >= 18:  # type：int
    print(f"您的年龄是：{age}岁，\n您已成年，可以开车！")
print()
print("校验结束，系统关系！")
print()

# 进阶

enter_age = int(input("请输入您的年龄："))  # str数据转化为int， 否则报错

if enter_age >= 18:
    print(f"您输入的年龄为：{enter_age}岁，允许进入网吧嗨皮！")

print()

# 2.双条件判断

# if else 语法
# if 条件 1:
#    条件成立执行的代码 1 # 注意tab键缩进
#    条件成立执行的代码 2 # 注意tab键缩进
# else 条件 2:
#    条件成立执行的代码 3 # 注意tab键缩进
#    条件成立执行的代码 4 # 注意tab键缩进

age = int(input("请输入您的年龄："))  # str数据转化为int

if age >= 18:  # type：int
    print(f"您的年龄是：{age}岁，\n您已成年，可以开车！")
else:
    print(f"您的年龄是：{age}岁，\n您未成年，请您滚蛋！")
print()
print("校验结束，系统关系！")  # 无论条件是否成立，代码均执行
print()

# 进阶

enter_age = int(input("请输入您的年龄："))

if enter_age >= 18:
    print(f"您输入的年龄为：{enter_age}岁，允许进入网吧嗨皮！")
else:
    print(f"您输入的年龄为：{enter_age}岁，还未成年，给老子爬！")
print()

# 3.多重判断

# if 条件 1:
#    条件成立执行的代码 1 # 注意tab键缩进
#    条件成立执行的代码 2 # 注意tab键缩进
# elif 条件 2:
#    条件成立执行的代码 3 # 注意tab键缩进 - 使用纯粹的变量，不要套函数使用，例：int(input)
#    条件成立执行的代码 4 # 注意tab键缩进 - 使用纯粹的变量，不要套函数使用，例：int(input)
# ······
# else:
#    条件成立执行的代码 5 # 注意tab键缩进
#    条件成立执行的代码 6 # 注意tab键缩进

# 3.1 第一种写法(化简写法)
age = int(input("请输入您的年龄："))  # str数据转化为int

if 0 <= age < 18:
    print(f"您的年龄为：{age}岁，\n您TM是童工，别害人！")
elif 60 >= age >= 18:
    print(f"您的年龄为：{age}岁，\n您属于合法用工年龄！")
else:
    print(f"您的年龄为：{age}岁，\n你已到法定退休年龄，\n请您滚蛋！")
print()
print("校验结束，系统关系！")
print()

# 3.2 第二种写法
age = int(input("请输入您的年龄："))  # str数据转化为int

if (age < 18) and (age >= 0):
    print(f"您的年龄为：{age}岁，\n您TM是童工，别害人！")
elif (age >= 18) and (age <= 60):
    print(f"您的年龄为：{age}岁，\n您属于合法用工年龄！")
else:
    print(f"您的年龄为：{age}岁，\n你已到法定退休年龄，\n请您滚蛋！")
print()
print("校验结束，系统关系！")
print()

# 3.3 第三种写法
age = int(input("请输入您的年龄："))  # str数据转化为int

if (age < 18) and (age >= 0):
    print(f"您的年龄为：{age}岁，\n您TM是童工，别害人！")
elif (age >= 18) and (age <= 60):
    print(f"您的年龄为：{age}岁，\n您属于合法用工年龄！")
elif age > 60:
    print(f"您的年龄为：{age}岁，\n你已到法定退休年龄，\n请您滚蛋！")
print()
print("校验结束，系统关系！")
print()

# 其他扩展
guess = int(input("从1-10，你猜我想我的数字是多少："))
if guess == 9:
    print("哇塞，猜对了！")
    print("不过没奖励")
else:
    while guess != 9:
        guess = int(input("继续猜:"))
        if guess == 9:
            print("恭喜你，猜对了！")
            print("你好棒棒！")
        else:
            if guess > 9:
                print("偏大")
            else:
                print("偏小")
print("游戏结束")
print()

# 拓展 - 女友节日案例
print("*" * 26)
info_one = "单身狗脱单之节日攻略"
print(info_one.center(20))
print("*" * 26)
info_two = "过 情人节 请按 1"
print(info_two.center(22))
info_three = "过 平安夜 请按 2"
print(info_three.center(22))
info_four = "过 双十一 请按 3"
print((info_four.center(22)))
info_five = "过 生日宴 请按 4"
print((info_five.center(22)))
info_six = "过 每一天 请按 5"
print((info_six.center(22)))
print("*" * 26)
print()

enter_num = int(input("请输入节日数字："))
print()

holiday_name_one = "情人节"
holiday_name_two = "平安夜"
holiday_name_three = "双十一"
holiday_name_four = "生日宴"
holiday_name_five = "每一天"

if enter_num == 1:
    print("*" * 26)
    print(f"在 {holiday_name_one} ，\n单身狗应该准备：\n红包，玫瑰花，电影票和如家房卡！")
    print("*" * 26)
elif enter_num == 2:
    print("*" * 26)
    print(f"在 {holiday_name_two} ，\n单身狗应该准备：\n红包，红苹果，圣诞礼物和如家房卡！")
    print("*" * 26)
elif enter_num == 3:
    print("*" * 26)
    print(f"在 {holiday_name_three} ，\n单身狗应该准备：\n红包，清空购物车和如家房卡！")
    print("*" * 26)
elif enter_num == 4:
    print("*" * 26)
    print(f"在 {holiday_name_four} ，\n单身狗应该准备：\n红包，清空购物车和如家房卡！")
    print("*" * 26)
else:
    print("*" * 26)
    print(f"在 {holiday_name_five} ，\n单身狗应该准备：\n仪式感、安全感和红包！")
    print("*" * 26)
print()
