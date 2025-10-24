# 类 的继承

# 面对对象的三大特性
# - 封装 根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中
# - 继承 实现代码的重用，相同的代码不需要重复的编写
# - 多态 不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度

# 继承：子类 拥有 父类 的所有 属性 和 方法 (又叫做继承的传递性)
# 语法：
#   class 类名(父类名):
#       pass

# 常规 类
class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def bark(self):
        print("汪汪叫")


animal_variable = Animal()

animal_variable.eat()  # 输出：吃
animal_variable.drink()  # 输出：喝
animal_variable.run()  # 输出：跑
animal_variable.sleep()  # 输出：睡
print()

dog_variable = Dog()

dog_variable.eat()  # 输出：吃
dog_variable.drink()  # 输出：喝
dog_variable.run()  # 输出：跑
dog_variable.sleep()  # 输出：睡
dog_variable.bark()  # 输出：汪汪叫
print()


# 继承 类
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    #    def eat(self):
    #        print("吃")
    #    def drink(self):
    #        print("喝")
    #    def run(self):
    #        print("跑")
    #    def sleep(self):
    #        print("睡")
    def bark(self):
        print("汪汪叫")


animal_variable = Animal()

animal_variable.eat()  # 输出：吃---
animal_variable.drink()  # 输出：喝---
animal_variable.run()  # 输出：跑---
animal_variable.sleep()  # 输出：睡---

dog_variable = Dog()

dog_variable.eat()  # 输出：吃---
dog_variable.drink()  # 输出：喝---
dog_variable.run()  # 输出：跑---
dog_variable.sleep()  # 输出：睡---
dog_variable.bark()  # 输出：汪汪叫
print()


# 总结
# - Dog 是 Animal 的子类，Animal 是 Dog 的父类，Dog 从 Animal 继承
# - Dog 是 Animal 的派生类，Animal 是 Dog 的基类，Dog 从 Animal 派生

class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("- 我会飞 -")


xtq_variable = XiaoTianQuan()

xtq_variable.eat()  # 输出：吃---
xtq_variable.drink()  # 输出：喝---
xtq_variable.run()  # 输出：跑---
xtq_variable.sleep()  # 输出：睡---
xtq_variable.bark()  # 输出：汪汪叫
xtq_variable.fly()  # 输出：- 我会飞 -
print()


# 1.单继承
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("- 我会飞 -")


class Cat(Animal):

    def catch(self):
        print("抓抓抓")


xtq_variable = XiaoTianQuan()

# xtq_variable.catch()
# 输出：'XiaoTianQuan' object has no attribute 'catch'
# 不能调用未继承的方法
print()


# 2.方法的重写
# - 当 父类 的方法实现不能满足子类需要时，可以对方法进行 重写(override)
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("- 我是哮天犬，我会飞 -")

    def bark(self):
        print("- 我是哮天犬，嘤嘤嘤 - ")


xtq_variable = XiaoTianQuan()

xtq_variable.bark()  # 输出：- 我是哮天犬，嘤嘤嘤 -
# 如果子类中，有重写方法，则优先调用子类
# 子类中不存在重写的方法，再调用父类
print()


# 4.在子类中对父类进行方法进行调用
# PYTHION 2.0 后，使用 super()
# - 语法：super().父类方法
# PYTHION 2.0 前，则使用：父类名.方法(self)

# PYTHONE 2.0 后
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    # 方法重写
    def bark(self):
        print("- 我是哮天犬，嘤嘤嘤 - ")

        # 在子类中调用父类方法
        super().bark()

        # 子类调用父类方法后输出
        print("@#$%&")


xtq_variable = XiaoTianQuan()

xtq_variable.bark()
# 输出：- 我是哮天犬，嘤嘤嘤 -
#      汪汪叫
#      @#$%&
print()


# PYTHONE 2.0前
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    # 方法重写
    def bark(self):
        print("- 我是哮天犬，嘤嘤嘤 - ")

        # 在子类中调用父类方法
        Dog.bark(self)

        # 子类调用父类方法后输出
        print("@#$%&")


xtq_variable = XiaoTianQuan()

xtq_variable.bark()
# 输出：- 我是哮天犬，嘤嘤嘤 -
#      汪汪叫
#      @#$%&
print()


# 5.父类私有属性和方法的案例

class Dad:

    def __init__(self):
        self.num_1 = 100
        self.__num_2 = 200

    def __test(self):
        print(f"私有方法：{self.num_1} 和 {self.__num_2}")

    def test(self):
        print(f"父类的共有方法内容为：{self.__num_2}")
        # 输出：父类的共有方法内容为：200
        # 类的内部，可以访问私有属性

        self.__test()


class Son(Dad):

    def demo(self):
        # 访问父类的私有属性
        print(f"访问父类的私有属性 num_1：{self.num_1}")
        # 输出：访问父类的公有属性 num_1：100
        # 子类能访问父类的公有方法

        # print(f"访问父类的私有属性 __num_2：{self.__num_2}")
        # 输出：'Son' object has no attribute '_Son__num_2'
        # 子类不能访问父类的私有属性

        # 调用父类的私有方法
        # self.__test()
        # print("调用父类的私有方法")
        # 输出：'Son' object has no attribute '_Son__test'
        # 子类不能调用父类的私有方法
        self.test()
        # 输出：父类的共有方法
        # 子类能调用父类的公有方法


variable = Son()

print(variable)  # 输出：<__main__.Son object at 0x111242a90>
print(variable.num_1)  # 输出：100
# print(variable.__num_2)
# 输出：'Son' object has no attribute '__num_2'
# 在外部，不能访问私有属性
# print(variable.__test)
# 输出：'Son' object has no attribute '__test'
# 在外部，不能调用私有方法
print()

variable.demo()
print()


# 2.多继承 - 继承多个父类
# 语法：class 子类名(父类名1， 父类名2，···)
class Dad1:

    def dad_1_method(self):
        print("父类方法一")


class Dad2:

    def dad_2_method(self):
        print("另一个父类方法一")


class Son(Dad1, Dad2):  # 继承所有父类的属性和方法

    pass


bitch = Son()

bitch.dad_1_method()  # 输出：父类方法一
bitch.dad_2_method()  # 输出：另一个父类方法一
print()


# 2.1 PYTHON 中的 MRO - 方法搜索顺序 或 方法解决顺序
# - 类 中的 内置属性 __mro__ 可以查看 方法 搜索顺序
# - MRO 是 method resolution order
# - 用于 在多继承是判断 方法、属性 的调用 路径

class Dad1:

    def test(self):
        # 尽量避免相同方法名称
        # 否则，先继承谁，就只显示谁
        print("父类方法一")

    def demo(self):
        # 尽量避免相同方法名称
        # 否则，先继承谁，就只显示谁
        print("父类方法二")


class Dad2:

    def test(self):
        # 尽量避免相同方法名称
        # 否则，先继承谁，就只显示谁
        print("另一个父类方法一")

    def demo(self):
        # 尽量避免相同方法名称
        # 否则，先继承谁，就只显示谁
        print("另一个父类方法二")


class Son(Dad1, Dad2):  # 继承所有父类的属性和方法

    pass


bitch = Son()

bitch.test()  # 输出：父类方法一
bitch.demo()  # 输出：父类方法二

# 确定 bitch 对象调用的方法顺序
# - 优先子内部
# - 其次是继承顺序
# print(bitch.__mro__) # PYCHARM可显示，PYTHON中报错
print()
