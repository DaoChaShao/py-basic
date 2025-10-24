# 类的属性
# 累属性 就是给 类对象 中定义的 属性
# 通常用来记录 与这个类相关 的特征
# 类属性 不会用于 记录 具体对象的特征

# 1.类的属性及访问
"""
需求：
- 定义一个 工具类
- 每件工具都有自己的 name
- 需求——知道使用这个类，创建了多少个工具对象？
"""


# ***************************
# ---------------------------
# ---------------------------
# ***************************

# ***************************
# Tool
# ---------------------------
# tool.acout
# name
# ---------------------------
# __init__(self, name):
# ***************************

class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    # 初始值为 0
    count = 0

    def __init__(self, tool_name):
        self.name = tool_name

        # 累计类属性的次数
        Tool.count += 1


# 创建工具对象
variable_1 = Tool("斧头")
variable_2 = Tool("榔头")

# 输出工具对象的总数
print(Tool.count)  # 输出：2
print()
print(f"工具对象总数：{variable_1.count}")
# 输出：工具对象总数：2
# >>> 不推荐使用 <<<
print(f"工具对象总数：{variable_2.count}")
# 输出：工具对象总数：2
# >>> 不推荐使用 <<<
print()

variable_2.count = 99

print(f"工具对象总数：{variable_2.count}")
# 输出：工具对象总数：99
print(f"类属性的实际值：{Tool.count}")
# 输出：类属性的实际值：2
print()

# 2.类的方法及调用
# 定义类方法语法：
#   @classmethod
#   def 类方法名(cls)：
#   pass

# 访问类属性
# 语法：cls.类属性名称

# 调用类方法(在外部)
# 语法：类名称.类方法名称()

"""
需求：
- 定义一个 工具类
- 每件工具都有自己的 name
- 需求——在 类 封装一个 show_tool_count 的类方法，输出使用当前这个类，创建的对象个数
"""


# ***************************
# Tool
# ---------------------------
# tool.acout
# tool_name
# ---------------------------
# __init__(self, tool_name):
# show_tool_count(cls):
# ***************************

class Tool(object):
    # 创建类属性 - 类属性名称为：count
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    # 初始值为 0
    count = 0

    # 创建类方法
    @classmethod
    def show_tool_count(cls):
        # 在类方法中访问类属性，使用 cls.类属性名称 方式
        print(f"工具对象的数量：{cls.count}")

    def __init__(self, tool_name):
        self.name = tool_name

        # 累计类属性的次数
        Tool.count += 1


# 创建工具对象
variable_1 = Tool("斧头")
variable_2 = Tool("榔头")

# (在外部)调用类方法
Tool.show_tool_count()  # 输出：工具对象的数量：2
print()


# 3.静态方法
# 开发时，如果需要在 类 中封装一个方法，这个方法：
# - 既 不需要 访问 实例属性 或者调用 实例方法
# - 也 不需要 访问 类属性 或者调用 类方法
# 此时，可以把这个方法封装成一个 静态方法

# 语法：
#   @staticmethod
#   def 静态方法名()：
#       pass

# 外部调用方法
# 语法：类名.方法名()

class Dog(object):

    # 在既不访问实例属性，也不访问类属性，就定义为静态方法
    @staticmethod
    def run():
        print("狗子，跑起来···")


# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()  # 输出：狗子，跑起来···
print()

# 如果方法内部急需要访问 实力属性，有需要访问 类属性，则封装实力属性

# 4.案例体验

"""
需求：
1.设计一个 Game 类
2.属性
 - 定义一个 类属性 top_score 记录游戏的历史最高分
 - 定义一个 实例属性 player_name 记录当前游戏的玩家姓名
3.方法
 - 静态方法：show_help 显示游戏帮助信息
 - 类方法：show_top_score 显示历史最高分
 - 实力方法：start_game 开始当前玩家的游戏
4.主程序
 - 查看帮助信息
 - 查看历史最高分
 - 创建游戏对象，开始游戏
"""


# ***************************
# Game - 类名
# ---------------------------
# Game.top_score - 类属性
# player_name - 实例属性 (实力属性要放在初始化中)
# ---------------------------
# __init__(self, player_name) - 方法初始化
# show_help() - 静态方法
# show_top_score(cls) - 类方法
# start_game(self) - 实例方法
# ***************************

# 创建类

def print_stars():
    """打印 * """
    print("*" * 27)


def print_double_lines():
    """打印 = """
    print("=" * 27)


def print_lines():
    """打印 -"""
    print("-" * 27)


class Game(object):
    """游戏运行类"""

    # 创建类属性 - 相当于全局变量
    # 创建历史分数，并把初始值设定为 0
    top_score = 0

    # 创建方法初始化
    # 设置玩家信息
    def __init__(self, player_name):
        self.name = player_name
        print_stars()
        print(f"{self.name} 已被创建")
        print("游戏即将开始")
        print_stars()
        print()

    # 创建静态方法
    # 设置游戏帮助
    @staticmethod
    def show_help():
        print_double_lines()
        print("游戏帮助信息已开始")
        print("游戏帮助信息已结束")
        print_double_lines()
        print()

    # 创建类方法
    # 设置分数展示
    @classmethod
    def show_top_score(cls):
        print_lines()
        print(f"游戏最高分为：{cls.top_score}")
        print("真TM的厉害")
        print_lines()
        print()

    # 创建实例方法
    # 运行游戏
    def start_game(self):
        print_stars()
        print(f"{self.name} 进入游戏")
        print("游戏开始")
        print_stars()
        print()


# 调用静态方法 创建查看帮助信息的对象
Game.show_help()
# 输出：===========================
#      游戏帮助信息已开始
#      游戏帮助信息已结束
#      ===========================

# 调用类方法 创建查看历史最高分的对象
Game.show_top_score()
# 输出：---------------------------
#      游戏最高分为：0
#      真TM的厉害
#      ---------------------------

# 调用实例属性 创建游戏对象
player = Game("大西瓜")
# 输出：***************************
#      大西瓜 已被创建
#      游戏即将开始
#      ***************************

# 调用实力方法 用游戏对象开启游戏
player.start_game()
# 输出：***************************
#      大西瓜 进入游戏
#      游戏开始
#      ***************************
print()
