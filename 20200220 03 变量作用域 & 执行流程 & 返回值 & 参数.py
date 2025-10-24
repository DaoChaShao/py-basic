
# 函数进阶内容
# - 包括：变量作用域、执行流程、返回值、参数
# - 每一个以 .PY 结尾的文件，都是一个模块

# 1.变量的作用域
# - 解释：变量生效的范围
# - 变量的分类：局部变量 和 全局变量

# 1.1 局部变量
# - 局部变量：定义在函数体内部的变量，即只在函数体内部生效

def testA():
    a = 100

    print(a)

testA() # 输出：100 - 函数体 内部 访问 变量
###print(a)
    # 输出：NameError: name 'a' is not defined
    # 变量 a 是定义在 testA 函数内部的变量，在函数外部访问，则立即报错
print()

# 1.2 全局变量
# - 全局变量：在函数体内、外都能生效的变量

a = 100 # 定义：全局变量 a

print(a) # 输出：100 - 全局变量输出

def testA():
    print(a) # 访问全局变量 a，并打印变量 a 存储的数据

def testB():
    print(a) # 访问全局变量 a，并打印变量 a 存储的数据

testA() # 输出：100 - 局部变量输出
testB() # 输出：100 - 局部变量输出

print(a) # 输出：100 - 全局变量输出
print()

b = 100

print(b)

def testC():
    print(b)

def tsetD():
    # 想要把局部变量修改为全局变量
    global b # 声明 b 为全局变量
    b = 200 # 局部变量
    print(b) # 输出：200 - 局部变量输出

testC()
tsetD()
print(b)
"""
- 如果在局部函数里更改局部变量，此时相当于声明了一个新变量，而不是修改了全局变量
- 如果在局部函数里想更改全局变量，首先要用 global 声明为全局变量，然后再重新对变量赋值
"""
print()

# 2.多函数程序执行流程
# 一般在实际开发过程中，一个程序往往由多个函数组成，且多个函数共享某些数据 - 共享全局变量

# 定义全局变量
glo_num = 0

def test_one():
    global glo_num
    # 修改全局变量
    glo_num = 100

def test_two():
    # 调用 test_one 函数中修改后的全局变量
    print(glo_num)

print(glo_num) # 输出：0 - 因为没有调用函数
# 调用 test_one 函数，执行函数内部代码：生命和修改全局变量
test_one()
# 调用 test_two 函数，执行函数内部代码：打印
test_two() # 输出：100
print()

# 3.函数返回值

# 3.1 返回值可以作为另外一个函数的参数

def test_three():
    return 50

def test_four(num):
    print(num)

# 保存函数 test_three 的返回值
result = test_three()

# 将函数返回值所在的变量作为参数传递到 test_four 函数中
test_four(result) # 输出：50 - 也可以：test_four(test_three())
print()

# 3.2 一个函数有多个返回值

def return_num_one():
    return 1 # return 有结束代码的功能
    return 2 # return 的返回值代码不能被执行

result = return_num_one()
print(result) # 输出：1

def return_num_two():
    return 1, 2

result = return_num_two()
print(result) # 输出：(1, 2)
print(type(result)) # 输出：<class 'tuple'>
print()

# 返回单个数据
def measure():
    """测量温度和湿度"""

    print("测量开始")
    temp = 39
    print("测量结束")

    return temp

result = measure()

print(result)
    # 输出：
    # 测量开始
    # 测量结束
    # 39
print()

# 返回多个数据 - 元组
def measure():
    """测量温度和湿度"""

    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")

    # 元组可以保存多个数据，因此可以让元组函数一次返回多个值
    # 返回值为元组时，可以不添加元组的小括号
    #return (temp, wetness)
    return temp, wetness

result = measure()

print(result)
    # 输出：
    # 测量开始
    # 测量结束
    # (39, 50)
print()

# 返回多个数据后，需单独处理返回的数据
def measure():
    """测量温度和湿度"""

    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")

    return temp, wetness
    #        0      1
    # 返回值对应 元组下标的顺序

result = measure()

print(result)
    # 输出：
    # 测量开始
    # 测量结束
    # (39, 50)
# 使用元组索引 - 不太方便
print(result[0]) # 输出：39
print(result[1]) # 输出：50
print()
# 如果函数返回的类型是元组，同时希望单独处理元祖中的元素
# 可以使用多个变量，一次接收函数的返回值
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
    # 输出：
    # 测量开始
    # 测量结束
    # 39
    # 50
print()

# 3.3 return 后面可以直接书写 元组，列表，字典，集合，且返回多个值

def return_num_three():
    # return 后面可以直接书写 元组，且返回多个值
    return (10, 20)

result = return_num_three()
print(result) # 输出：(10, 20)
print(type(result)) # 输出：<class 'tuple'>
print()


def return_num_four():
    # return 后面可以直接书写 列表，且返回多个值
    return [10, 20]

