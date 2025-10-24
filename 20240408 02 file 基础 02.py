'''
1.打开文件和关闭文件的方法一：
f = open('file.txt','r',encoding='utf-8')
print(f.read())
f.close()

2.打开文件和关闭文件的方法二：
with open('file.txt') as f:
print(f.read())
'''

with open('20240408 00 file data（测试）.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
