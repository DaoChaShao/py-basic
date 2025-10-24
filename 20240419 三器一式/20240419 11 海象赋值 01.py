# := 赋值运算符
# 语法：变量名 := 表达式
# 功能：将表达式的值赋给变量名，并返回表达式的值。


import numpy as np

min_value = 1
max_value = 6
length = 3

game_list = [np.random.randint(min_value, max_value, length)]
print(f"游戏列表：{game_list}，列表类型：{type(game_list)}")
set_list = set(tuple(*game_list))
print(f"集合列表：{set_list}，集合类型：{type(set_list)}")

if (n_l := len(set_list)) == 1:
    print(f"恭喜你摇出【超级】大奖！")
elif (n_l := len(set_list)) == 2:
    print(f"恭喜你摇出大奖:)")
elif (n_l := len(set_list)) == 3:
    print(f"很遗憾你未中奖:(")
