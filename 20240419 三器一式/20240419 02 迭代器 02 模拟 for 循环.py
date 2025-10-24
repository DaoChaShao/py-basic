
from faker import Faker

example_list = [Faker(locale='ZH_CN').name() for _ in range(10)]
print(example_list)

# 迭代器
result_list = iter(example_list)

# 循环
while True:
    try:  # 尝试执行代码
        print(next(result_list), end=' ')  # 执行内容
    except StopIteration:  # 给出捕捉 StopIteration 异常
        break  # 该类异常步骤后，跳出循环

print()

for i in example_list:
    print(i, end=' ')
