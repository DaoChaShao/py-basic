# 异常

# 1.捕获异常
# - try 尝试，下方编写要尝试代码，不确定是否能够正常执行的代码
# - except 如果不是，下方便些尝试失败的代码

# 1.1 语法：
#   try:
#       尝试执行的代码
#   except:
#       出现错误的需要执行的代码

# 1.2 案例体验
# 1.2.1 基本组
num = int(input("请输入一个整数："))
# 输入：a
# 输出：invalid literal for int() with base 10: 'a'
print()

# 1.2.2 对照组
try:
    # 不能确定正确执行的代码
    num = int(input("请输入一个整数："))
    # 输入：a
except:
    # 触发错误后，需要执行的代码
    print("请输入一个整数")
print("*" * 27)
# 整体输出结果：请输入一个整数
#             ***************************
print()

# 2.错误类型捕获
# 2.1 捕捉报错 - 基本组

# 语法：
#   try：
#       尝试执行代码
#   except 报错类型名：
#       出现错误的需要执行的代码

# 提示用户输入一个整数
num = int(input("请输入一个整数："))
# 输入：0
# 输入：a

# 使用 8 除以用户输入的整数并且输出
result = 8 / num

print(result)
# 输出：division by zero
# 输出：invalid literal for int() with base 10: 'a'
print()

# 2.2 捕捉报错 - 对照组

# 提示用户输入一个整数
num = int(input("请输入一个整数："))
# 输入：0
# 输入：a

# 使用 8 除以用户输入的整数并且输出
result = 8 / num

print(result)
# 输出：division by zero
# 输出：invalid literal for int() with base 10: 'a'
print()

# 2.3 案例体验 - 对照组 1
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 输入：0
    # 输入：a

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num

    print(result)
    # 输出：输入除 0 以外的整数
    # 输出：不能输入字母

# except 后填写报错的错误类型
except ZeroDivisionError:
    print("输入除 0 以外的整数")

# except 后填写报错的错误类型
except ValueError:
    print("不能输入字母")

print()

# 2.2 捕捉未知错误
# 语法：
#   except Exception as result：
#       print("未知错误 %s" % result)
#       或者
#       print(f"未知错误 {result}")
#

try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 输入：0
    # 输入：a

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num

    print(result)
    # 输出：未知错误 division by zero
    # 输出：不能输入字母

# except 后填写报错的错误类型
except ValueError:
    print("不能输入字母")

# 捕获未知错误
except  Exception as result:
    print(f"未知错误 {result}")

print()

# 2.3 完整的错误捕捉
# 语法：
#   try：
#       尝试执行代码
#   except 报错类型名 1：
#       针对错误类型 1，出现错误的需要执行的代码
#   except 报错类型名 2：
#       针对错误类型 2，出现错误的需要执行的代码
#   except (报错类型名 3, 报错类型名 4)：
#       针对错误类型 3 和 4，出现错误的需要执行的代码
#   except Exception as result：
#       (打印错误信息)
#       print(result)
#   else：
#       没有错误才会执行的代码
#   finally：
#       (无论是否有异常，都会执行的代码)
#       print("无论是否有异常，都会执行的代码")

try:

    num = int(input("请输入一个整数："))
    # 输入 1
    # 输入 a
    # 输入 0

    outcome = 8 / num

    print(outcome)
    # 输出：8.0
    #      尝试成功
    #      无论是否有异常，都会执行的代码
    #      ***************************

    # 输出：不能输入字母
    #      无论是否有异常，都会执行的代码
    #      ***************************

    # 输出：未知错误 division by zero
    #      无论是否有异常，都会执行的代码
    #      ***************************

except ValueError:
    print("不能输入字母")
except Exception as result:
    print(f"未知错误 {result}")
else:
    print("尝试成功")
finally:
    print("无论是否有异常，都会执行的代码")

print("*" * 27)
print()


# 2.4 异常的传递

# 2.4.1 常规组
def demo_1():
    print(int(input("请输入整数：")))
    # 输入 a


def demo_2():
    return demo_1()


print(demo_2())
# 输出：nvalid literal for int() with base 10: 'a'
print()


# 2.4.2 对照组
def demo_1():
    print(int(input("请输入整数：")))
    # 输入 a


def demo_2():
    return demo_1()


# 利用异常的传递性，在主程序中捕获异常
try:
    print(demo_2())
    # 输出：未知错误 invalid literal for int() with base 10: 'a'
except Exception as result:
    print(f"未知错误 {result}")
print()


# 3.主动抛出(raise)异常
# 创建 Exception 的对象
# 使用 raise 关键字 抛出 异常对象

# 密码案例
# - 长度小于 8 抛出异常
# - 长度大于等于 8 正常

def input_password():
    # 1.提示用户输入密码
    enter_info = input("请输入密码：")
    # 输入：1

    # 2.判断密码长度
    # 2.1 如果长度 >= 8 则返回用户输入的密码
    if len(enter_info) >= 8:
        return enter_info

    # 2.2 如果长度 < 8 主动抛出异常
    print("主动抛出异常")

    # 2.2.1 创建异常对象
    # - 用赋值的方式创建异常
    # - 可以使用错误信息的字符串作为参数 >>>"密码长度不足八位"<<<
    error_info = Exception("密码长度不足八位")

    # 2.2.2 主动抛出异常 - 运行时，会出现红字报错
    raise error_info


# 调取 并 输出 用户输入密码函数
# 由于上面已经创建异常，此处要捕捉异常
try:
    print(input_password())

except Exception as result:
    print(result)
    # 输出：主动抛出异常
    #      密码长度不足八位
print()
