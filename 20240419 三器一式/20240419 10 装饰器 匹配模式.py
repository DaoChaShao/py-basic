
"""
模式匹配（Pattern Matching，Python 3.10+ 引入的 match 语句）：
在 Python 3.10 及以上版本中，| 用于模式匹配语句中表示模式的选择（逻辑或）。
"""


def match_example(value):
    match value:  # 匹配 value 变量
        case 1 | 2 | 3:  # 如果 value 等于1、2、3中的任意一个
            return "Value is 1, 2, or 3"
        case _:  # 如果 value 与上述模式不匹配，_ 是通配符，代表任意值
            return "Value is something else"


if __name__ == '__main__':
    print(match_example(2))  # 输出: Value is 1, 2, or 3
    print(match_example(5))  # 输出: Value is something else
