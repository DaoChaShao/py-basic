
# 字符串基础内容

# 1.单引号

a = 'Hello python'
print(a)
print(type(a))

b = 'let\'s go!' # 增加转义符号 - 反斜杠
print(b)
print(type(b))



# 2.双引号

c = "PYTHON"
print(c)
print(type(c))

d = "I'm TOM"
print(d)
print(type(d))



# 3.三引号

e = """YONG"""
print(e)
print(type(e))

f = """讨
厌"""
print(f) # 三引号支持换行输出
print(type(f))



# 4.字符串输出

print("我爱派森！")

name = "汤姆" # name = input("请输入您的名字：") - 格式化输出方便交互
print("我的名字是：%s" % name)
print(f"我的名字是：{name}")



# 5.字符串输入

password = input("为方便我偷窥，请输入您的密码：")
print(f"您输入的密码是：{password}，我已掌握！")
print(type(password))



# 6.下标 (索引或索引值) - (字符串、列表、元组都会用上)

str_one = "abcdefghij" # 程序运行是，数据存在内存里
print(str_one)

# 使用字符串中某个特定的数据，例：得到数据中的 a
# 数据存在内存中时，会为这些数据顺序分配从0开始的编号，如下：
# 数据：a  b  c  d  e  f  g  h  i  j
# 编号：0  1  2  3  4  5  6  7  8  9
# 使用这些对应编号可以找到相对应的数据
# 这个编号被称作：下标、索引或索引值
# 下标语法：str_one[下标] - (以上述str_one变量为例)
# 例：print(str_one[0]) - a

print(str_one[0])
print(str_one[1])



# 7.切片

# 指截取操作对象截取其中一部分的操作
# 字符串、列表、元组都支持切片操作
# 切片语法：序列[开始位置下标:结束位置下标:步长]
# 取的数据范围是：“左闭右开”的区间范围

str_two = "ABCDEFG" # 程序运行是，数据存在内存里
        #  0123456
print(str_two)
print(str_two[2]) # 得到某个特定的数据 C
print(str_two[0:3:1]) # 得到某几个特定的数据 ABC

str_three = "1234567890"
#            0123456789 - 下标

print(str_three[2:5:1]) # 345
print(str_three[2:5:2]) # 35 - 每隔 1 个截取
print(str_three[2:5]) # 345 - 如果不写步长，就默认步长为 1
print(str_three[:5]) # 12345 - 如果不写起始下标，就默认起始下标位置为 0 ，且包括 0
print(str_three[2:]) # 34567890 - 如果不写结束下标，就默认结束下标位置为最后，且包含结束
print(str_three[:]) # 1234567890 - 如果不写开始和结束下标，就默认是所有数据
print()
print(str_three[::-1]) # 0987654321 - 如果步长为 负 ，则数据为倒叙排列
print(str_three[-4:-1]) # 789 - 起始和结束下标为负是：依次从后向前数
print(str_three[-4:-1:1]) # 789 - 和上面一样，不写步长为，就默认步长为 1
print(str_three[-4:-1:-1]) # 不能输出
                           # 原因如下：
                           # - 从-4开始至-1结束，选取反向为：从左到右
                           # - 步长-1，选取方向为：从右到左
                           # - 选取方向(下标开始至结束的方向)不能与步长方向冲突
                           # - 如果冲突，则无法选取数据
print(str_three[-1:-4:-1]) # 098
                           # 原因如下：
                           # - 从-1至-4是，选取方向为：从右到左
                           # - 步长方向为：从左到右
                           # - 选取方向与步长方向一致，所以可以显示数据
