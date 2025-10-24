# 1.将 桌子 2200 1 写进data中
# 2.将 椅子 1800 1 写进data中
import os
import sys

# 创建美化类
class BeautyInterface:
    def __init__(self):
        pass
    @staticmethod
    def draw_lines():
        print('-' * 30)
    @staticmethod
    def draw_stars():
        print('*' * 30)


# 创建反馈类
class GiveFeedback:
    def __init__(self):
        pass
    @staticmethod
    def message_success():
        print('您操作已成功,')
    @staticmethod
    def message_error():
        print('别瞎他妈低输！')
    @staticmethod
    def message_reentre():
        print('请您重新输入！')


# 定义打开函数
def open_action():
    file = open('data/20240408 00 file data（测试）.txt', 'r', encoding='utf-8')
    show_content = file.read()
    print(show_content)
    file.close()


# 创建写入类
class AddInfor:
    def __init__(self):
        pass
    # 定义写入名称的方法
    def add_name(self, prompt):
        file = open('data/20240408 00 file data（测试）.txt', 'a', encoding='utf-8')
        add_content = file.write('\n' + input(prompt))
        file.close()
    # 定义写入其他的方法
    def add_other_name(self, prompt):
        file = open('data/20240408 00 file data（测试）.txt', 'a', encoding='utf-8')
        add_content = file.write(' ' + input(prompt))
        file.close()

# 定义删除写入内容的函数
def delete_last_line():
    with open('data/20240408 00 file data（测试）.txt', 'r+b') as file:  # 以读取和写入二进制模式打开文件
        # 将文件指针移动到文件末尾
        file.seek(0, 2)

        # 获取文件指针的当前位置
        position = file.tell()  # position是指偏移量，可以理解成为坐标轴第一象限从左向右的偏移

        # 从文件末尾开始向前搜索
        while position > 0:  # position有偏移（最大便宜位置）
            position -= 1  # position从偏移的位置向回缩减，这里就是回扫
            file.seek(position)  # 将文件指针放置到偏移最大偏移位置
            if file.read(1) == b'\n':  # b'\n'：换行符的字节表示形式，以匹配字节；文件指针的第一个字节位置
                break

        # 截断文件到倒数第二行的末尾
        file.truncate(position)


# 创建美化对象
beauty_class = BeautyInterface()
# 创建反馈对象
feedback_class = GiveFeedback()
# 创建写入对象
add_infor = AddInfor()

# 执行函数（主体程序）
# 查询数据库
while True:
    beauty_class.draw_stars()
    print('您是否想要查看【数据库】中的内容')
    print('Y 是   N 否   0 终止程序')
    beauty_class.draw_lines()
    text = input('>>>')
    if text == 'Y' or text =='y':
        beauty_class.draw_lines()
        feedback_class.message_success()
        beauty_class.draw_stars()
        print()
        beauty_class.draw_stars()
        print('【数据库】')
        beauty_class.draw_lines()
        open_action()
        beauty_class.draw_stars()
        print()
        break
    elif text == 'N' or text =='n':
        beauty_class.draw_lines()
        feedback_class.message_success()
        print('执行后续程序！')
        beauty_class.draw_stars()
        print()
        break
    elif text == '0':
        beauty_class.draw_lines()
        feedback_class.message_success()
        print('程序即刻终止！')
        beauty_class.draw_stars()
        sys.exit()
    else:
        beauty_class.draw_lines()
        feedback_class.message_error()
        feedback_class.message_reentre()
        beauty_class.draw_stars()
        print()
# 写入数据名称
beauty_class.draw_stars()
print('请您在下行输入想要添加【数据库】的名称：')
beauty_class.draw_lines()
add_infor.add_name('>>>')
beauty_class.draw_lines()
feedback_class.message_success()
beauty_class.draw_stars()
print()
# 写入数据细节一
beauty_class.draw_stars()
print('请您在下行输入想要添加【数据库】的金额：')
beauty_class.draw_lines()
add_infor.add_other_name('>>>')
beauty_class.draw_lines()
feedback_class.message_success()
beauty_class.draw_stars()
print()
# 写入数据细节二
beauty_class.draw_stars()
print('请您在下行输入想要添加【数据库】的数量：')
beauty_class.draw_lines()
add_infor.add_other_name('>>>')
beauty_class.draw_lines()
feedback_class.message_success()
beauty_class.draw_stars()
print()
# 展示数据库写入结果
beauty_class.draw_stars()
print('【数据库】现状')
beauty_class.draw_lines()
open_action()
beauty_class.draw_stars()
print()
# 恢复数据库原始状态
beauty_class.draw_stars()
print('【数据库】原状')
beauty_class.draw_lines()
delete_last_line()
open_action()
beauty_class.draw_stars()
print()
