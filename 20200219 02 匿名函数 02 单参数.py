
# 单参数


# 传统函数
def calculate(num):
    return num ** 2


print(calculate(10))

# 匿名函数
square = lambda num: num ** 2

print(square(10))

print((lambda num: num ** 2)(10))
