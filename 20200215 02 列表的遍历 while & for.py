# 列表的循环遍历
# 列表遍历：访问列表中的每一个数据

# 1. while 循环遍历
# 依次打印列表中的每个数据

name_list_one = ["小熊", "小呆", "小虎", "小萌", "小明"]
              #    0      1       2      3       4

i = 0

while i < len(name_list_one):  # len()：取列表的长度
    print(name_list_one[i])
    i += 1
    # 输出：小熊
    #      小呆
    #      小虎
    #      小萌
    #      小明
print()

# 2. for 循环遍历 - 迭代遍历 (iteration)

name_list_one = ["小熊", "小呆", "小虎", "小萌", "小明"]
#    0      1       2      3       4

for j in name_list_one:
    """
    - 从列表中依次获取数据
    - 每次循环遍历中，数据都会保存在临时变量 j 中
    """

    print(j)
    # 输出：小熊
    #      小呆
    #      小虎
    #      小萌
    #      小明
print()


num_list_two = [2, 8, 5, 3, 7]

# 找出列表最小值
fake_min_value = num_list_two[0]  # 假设值，假设列表中的第一个值为最小值
list_index = 1  # list_index 是列表的下标，目标是为了通过改变下标获取下标对应的列表值

# 遍历列表中的所有值，因此list_index不能大于列表长度
while list_index < len(num_list_two):  # 这里已知num_list_one有5个值，但如果不知道的话，可以通过len()获取列表长度
    if num_list_two[list_index] < fake_min_value:  # 如果列表中的值小于假设值
        fake_min_value = num_list_two[list_index]  # 假设值则被更新为新的最小值
    list_index += 1
print(fake_min_value)