result = return_num_four()
print(result) # 输出：[10, 20]
print(type(result)) # 输出：<class 'list'>
print()


def return_num_five():
    # return 后面可以直接书写 字典，且返回多个值
    return {"name" : "tom", "age" : 20}

result = return_num_five()
print(result) # 输出：{'name': 'tom', 'age': 20}
print(type(result)) # 输出：<class 'dict'>
print()


def return_num_six():
    # return 后面可以直接书写 集合，且返回多个值
    return {"name",}

result = return_num_six()
print(result) # 输出：{'name'}
print(type(result)) # 输出：<class 'set'>
print()

# 4.函数参数的四种写法

# 4.1 位置参数
# - 调用函数时，根据函数定义的参数位置来传递参数
# - 传递和定义参数的顺序及个数必须一致，否则会报错
#   - user_info_three() missing 1 required positional argument: 'gender'

def user_info_one(name, age, gender):
    print(f"您的名字是：{name}，年龄是：{age}岁，性别是：{gender}")

user_info_one("tom", 30, "男") # 输出：您的名字是：tom，年龄是：30岁，性别是：男
print()

# 4.2 关键字参数
# - 函数调用时，通过 “键=值” 形式加以指定
# - 可以让函数更加清晰、容易使用
# - 清楚了参数的顺序需求
# - 注意：
#   - 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面
#   - 函数调用时，关键字参数之间不存在先后顺序

def user_info_two(name, age, gender):
    print(f"您的名字是：{name}，年龄是：{age}岁，性别是：{gender}")

user_info_two("rose", age = 20, gender = "女") # 关键字就是形参，不能加引号
    # 输出：您的名字是：rose，年龄是：20岁，性别是：女
user_info_two("小明", gender = "男", age = 16) # 关键字就是形参，不能加引号
    # 输出：您的名字是：小明，年龄是：16岁，性别是：男
print()


# 4.3 缺省参数
# - 缺省参数也叫默认参数
# - 用于定义函数，为参数提供默认值，调用函数时，可不传该默认参数的值
# - 注意：
#   - 所有位置参数必须出现在默认参数前，包括函数定义和调用
#   - 函数调用时，如果为缺省参数传值，则修改默认参数值，否则使用这个默认值

def user_info_three(name, age, gender = "男"):
    print(f"您的名字是：{name}，年龄是：{age}岁，性别是：{gender}")

user_info_three("jerry", 20) # 不为缺省参数传值，则使用默认值
    # 输出：您的名字是：jerry，年龄是：20岁，性别是：男
user_info_three("jerry", 18, "女") # 为缺省参数传值，则修改默认参数值
    # 输出：您的名字是：jerry，年龄是：18岁，性别是：女
print()

# 4.4 不定长参数
# - 不定长参数也叫可变参数
# - 用于不确定调用的时候，会传递多少个参数 (不传参也可以)的场景
# - 用包裹 (packing) 位置参数，或者包裹关键字参数，来进行参数的传递，会显得非常方便
# - 无论是包裹位置传递，还是包裹关键字传递，都是一个组包的过程

# 4.4.1 包裹位置传递 - 接受 所有不定个数的位置参数
# - 注意：
#   - 传进的所有参数都会被 args 变量收集，它会根据传进参数的位置，合并为一个元组 (tuple)

def user_info_four(*args): # * 是必须要写的，args (arguments缩写)可以被其他变量名替换
    print(args)

user_info_four("tom") # 输出：('tom',)
user_info_four("tom", 18) # 输出：('tom', 18)
print()

# 4.4.2 包裹关键字传递 - 接受 关键字参数，且不确定个数的时候

def user_info_five(**kwargs): # kwargs = keyWordsArguments
    print(kwargs)

user_info_five(name = "tom", age = 18, id = 110)
    # 输出：{'name': 'tom', 'age': 18, 'id': 110}
    # 类型：字典
print()

# 4.4.3 综合传递

def demo(num, *args, **kwargs):

    print(num) # 输出：1
    print(args) # 输出：(2, 3, 4, 5)
    print(*args) # 输出：2 3 4 5
    print(kwargs) # 输出：{'name': 'Tom', 'age': 18}
    #print(**kwargs) # 输出：报错

demo(1, 2, 3, 4, 5, name="Tom", age=18)


# 4.4.4.1 多个数字求和 - *args
def sum_num(*args):

    num = 0

    print(args)
    print(*args)

    # 循环遍历
    for n in args:

        num += n

    return num

result = sum_num(1, 2, 3, 4, 5)

print(result)
print()

# 4.4.4.2 多个数字求和 - args
def sum_num(args):

    num = 0

    print(args)
    print(*args)

    # 循环遍历
    for n in args:

        num += n

    return num

result = sum_num((1, 2, 3, 4, 5))

print(result)
print()
