

# 函数进阶内容
# -包括：拆包和交换变量值、引用、数据类型

# 1.拆包 和 交换变量值

# 1.1 拆包

# 1.1.1 拆包元组数据

def return_num():
    return 100, 200

result = return_num() # 利用返回值 - 组包
num_one, num_two = return_num() # 拆包

print(result) # 输出：(100, 200) - 元组组包成功
print(num_one) # 输出：100
print(num_two) # 输出：200
print()


# 1.1.2 拆包字典 - 找到对应的 key 对应的 value

dict_one = {"name" : "tom", "age" : 30}

# dict_one 中有两个键值对，拆包的时候用两个变量接收数据
# kvp - key value pair
kvp_one, kvp_two = dict_one

# 对字典进行拆包，取出来的是字典的 key - 即变量存储的是 key 值
print(kvp_one) # 输出：name
print(kvp_two) # 输出：age

# 拆包后，按 key 做查找，取出的是字典的 value
print(dict_one[kvp_one]) # 输出：tom
print(dict_one[kvp_two]) # 输出：30
print()

# 1.1.3 拆包函数的实参
def demo(*args, **kwargs):

        print(args)
        print(kwargs)

# 元组或字典的变量
gl_nums = (1,2,3)
gl_dict = {"name":"Tom","age":18}

demo(gl_nums, gl_dict)
        # 输出：((1, 2, 3), {'name': 'Tom', 'age': 18})
        #      {}
print()

# 拆包语法：可以简化元组或字典变量的传递
# - 拆包指的是拆函数实参的复杂度，用简单的实参替代
demo(*gl_nums, **gl_dict)
        # 输出：(1, 2, 3)
        #      {'name': 'Tom', 'age': 18}
print()

demo(1,2,3,name="Tom",age=18) # 注意输入字典的格式，是 =，不是：
        # 输出：(1, 2, 3)
        #      {'name': 'Tom', 'age': 18}
print()


# 1.2 交换变量值 - 交换两个变量的值

# 1.2.1 方法一 - 借助第三变量存储数据 (难)

a = 10
b = 20

# 第一步：定义中间变量 c
c = 0

# 第二步：将 a 的数据存储到 c - a 和 c 的位置千万不能互换
c = a

# 第三步：将 b 的数据 20 赋值到 a，此时 a = 20
a = b

# 第四步：将之前 c 的数据 10 赋值到 b，此时 b = 10
b = c

print(a) # 输出：20
print(b) # 输出：10
print()


# 1.2.2 方法二
a = a + b
b = a - b
a = a - b

print(a) # 输出：20
print(b) # 输出：10
print()


# 1.2.3 方法三 - 相当于元组转换，再拆包 (易)

a, b = 1, 2

print(a) # 输出：1
print(b) # 输出：2
print()

# PYTHON 专有写法 - 等号右边是元组，且元组的小括号可以去掉
# a, b = (b, a)
a, b = b, a

print(a) # 输出：2
print(b) # 输出：1
print()

# 2.引用 - 有点儿类似C中的指针
# - 在Python中，值是靠 引用 来传递的
# - 我们可以用 id() 来判断两个变量是否为同一个值的引用
# - 我们可以将 id值 理解为那块内存的地址标识


# 2.1 整型 (int)数据类型 - 不可变数据类型

a = 1
b = a

print(b) # 输出：1

print(id(a)) # 输出：4433037968
print(id(b)) # 输出：4433037968
    # 数据a 和 数据b 的内存地址一致
print()

a = 2
print(b) # 输出：1 - 说明 int类型 为不可变类型
print(id(a)) # 输出：4425865904 - 此时得到的是 数据2 的内存地址
print(id(b)) # 输出：4425865872
print()


# 2.2 列表数据类型 - 可变数据类型

aa = [10, 20]
bb = aa

print(bb) # 输出：[10, 20]

print(id(aa)) # 输出：4461466560
print(id(bb)) # 输出：4461466560
print()

aa.append(30)

print(aa) # 输出：[10, 20, 30]
print(bb) # 输出：[10, 20, 30]
print(id(aa)) # 输出：4461466560
print(id(bb)) # 输出:4461466560
print()


# 2.3 引用当做实参


def test_one(a):
    print(a)
    print(id(a))
    print()

    a += a

    print(a)
    print(id(a))
    print()

# int：计算前后id值 不同

b = 100
test_one(b)
    # 输出：100
    #      4491736816
    #
    #      200
    #      4491740016

# 列表：计算前后id值 相同

c = [11, 22]
test_one(c)
    # 输出：[11, 22]
    #      4493480512
    #
    #      [11, 22, 11, 22]
    #      4493480512
print()




# 3.数据类型 - 可变和不可变类型

# - 可变类型数据：数据能直接修改
# - 不可变类型数据：数据不能直接修改

# - 可变类型数据包括：列表、字典、集合
# - 不可变类型数据包括：整型、浮点型、字符串、元组
