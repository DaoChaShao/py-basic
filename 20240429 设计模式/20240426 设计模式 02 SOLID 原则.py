"""
SOLID原则：
1. Single Responsibility Principle (SRP)：一个类只负责一项职责。
2. Open-Closed Principle (OCP)：软件实体应该对扩展开放，对修改关闭。
3. Liskov Substitution Principle (LSP)：子类必须能够替换其基类。
4. Interface Segregation Principle (ISP)：使用多个专门的接口比使用单一的总接口更好。
5. Dependency Inversion Principle (DIP)：高层模块不应该依赖低层模块，两者都应该依赖其抽象。
"""

from abc import ABCMeta, abstractmethod

from utils.highlighter import lines


class Animal(metaclass=ABCMeta):
    """ 设置统一的接口 """

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class LandAnimal(metaclass=ABCMeta):
    """ 陆生动物分接口 """

    @abstractmethod
    def walk(self):
        pass


class AquaticAnimal(metaclass=ABCMeta):
    """ 海洋动物分接口 """

    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    """ 天空动物分接口 """

    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print("Tigers can walk")

    def tiger_move(self):
        Tiger.walk(self)
        lines()


class Frog(LandAnimal, AquaticAnimal):
    def walk(self):
        print("Frogs can walk")

    def swim(self):
        print("Frogs can swim")

    def frog_move(self):
        Frog.walk(self)
        Frog.swim(self)
        lines()


class Eagle(SkyAnimal, LandAnimal):
    def fly(self):
        print("Eagles can fly")

    def walk(self):
        print("Eagles can walk")

    def eagle_move(self):
        Eagle.fly(self)
        Eagle.walk(self)
        lines()


if __name__ == '__main__':
    tiger = Tiger()
    frog = Frog()
    eagle = Eagle()

    tiger.tiger_move()
    frog.frog_move()
    eagle.eagle_move()
