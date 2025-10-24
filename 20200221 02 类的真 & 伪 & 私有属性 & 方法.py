
# 私有 和 伪私有 属性和方法

# 私有属性：对象 不希望公开的 属性
# 私有方法：对象 不希望公开的 方法

# 1.私有属性和私有方法

# 1.1 语法：
# - __私有属性
# - __私有方法

# *****************
# Women
# -----------------
# name
# __age
# -----------------
# __init__(self, name):
# __str__(self):
# *****************

print()

# 1.2 常规类
class Women:

    def __init__(self, name):

        self.name = name
        self.age = 18

    def secret(self):

        print(f"{self.name} 的年龄：{self.age}。")

person = Women("小美")

print(person.age) # 输出：18
person.secret() # 输出：小美 的年龄：18。
print()

# 1.3 私密类 - 私密属性 (对比)
class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def secret(self):

        print(f"{self.name} 的年龄：{self.__age}。")

person = Women("小美")

# 在对象的方法外部，不可以直接访问私有属性
#print(person.__age) # 输出：'Women' object has no attribute '__age'

# 在对象的方法内部，可以直接访问私有属性
person.secret() # 输出：小美 的年龄：18。
print()

# 1.4 私密类 - 私密方法 (对比)
class Women:

    def __init__(self, name):

        self.name = name
        self.age = 18

    def __secret(self):

        print(f"{self.name} 的年龄：{self.age}。")

person = Women("小美")

print(person.age) # 输出：18

# 在对象的方法外部，不可以直接访问私有方法
#person.__secret() # 输出：'Women' object has no attribute '__secret'
print()

# 2.伪私有属性和私有方法
# >>> 不推荐使用和尝试访问私有属性和方法 <<<

# 语法：
# - 在 名称 前面加上 _类名
# - 即：_类名私有属性名称 - _Women__age
# - 即：_类名私有方法名称 - _Women__secret()

class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):

        print(f"{self.name} 的年龄：{self.__age}。")

person = Women("小美")

# 在对象的方法外部，重新访问私有属性
print(person._Women__age) # 输出：18

# 在对象的方法外部，重新访问私有方法
person._Women__secret() # 输出：小美 的年龄：18。
print()
