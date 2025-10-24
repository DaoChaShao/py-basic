
file = open('data/20240408 00 file data（测试）.txt', 'r', encoding='utf-8')

while True:
    details = file.readline()
    if len(details) == 0:
        break
    output = details.strip()
    print(output)
# 关闭文件
file.close()
print()
