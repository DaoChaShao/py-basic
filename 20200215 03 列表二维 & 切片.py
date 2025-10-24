# 二维列表 & 嵌套
# 找出最大值

list_01 = [[1, 4, 3], [2, 6, 5], [9, 7, 8]]
# print(list_01)
# print(list_01[0])
# print(list_01[1])
# print(list_01[2])

# 1 4 3
# 2 6 5
# 9 8 7

num = int(len(list_01))
# print(num)
# 建立新的数据库
max_num_data = []

temporary_max_num = 0
while num > 0:  # 使用 num > 0 作为退出条件
    list_01[num - 1].sort(reverse=True)
    # print(list_01[num - 1])  # 检查排序
    temporary_max_num = list_01[num - 1][0]
    max_num_data.append(temporary_max_num)
    num -= 1   # 使用 -= 更新 num 的值
# print(max_num_data)  # 检查新数据库
max_num_data.sort(reverse=True)
max_num = max_num_data[0]

print('*' * 30)
print(max_num)
print('*' * 30)

# 切片
list_02 = [11, 42, 53, 74, 85, 23, 48, 64, 75]
print(list_02)

# 切出 2 - 5
# list_02[0:len(list_02):1]是切片默认，即整个列表，切片区间是：左闭右开
cut = list_02[2:6]
print(cut)

