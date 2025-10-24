# 面向对象(之前都属于面向过程)
# - 面向对象是更大的封装
# - 根据 职责 在 一个对象中 封装 多个方法
# -- 首相确定 职责 - 要做的事情(方法)
# -- 根据 职责 不同，确定不同的 对象， 在对 对象 内部封装不同的 方法(多个)
# -- 最后完成的代码，就是顺序的让 不同的对象 调用 不同的方法

# 1.类
# - 在程序开发中，应该 >> 先有类，再有对象 <<

# 1.1 类的基本内容
# - 相当于制造飞机时的图纸，是一个模板，是负责创建对象的
# - 特征 被称为 属性
# - 行为 被称为 方法
# - 类 只能有一个
# - 类 中定义了什么 属性和方法，对象 中就有什么属性和方法，不可能多，也不可能少

# 1.2 类的设计
# 类的设计，通常要满足三个 要素

# 1.2.1 类名：这类食物的名字要满足——大驼峰命名法
# - 大驼峰命名法：MyName
# - 类名的确定 - 名词提炼法：分析业务流程，出现的名词就是要找到的类

# 1.2.2 属性：这类事物具有什么特征
# - 对 对象的特征描述，可以定义为 属性

# 1.2.3 方法：这类事物就有什么行为
# - 对象具有的行为(动词)，可以定义为 方法

# 类的练习一
# - 小明 18岁，身高1.70，每天跑步，之后去吃东西
# - 小美 17岁，身高1.65，每天不跑步，直接吃东西
# -----------------
# >>> person - 类名
# -----------------
# >>> name - 属性
# >>> age - 属性
# >>> height - 属性
# -----------------
# >>> run() - 方法
# >>> eat() - 方法
# -----------------

# 类的练习二
# - 大黄 黄色，喜欢叫，摇尾巴
# -----------------
# >>> animal - 类名
# -----------------
# >>> name - 属性
# >>> color - 属性
# -----------------
# >>> shout() - 方法
# >>> shake() - 方法
# -----------------

# 2.对象
# - 在程序开发中，应该 >> 先有类，再有对象 <<

# 2.1 对象的基本内容
# - 对象 是由类创建出来的一个具体存在，可以直接使用
# - 由 哪一类 创建出来的对象，就拥有在 哪一个类 中定义：
# -- 属性
# -- 方法
# - 对象就相当于用图纸造出来的飞机
# - 对象可以有很多个
# - 类 中定义了什么 属性和方法，对象 中就有什么属性和方法，不可能多，也不可能少

# 3 dir()
# - 查看对象的 内置方法
# - 会出现：__方法名__ 的内容
# - 这些内容是：内置 方法 或 属性

# 4 简单定义类(只包含方法)

# 4.1 定义只包含方法的类名
# - 语法如下：
# -----------------
# class 类名(大驼峰，且首字母必须大写)：
# -----------------
#   def 方法1(self, 列表参数)：
#       pass
#
#   def 方法2(self, 列表参数)：
#       pass
# -----------------

# 4.2 创建对象
# - 当一个类定义完成之后，要使用这个类来创建对象
# - 语法如下：
#       对象变量 = 类名()

# 4.3 调用对象
# - 语法如下：
#       对象变量.方法1()
#       对象变量.方法2()

# 4.4 类的练习
# 需求：小猫爱吃鱼，小猫爱喝水
# 分析如下：
# - 类：猫
# - 方法：吃 和 喝

# 4.4.1 默认 参数 self
class Cat:

    def eat(self):
        # - PYTHON 里，()不自带 self 参数，需要手动填写
        # - PYTHON 里，如不手动填写参数 self，则会报错
        # - PYCHARM 中，()自带 self 参数，无需手动填写
        print("小猫爱吃鱼")

    def drink(self):
        # - PYTHON 里，()不自带 self 参数，需要手动填写
        # - PYTHON 里，如不手动填写参数 self，则会报错
        # - PYCHARM 中，()自带 self 参数，无需手动填写
        print("小猫爱喝水")


tom = Cat()
print(tom)
# 输出：<__main__.Cat object at 0x11106ff10>
# - 11106ff10 - 十六进制 (地址)

