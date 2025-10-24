
# 没有元组推导式

from faker import Faker

example = (Faker(locale='zh_CN').name() for i in range(10))
print(type(example))
print(example)

# 输出数据
# for i in example:
#     print(i, end=' ')

# list, tuple, set 可以将生成器直接内的数据直接拿空
print(set(example))
print(list(example))
