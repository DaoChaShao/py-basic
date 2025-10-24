with open('data/20240408 00 file data（测试）.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # 去掉首尾空白字符
        if line and not line.isspace():  # 检查是否为空行
            print(line)