addr = id(tom)
print(f"地址为：{addr}")
# 输出：地址为：4580638480
# - 4580638480 - 十进制
print("地址为：%d" % addr)
# 输出：地址为：4580638480
# - 4580638480 - 十进制
print("地址为：%x" % addr)
# 输出：地址为：11106ff10
# - 11106ff10 十六进制

tom.eat()  # 输出：小猫爱吃鱼
tom.drink()  # 输出：小猫爱喝水

lazy_cat = Cat()  # 和上面的一只猫不一样，两只猫不在一个地址
print(lazy_cat)  # 输出：<__main__.Cat object at 0x10972f1f0>

lazy_cat.eat()  # 输出：小猫爱吃鱼
lazy_cat.drink()  # 输出：小猫爱喝水

lazy_cat_2 = lazy_cat  # 和上一只猫一样，两只猫在一个地址，是一只猫
print(lazy_cat_2)  # 输出：<__main__.Cat object at 0x10972f1f0>
print()


# 4.4.2 在类的外部，设置对象属性
# - 给对象设置属性非常容易，但是：>>> 不推荐使用 <<<
# - 因为：对象属性的封装应该封装在类的内部
# - 只需要通过 类 外部的代码直接通过即可，设置一个属性即可

class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()  # 对象的设置
tom.name = "汤姆"
# 属性已经增加
# 属性的增加，必须要在对象设置之后，不然无法调用到类的内部
# 但这里面没有输出控制台
# >>> 不推荐使用 <<<
# - 一旦位置(行数)出现的过早或者过晚，均会报错

tom.eat()
tom.drink()
print()


