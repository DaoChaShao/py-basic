
# 多态

# 面对对象三大特性 - 封装、继承和多态

# 多态 不同于 不同于 子类对象 调用相同的 父类方法，产生不同的执行结果
# - 多态 可以 增加代码的灵活度
# - 以 继承 和 重写父类方法 为前提
# - 是调用方法的技巧， 不会影响到类的内部设计

# 案例演练
# 1.在Dog中封装game
# - 普通狗只是简单的玩耍
# 2.定义哮天犬继承Dog，并且重写game
# 3.定义person，并且封装一个和够玩的方法
# - 在方法内部，直接让狗对象调用game方法

# *****************
# Person
# -----------------
# name
# -----------------
# game_with_dog(self):
# *****************

# *****************
# Dog
# -----------------
# name
# -----------------
# game(self):
# *****************

# *****************
# XiaoTianQuan
# -----------------
# name
# -----------------
# game(self)
# *****************

class Dog(object):

    def __init__(self, dog_name):
        self.name = dog_name

    def game(self):
        print(f"{self.name} 蹦蹦跳跳的玩耍···")

class XiaoTiaoQuan(Dog):

    # 方法重写(方法名称一致，覆盖重写)
    def game(self):
        print(f"{self.name} 在天上撒欢···")

class Person(object):

    def __init__(self, person_name):
        self.name = person_name

    def game_with_god(self, dog):
        print(f"{self.name} 和 {dog.name} 在快乐的玩耍···")

        # 让狗玩耍
        dog.game()

# 创建狗对象
#dog_variable = XiaoTiaoQuan("小舔犬")
    # 输出：二眼怪 和 小舔犬 在快乐的玩耍···
dog_variable = Dog("小舔犬")
    # 输出：小舔犬 蹦蹦跳跳的玩耍···

# 创建人对象
person_variable = Person("二眼怪")

# 调用玩耍
person_variable.game_with_god(dog_variable)
print()
