
# 传统查找
get_input = input("请输入要查找的数字：")

example_list_01 = [i for i in range(10)]

for i in example_list_01:
    if int(get_input) == i:
        print("找到了！")
        break
else:
    print("没有找到！")


# 二分法查找
get_input = int(input("请输入要查找的数字："))

example_list_02 = [i for i in range(10)]

left = 0
right = len(example_list_02) - 1

while left <= right:  # 循环条件：如果左边界小于等于右边界
    mid = (left + right) // 2  # 计算中间位置
    if get_input == example_list_02[mid]:  # 如果输入值等于中间位置的值
        print(f"找到了！位置 {mid}")
        break
    elif get_input < example_list_02[mid]:  # 如果输入值小于中间位置的值
        right = mid - 1
    else:  # 如果输入值大于中间位置的值
        left = mid + 1
else:
    print("没有找到！")
