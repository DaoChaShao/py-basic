
# shutil 模块提供了对文件和目录的高级操作，如文件复制、移动、删除、压缩与解压等。

import shutil


# 移动文件
def shutil_move_file():
    shutil.move(
        'file_shutil_letters/file_a.txt',  # 源文件
        'file_shutil_numbers'  # 目标文件目录（文件夹）
    )


# 复制文件
# 复制2个文件句柄：把文件1中的内容复制到文件2中，文件1和文件2都必须存在。
def shutil_copy_and_exist_file():
    file_01 = open('file_shutil_numbers/file_1.txt', 'rb')
    file_02 = open('file_shutil_letters/file_1_copy.txt', 'wb')

    shutil.copyfileobj(
        file_01,  # 读取文件句柄
        file_02  # 往对应文件中，写入文件句柄
    )


def shutil_move_file_content():
    shutil.copyfile('file_shutil_numbers/file_1.txt', 'file_shutil_letters/file_b.txt')  # 复制文件内容


def shutil_copy_file_all():
    shutil.copy('file_shutil_numbers/file_1.txt', 'file_shutil_letters/file_1_copy_all.txt')  # 复制文件，包括：文件权限、文件属性、文件内容等。


if __name__ == '__main__':
    # 移动文件
    # shutil_move_file()
    # 复制文件
    # shutil_copy_and_exist_file()
    # 复制文件内容（复制文件内容）
    # shutil_move_file_content()
    # 复制文件内容，包括：文件权限、文件属性、文件内容等。
    shutil_copy_file_all()