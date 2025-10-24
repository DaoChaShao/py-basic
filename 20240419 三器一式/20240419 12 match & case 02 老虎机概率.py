from random import randint

from utils.decorator import timer, beautifier
from utils.highlighter import red, green, yellow, lines


@beautifier
@timer
def roll_dice(in_times: int) -> tuple[int, float]:
    # 设定计数器
    triple = 0
    double = 0
    single = 0

    # 模拟投掷n次骰子
    for i in range(in_times):
        roll = [randint(1, 6) for _ in range(3)]
        match roll:
            case [6, 6, 6]:
                triple += 1
            case [6, 6, _] | [6, _, 6] | [_, 6, 6]:
                double += 1
            case [6, _, _] | [_, 6, _] | [_, _, 6]:
                single += 1

    # 计算百分比
    triple_percentage = triple / in_times * 100
    double_percentage = double / in_times * 100
    single_percentage = single / in_times * 100

    # 输出结果
    print(f"共进行了 {in_times} 次投骰子，结果如下：")
    lines()
    print(f"投中三个6的次数有：{red(triple)} 次，投中率为：{red(triple_percentage)} %")
    print(f"投中两个6的次数有：{yellow(double)} 次，投中率为：{yellow(double_percentage)} %")
    print(f"投中一个6的次数有：{green(single)} 次，投中率为：{green(single_percentage)} %")

    return triple, triple_percentage


if __name__ == "__main__":
    roll_times = 1_000_000
    roll_dice(roll_times)
