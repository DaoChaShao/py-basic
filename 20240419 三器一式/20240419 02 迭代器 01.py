
from faker import Faker

# 内置函数 dir() 可以查看一个对象的所有属性和方法，包括迭代器的 __iter__ 和 __next__ 方法。

print(dir(str))  # __iter__ 表示：可以用 for 循环迭代
print(dir(list))  # __iter__
print(dir(dict))  # __iter__
print(dir(int))  # __iter__ 无
print(dir(bool))  # __iter__ 无

# 所有可迭代的对象内部都含有一个 __iter__ 方法
# 该方法返回一个迭代器对象
# 该对象具有 __next__ 方法，该方法返回下一个元素。

# 迭代器 iterator

example_list = [Faker(locale='ZH_CN').name() for _ in range(5)]
print(example_list)

result_list = iter(example_list)

print(next(result_list))
print(next(result_list))
print(next(result_list))
print(next(result_list))
print(next(result_list))

# 迭代器只能使用一次，一旦迭代完成，就不能再次使用。

example_set = {Faker(locale='ZH_CN').name() for _ in range(5)}
print(type(example_set))
print(example_set)

result_set = iter(example_set)

print(next(result_set))
print(next(result_set))
print(next(result_set))
print(next(result_set))
print(next(result_set))

# 迭代器只能使用一次，一旦迭代完成，就不能再次使用。

