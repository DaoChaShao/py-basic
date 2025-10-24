
from faker import Faker

fake_list = [Faker(locale='zh_CN').name() for i in range(10)]

example_set = {item for item in fake_list}
print(type(example_set))
print(example_set)
