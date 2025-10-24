
class Person:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property
    def age(self):
        return 2024 - self.birth_year  # 计算年龄

    @classmethod
    def from_birth_year(cls, birth_year):
        age = 2024 - birth_year  # 计算年龄
        return cls(age)


# 使用@property装饰器将方法转换为属性
p1 = Person(1990)
print(p1.age)  # 直接访问属性，无需调用方法

# 使用@classmethod装饰器创建类方法
p2 = Person.from_birth_year(1990)
print(p2.age)
