
# 身份运算符
# is - 判读两个标识符是同一个对象
# - x is y ，类似 id(x) = id(y)
# is not - 判断两个标识符不是同一个对象
# - x is not y ，类似 id(x) != id(y)

# 1.is 和 == 的区别
# is 用于判断 两个变量 引用对象是否为同一个
# == 用于判断 引用量变的值 是否相等

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # 输出：True
print(a is b) # 输出：False
