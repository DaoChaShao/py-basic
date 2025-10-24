# 二进制打开文件

# 打开文件
with open('data/20240408 00 Pic.png', 'rb') as file:
    content = file.read()
    # 打开文件 = 创建该文件的名称和文件，用二进制写入使用“wb”
    with open('new 20240408.png', 'wb') as new_file:
        # 在本地文件夹中写出另一张照片
        new_file.write(content)
