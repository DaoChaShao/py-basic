
# 双参数

def add(x, y):
    return x + y


print(add(2, 3)) # 5

# 匿名函数
add_lambda = lambda x, y: x + y
print(add_lambda(2, 3))  # 5

print((lambda x, y: x + y)(2, 3))

lambda_func = lambda x, y: (x + y, x - y)
print(lambda_func(2, 3))  # (5, -1)
