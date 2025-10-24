
from faker import Faker

# 传统
example_list_01 = []
for i in range(10):
    example_list_01.append(i)
print(example_list_01)

# 推导式
example_list_02 = [i for i in range(10)]
print(example_list_02)

# 推导式 + 判断
# 筛选出偶数
example_list_03 = [i for i in range(10) if i % 2 == 0]
print(example_list_03)

# 筛选出奇数
example_list_04 = [i for i in range(10) if i % 2 == 1]
print(example_list_04)

# 把奇数的平方添加至列表
example_list_05 = [i**2 for i in range(10) if i % 2 == 1]
print(example_list_05)

# 字符串
example_list_06 = [f'衣服 第 {i+1} 件' for i in range(10)]
print(example_list_06)
