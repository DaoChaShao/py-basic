# while and for ··· else
# else下方缩进的代码是指：当循环正常结束后要执行的代码


# 体验案例：连续说5遍“媳妇，我错了！”，女朋友选择原谅···

# 非 else 方法

i = 1

while i <= 5:
    print(f"第{i}遍：媳妇，我错了！")
    i += 1

print("你都承认错误了，女朋友当然是选择原谅啦！")

# 1. while···else

# while···else 的语法
# while 条件:
#   条件成立重复执行的代码
# else：
#   循环正常结束之后要执行的代码

j = 1

while j <= 5:
    print(f"第{j}遍：媳妇，我错了！")
    j += 1
else:
    print("你都承认错误了，女朋友当然是选择原谅啦！")

# 1.1 while···else 配合 break (break执行在先，else部分的代码不执行)

k = 1

while k <= 5:
    if k == 3:
        print(f"第{k}遍停吧，你这也不真诚吖，分手吧！")
        break
    print(f"第{k}遍：媳妇，我错了！")
    k += 1
else:
    print("你都承认错误了，女朋友当然是选择原谅啦！")

# 1.2 while···else 配合 continue (continue执行在先，else部分的代码继续执行)

l = 1

while l <= 5:
    if l == 3:
        print(f"第{l}遍停吧，前面的道歉一点儿也不真诚，后面的道歉必须真诚才行！")
        l += 1  # continue 之前必须要更改计数器，不然会进入死循环！！！
        continue  # continue 之前必须要更改计数器，不然会进入死循环！！！
    print(f"第{l}遍：媳妇，我错了！")
    l += 1
else:
    print("你都承认错误了，女朋友当然是选择原谅啦！")

# 2. for···else

# for···else 的语法
# for 临时变量 in 序列:
#   执行重复的代码
#   ···
# else：
#   循环正常结束之后要执行的代码

str_one = "PYTHON"

for i in str_one:
    print(i)

else:
    print("执行正常循环后，再执行 else 部分的代码")

# 2.1 for···else 配合 break (break执行在先，else部分的代码不执行)

str_two = "PYTHON"

for i in str_two:
    if i == "H":
        break
    print(i)

else:
    print("执行正常循环后，再执行 else 部分的代码")

# 2.2 for···else 配合 continue (continue执行在先，else部分的代码继续执行)

str_three = "PYTHON"

for i in str_three:
    if i == "H":
        continue  # continue 在非计数器的时候，直接使用！！！
    print(i)

else:
    print("执行正常循环后，再执行 else 部分的代码")


