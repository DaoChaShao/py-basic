# 类的 单例模式和设计概念

# 设计模式
# - 为某一特定问题设计的解决方案
# - 使用 设计模式 视为了可重用代码、让代码更容易被他人理解、保证代码可靠性

# 单例设计模式
# - 目的——让 类 创建的对象，在系统中 只有 唯一的一个实力
# - 每一次执行 类名() 返回的对象，内存地址都是相同的

# 应用场景
# - 音乐播放 对象
# - 回收站 对象
# - 打印机 对象

# 1.__new__(cls)方法 - 本身是自动的，也是被动的分配空间和地址
# - 在内容中为对象 分配空间
# - 返回 对象的引用

# 2.重写__new__方法 - 是主动的分配空间和地址
# - 一定要 return super().__new__(cls)
# - 否则 PY 的解释器 得不到 分配了的空间的 对象引用， 就不会调用对象的初始化方法
# - __new__ 是一个静态方法，在调用时需要 主动传递 cls 参数

# ***************************
# ---------------------------
# ---------------------------
# ***************************

# ***************************
# MusicPlayer
# ---------------------------
# __new__(cls):
# __init__(self):
# ***************************

# 2.1 参照组
class MusicPlayer(object):

    def __init__(self):
        print("播放器初始化")


song = MusicPlayer()

print(song)
# 输出：播放器初始化
#      <__main__.MusicPlayer object at 0x10806ff10>
print()


# 2.2 对比组 1
class MusicPlayer(object):

    # 重写__new__方法
    def __new__(self, *args, **kwargs):
        # 创建对象时，__new__方法会被自动调用
        print("重写__new__，空间被创建，空间被分配")

    def __init__(self):
        print("播放器初始化")


song = MusicPlayer()

print(song)
# 输出：重写__new__，空间被创建，空间被分配
#      None
#       - 重写__new__方法，一定要 return super().__new__(cls)
#         否则，识别不到
print()


# 2.3 对比组 2
class MusicPlayer(object):

    # 重写__new__方法
    def __new__(cls, *args, **kwargs):
        # 创建对象时，__new__方法会被自动调用
        print("重写__new__，空间被创建，空间被分配")

        # 为对象分配空间
        instance = super().__new__(cls)
        # 调用类方法，使用super().
        # 父类方法的结果 用一个变量接收

        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


song = MusicPlayer()

print(song)
# 输出：重写__new__，空间被创建，空间被分配
#      播放器初始化
#      <__main__.MusicPlayer object at 0x1044fc370>
print()


# 3.储存地址相同 - 案例

# 3.1 基本组
class MusicPlayer(object):
    pass


# 创建多个对象，证明地址是否一致 >>> 两个地址不一致 <<<
song_1 = MusicPlayer()
print(song_1)
# 输出：<__main__.MusicPlayer object at 0x10b10e5e0>
print()

song_2 = MusicPlayer()
print(song_2)
# 输出：<__main__.MusicPlayer object at 0x10b10e4f0>
print()


# 3.2 对照组 1 - 重写__new__
class MusicPlayer(object):
    # 创建类属性
    # 记录第一个被创建对象的引用
    # 因为对象还未被创建，所以也不存在地址
    # 所以赋值部分应该为 None
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性 instance 是否时空对象
        # 类属性查看 cls.
        if cls.instance is None:
            # 如果不是空对象，则调用父类方法，主动为第一个对象分配空间和地址
            # 调用父类方法 super().
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance


# 创建多个对象，证明地址是否一致 >>> 两个地址一致 <<<
song_1 = MusicPlayer()
print(song_1)
# 输出：<__main__.MusicPlayer object at 0x1047e53d0>
print()

song_2 = MusicPlayer()
print(song_2)
# 输出：<__main__.MusicPlayer object at 0x1047e53d0>
print()


# 3.3 对照组 2 - 初始化方法——初始化动作被执行两次
class MusicPlayer(object):
    # 创建类属性
    # 记录第一个被创建对象的引用
    # 因为对象还未被创建，所以也不存在地址
    # 所以赋值部分应该为 None
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性 instance 是否时空对象
        # 类属性查看 cls.
        if cls.instance is None:
            # 如果不是空对象，则调用父类方法，主动为第一个对象分配空间和地址
            # 调用父类方法 super().
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 初始化动作
        print("初始化播放器")


# 创建多个对象，证明地址是否一致 >>> 两个地址一致 <<<
song_1 = MusicPlayer()
print(song_1)
# 输出：初始化播放器
#      <__main__.MusicPlayer object at 0x108bce4c0>
print()

song_2 = MusicPlayer()
print(song_2)
# 输出：初始化播放器
#      <__main__.MusicPlayer object at 0x1047e53d0>
print()


# 3.4 对照组 3 - 初始化方法——初始化动作被执行一次
# - 定义一个类属性 init_flag 标记是否 执行初始化动作，初始值为FALSE
# - 在 __init__ 方法中，判断 init_flag
# - 如果为 FALSE，就执行初始化动作，否则就不执行
# - 然后将 init_flag 设置为 TRUE
# - 这样，再 自动 调用 __init__ 方法时，初始化动作就不会再被执行

class MusicPlayer(object):
    # 创建__new__类属性
    # 记录第一个被创建对象的引用
    # 因为对象还未被创建，所以也不存在地址
    # 所以赋值部分应该为 None
    instance = None

    # 创建__init__类属性
    # 记录是否执行过初始化的动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 判断类属性 instance 是否时空对象
        # 类属性查看 cls.
        if cls.instance is None:
            # 如果不是空对象，则调用父类方法，主动为第一个对象分配空间和地址
            # 调用父类方法 super().
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 判断类属性是否执行过初始化动作
        # 如果执行过，则直接返回
        # 类属性查找——类名.属性名
        if MusicPlayer.init_flag:
            # 因为前面类属性：init_flag = False
            # 所以此处：if MusicPlayer.init_flag: 相当于 if init_flag = False:
            return

        # 如果没有执行，则执行初始化动作
        # 初始化动作
        print("初始化播放器")

        # 当执行完初始化动作之后，修改类属性标记
        MusicPlayer.init_flag = True


# 创建多个对象，证明地址是否一致 >>> 两个地址一致 <<<
song_1 = MusicPlayer()
print(song_1)
# 输出：初始化播放器
#      <__main__.MusicPlayer object at 0x108bce4c0>
print()

song_2 = MusicPlayer()
print(song_2)
# 输出：<__main__.MusicPlayer object at 0x1047e53d0>
print()
