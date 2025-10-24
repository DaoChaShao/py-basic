
# 运算符和运算符号

# 1.算数运算符 (+, -, *, /)
# 2.赋值运算符
# 3.复合赋值运算符
# 4.比较运算符 (>, <)
# 5.逻辑运算符 (and, or，not)



# +
# -
# *
# /
# // (商)
# % (取“摩儿” - 取余数，例 9 % 4 其结果为 1)
# ** (幂计算优先)
# ()

# 优先级：() 高于 ** 高于 *, /, //, % 高于 +, -



# 1.算数运算(符)
print(1 + 1)
print()
print(1 + 1.1)
print()
print(1 - 0.5)
print()
print(2 * 0.5)
print()
print(4 / 2)
print()
print(9 // 4)
print()
print(9 % 4)
print()
print(2 ** 3)
print()
print(1 + 2 * 3)
print()
print((1 + 2) * 3)
print()
print(2 * 3 ** 2) # 优先幂计算
print()
print((2 * 3) ** 2)
print()




# 2.赋值运算(符)

# 2.1单变量赋值
num_one = 1
print(num_one)
print()

# 2.2多变量赋值
num_two, float_one, str_one = 10, 0.5, "hello PY"
print(num_one)
print(float_one)
print(str_one)
print()

# 2.3多变量赋相同值
a = b =10
print(a)
print(b)

# 3.复合赋值运算符

# 3.1 += 加法赋值运算符，例：c += a --- c = c + a
a = 10
a += 1 # a = a + 1
print(a)
print()

# 3.2 -= 减法赋值运算符，例：c -= a --- c = c - a
b = 9
b -= 1 # b = b - 1
print(b)
print()

# 3.3 *= 乘法赋值运算符，例：c *= a --- c = c * a
c = 10
c *= 1 + 2 # 注意：先算复合赋值运算右边的表达式，然后再计算复合赋值！
print(c)
print()

# 3.4 /= 除法赋值运算符，例：c /= a --- c = c / a
print()
print()

# 3.5 //= 整除赋值运算符，例：c // a --- c = c // a
print()
print()

# 3.6 %= 取余赋值运算符，例：c % a --- c = c % a
print()
print()

# 3.7 **= 幂赋值运算符，例：c ** a --- c = c ** a
print()
print()




# 4.比较运算符

# 4.1 == 条件结果为true

print(1 == 1)
print(1 == 2)
print()

# 4.2 !=

# 5.逻辑运算符
# 书写习惯：用小括号"()"括起来，例：print((a < b) and (c > a))
# 书写习惯的目的：避免歧义，提升效率，方便他人

# 5.1 and 且，同时成立为True
a = 0
b = 1
c = 2

print(a < b and c > a)
print(a > b and c > a)
print()

# 5.2 or 或，一个成立为True，都不成立是False
print(a < b or b > c)
print(a > b or b > c)
print()

# 5.3 not 非，不成立为True
print(not False)
print(not c > b)
print()

# 拓展
whether_emploee = True

if not whether_emploee:
    print("非本公司员工，玩蛋去！")
else:
    print("来呀，造作呀！")
print()

# 5.4 拓展

# 5.4.1 and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b) #0
print(b and a) #0
print(a and c) #0
print(c and a) #0
print(b and c) #2
print(c and b) #1
print()

# 5.4.2 or运算符，只有所有值为0，结果才为0，否则结果为第一个非0数字
print(a or b) #1
print(a or c) #2
print(b or c) #1
