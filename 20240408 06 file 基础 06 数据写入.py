# 1.将 桌子 2200 1 写进data中
# 2.将 椅子 1800 1 写进data中

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
    # 以 'r' 模式打开文件
    with open('data/20240408 00 file data（测试）.txt', 'r', encoding='utf-8') as file:
        # 获取文件的全部内容
        lines = file.readlines()

    # 以 'r+' 模式打开文件
    with open('data/20240408 00 file data（测试）.txt', 'r+', encoding='utf-8') as file:
        # 如果文件有多于一行的内容
        if len(lines) > 1:
            # 将除了最后一行以外的内容重新写入文件
            file.truncate(0)  # 先删除所有内容
            file.writelines(lines[:-1])  # 写入没有倒数第一行的所有内容
        else:
            # 文件只有一行或没有内容，则清空文件
            file.truncate(0)


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
print('【数据库】')
beauty_class.draw_lines()
open_action()
print()
# 恢复数据库原始状态
beauty_class.draw_stars()
print('【数据库】原状')
beauty_class.draw_lines()
delete_last_line()
open_action()
beauty_class.draw_stars()
print()
