'''
文件指针是一个特殊的变量，它指示了当前文件中的位置。在Python中，您可以使用seek()方法来移动文件指针的位置。

seek()方法有两个参数：偏移量（offset）和基准位置（whence）。

偏移量（offset）指示了移动多少个字节。如果偏移量是正数，文件指针向文件的末尾方向移动；如果是负数，文件指针向文件的开始方向移动。
基准位置（whence）指定了开始移动的参考点。有三个可能的值：
0 表示从文件的开头开始计算偏移量；
1 表示从当前位置开始计算偏移量；
2 表示从文件的末尾开始计算偏移量。
例如，file.seek(0, 2) 将文件指针移动到文件的末尾。
'''

with open('data/20240408 00 file data（测试）.txt', 'r', encoding='utf-8') as data_file:
    # 将指针放置在末尾
    last_position = data_file.seek(0, 2)
    print('当前指针被放置到：', last_position)

    # 获取当前指针位置
    position = data_file.tell()
    print('获取当前指针位置：', position)

    # 将指针放置回开头
    data_file.seek(0)

    # 读取当前位置内容
    # content_01 = data_file.readlines()
    content_02 = data_file.read(8)  # 8个占位
    # print(f'当前指针位置内容：{content_01}')
    print(f'当前指针位置内容：{content_02}')

    # 获取当前指针位置
    position = data_file.tell()
    print('获取当前指针位置：', position)  # 1个汉字占3个字节，空格占1个字节
