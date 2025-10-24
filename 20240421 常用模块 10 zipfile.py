
import zipfile


def zip_file():
    # 创建zip文件
    with zipfile.ZipFile('zipfile_example.zip', 'w') as zipf:
        zipf.write('file_shutil_letters/file_b.txt',  # 压缩指定文件到zip文件
                   'file_z.txt')  # 是该文件在压缩文件中的名称


'''
# 文件列表
files_to_compress = ['file_shutil_letters/file_a.txt', 'file_shutil_letters/file_b.txt']

# 创建压缩文件
with zipfile.ZipFile('zipfile_example.zip', 'w') as zipf:
    # 逐个压缩文件
    for file in files_to_compress:
        # 获取文件在压缩文件中的路径和名称，这里使用文件名作为在压缩文件中的名称
        # 你也可以根据需要自定义路径和名称
        zip_file_path = file.split('/')[-1]  # 获取文件名
        zipf.write(file, zip_file_path)
'''


# 解压zip文件
with zipfile.ZipFile('zipfile_example.zip', 'r') as zipf:
    # 产看zip文件中的文件列表
    print(zipf.namelist())
    # 解压所有文件到当前目录
    zipf.extractall()
