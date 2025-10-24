import random
import re

from utils.highlighter import red


def type_checker(value):
    """ 输入类型分类器 """
    match value:
        case str():
            print("字符串")
        case int():
            print("整数")
        case float():
            print("浮点数")
        case bool():
            print("布尔值")
        case _:
            print("其他类型")


def re_checker(text):
    """ 正则表达式分类器 """
    match text:
        case _ if re.match(r"^[\u4e00-\u9fa5]+$", text):
            print("纯中文")
        case _ if re.match(r"^[a-zA-Z]+$", text):
            print("纯英文")
        case _ if re.match(r"^[0-9]+$", text):
            print("纯数字")
        case _:
            print("其他型")


def main():
    """ 主函数 """
    # # 设置类型
    # test_list = [1, 2.0, "hello", True, None]
    # input_type = random.choice(test_list)
    # print(f"随机类型：{input_type}")

    # 调用分类器
    type_checker(red(12))
    type_checker(red(2.0))
    type_checker(red("hello"))
    type_checker(True)
    type_checker(None)

    # 设置输入内容
    text = [
        "你好世界",
        "你好world",
        "Helloworld",
        "1234567890",
        "@#$%^&*()_+",
    ]
    input_test = random.choice(text)
    print(f"随机内容：{input_test}")

    # 调用分类器
    re_checker(input_test)


if __name__ == "__main__":
    main()
