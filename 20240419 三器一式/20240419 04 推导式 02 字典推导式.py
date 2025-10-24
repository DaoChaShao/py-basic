
from faker import Faker

fake_list = [Faker(locale='zh_CN').name() for i in range(10)]
print(fake_list)

example_dict_01 = {i: fake_list[i] for i in range(len(fake_list))}
print(example_dict_01)

example_dict_02 = {i+1: fake_list[i] for i in range(len(fake_list))}
print(example_dict_02)
