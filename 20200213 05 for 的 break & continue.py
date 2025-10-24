
# for 的 break & continue

# break

str_one = "PYTHON"
for i in str_one:
    if i == "H": # 当某些条件成立
        print("到 H 啦，该退出啦！")
        break # 退出循环，注意：break 的缩进位置！！！
    print(i)




# continue

str_two = "YONG"
for i in str_two:
    if i == "N": # 当某些条件成立
        print("到 N 啦，该退出啦！")
        continue # 退出循环，注意：continue 的缩进位置！！！
    print(i)