# 4.4.2 利用 self 在类封装的方法中输出对象特征
class Cat:

    # self 哪一个对象调用该方法，self 就是哪一个对象的引用
    # tom 调用，self 就是 tom 的引用
    def eat(self):
        print(f"{self.name} 爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


tom = Cat()
tom.name = "汤姆"

tom.eat()  # 输出：汤姆 爱吃鱼
tom.drink()  # 输出：小猫爱喝水

lazy_cat = Cat()
lazy_cat.name = "大懒猫"

lazy_cat.eat()  # 输出：大懒猫 爱吃鱼
lazy_cat.drink()  # 输出：小猫爱喝水
print()


# 4.5 初始化方法 - 是 专门 用来定义一个类 具有哪些属性 的方法
# - 当类名创建对象是，会自动执行以下操作：
# -- 为对象的内存中 分配空间 -- 创建对象
# -- 为对象的属性 设置初始值 -- 初始化方法(init)
# 这个 初始化方法 就是 __init__ 方法， __init__ 是对象的内置方法

class Cat:

    def __init__(self):
        print("这是一个初始化方法")


# 使用类名()创建对象时，会自动调用初始化方法(__init__)
tom = Cat()  # 输出：这是一个初始化方法
print()


# 4.6 在初始化方法内部定义属性
# - 简化对象的创建
# - 个人理解：相当于整个 类 的 >最开始的基础设定<
# - 在初始化方法内部使用 > self.属性名 = 属性的初始值 < 就可以定义属性
# - 定义属性之后，再使用 类 创建的对象，都会拥有该属性

# 4.6.1 注意调用顺序一
class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print(f"{self.name} 爱吃鱼")


tom = Cat()

# print(tom) # 输出：<__main__.Cat object at 0x10cfd0f10>
print(tom.name)
# 输出：这是一个初始化方法
#      汤姆
print()


# 4.6.2 注意调用顺序二
class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print(f"{self.name} 爱吃鱼")


tom = Cat()

tom.eat()
# 输出：这是一个初始化方法
#      汤姆 爱吃鱼
# print(tom) # 输出：<__main__.Cat object at 0x10cfd0f10>
print(tom.name)
#      汤姆
print()


# 4.6.3 注意调用顺序三
class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print(f"{self.name} 爱吃鱼")


tom = Cat()

# print(tom) # 输出：<__main__.Cat object at 0x10cfd0f10>
print(tom.name)
# 输出：这是一个初始化方法
#      汤姆
tom.eat()
#      汤姆 爱吃鱼
print()


# 4.6.4 注意调用顺序四
class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print(f"{self.name} 爱吃鱼")


tom = Cat()

tom.eat()
# 输出：这是一个初始化方法
#      汤姆 爱吃鱼
# print(tom) # 输出：<__main__.Cat object at 0x10cfd0f10>
print(tom.name)
#      汤姆
tom.eat()
# 输出：汤姆 爱吃鱼
print()


# 4.7 在 类的内部 ，使用参数设置 属性的初始值

class Cat:

    def __init__(self, new_name):  # 添加 形参new_name

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # 在类的内部 用形参 设定属性的初始值
        self.name = new_name

    def eat(self):
        print(f"{self.name} 爱吃鱼")


tom = Cat(input("输入第一只猫的名字："))  # 输入：大懒猫

tom.eat()
# 输出：这是一个初始化方法
#      大懒猫 爱吃鱼
# print(tom) # 输出：<__main__.Cat object at 0x10cfd0f10>
print(tom.name)
#      大懒猫

lazy_cat = Cat(input("输入第二只猫的名字："))  # 加菲猫

lazy_cat.eat()
# 输出：这是一个初始化方法
#      加菲猫 爱吃鱼
print(lazy_cat.name)  # 输出：加菲猫
print()


# 4.8 __del__ 和 __str__ (str返回值必是字符串)
class Cat:

    def __init__(self, new_name):  # 方法初始化 设置后

        self.name = new_name

        print(f"{self.name} 来啦")

    def __del__(self):
        # PYTHON 里不主动运行，不运行
        # PYCHARM 里主动运行

        print(f"{self.name} 去了")

    def __str__(self):
        return "我是小猫"

    def eat(self):  # 方法一
        print(f"{self.name} 爱吃鱼")

    def drink(self):  # 方法二
        print(f"{self.name} 爱喝水")


variable = Cat(input("输入姓名："))
# 输入：老弟
# 输出：老弟 来啦
print(variable)  # 输出：我是小猫 - 如果没有返回值，就是地址

variable.eat()  # 输出：老弟 爱吃鱼
variable.drink()  # 输出：老弟 爱喝水
print()


# 4.8 对比组 __del__ 和 __str__ (str返回值必是字符串)
class Cat:

    def __init__(self, new_name):  # 方法初始化 设置后

        self.name = new_name

        print(f"{self.name} 来啦")

    def __del__(self):
        # PYTHON 里不主动运行，不运行
        # PYCHARM 里主动运行

        print(f"{self.name} 去了")

    def __str__(self):
        return f"我是小猫 {self.name}"

    def eat(self):  # 方法一
        print(f"{self.name} 爱吃鱼")

    def drink(self):  # 方法二
        print(f"{self.name} 爱喝水")


variable = Cat(input("输入姓名："))
# 输入：老弟
# 输出：老弟 来啦
print(variable)  # 输出：我是小猫 老弟 - 如果没有返回值，就是地址

variable.eat()  # 输出：老弟 爱吃鱼
variable.drink()  # 输出：老弟 爱喝水
print()

# 4.9 封装案例
# 人人爱跑步
"""
要求：
1.小明体重150斤
2.小明每次跑步，会减肥 1 斤
3.小明每次吃东西，会增加 2 斤

4.小美体重90斤
5.小美每次跑步，会减肥 1 斤
6.小美每次吃东西，会增加 2 斤

分析：
# *****************
# person
# -----------------
# name
# weight
# -----------------
# __int__(self,name,weight)
# __str__(self)
# run(self)
# eat(self)
# *****************
"""


class Person:

    # 方法初始化
    def __init__(self, name_enter, weight_enter):
        # self.属性 = 形参
        self.name = name_enter
        self.weight = weight_enter

    def __str__(self):
        return "我的名字：%s，体重：%03d斤" % (self.name, self.weight)

    def run(self):  # 方法一

        print(f"{self.name} 爱跑步，运动运动能减肥！")
        self.weight -= 1

    def eat(self):  # 方法二

        print(f"{self.name} 是吃货，吃完这顿再减肥！")
        self.weight += 2


person_info_enter = Person(input("输入姓名："), int(input("输入体重(斤)：")))

person_info_enter.run()
person_info_enter.eat()
print()
print(person_info_enter)
print()
