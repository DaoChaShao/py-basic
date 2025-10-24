
# 字符串操作方法

# 1.字符串的查找：查找子串在字符串中的位置(即：下标)和次数

# 1.1 .find()：检测某个子串是否包含在这个字符串中，如果在,则返回这个子串开始的位置下标，如不在，则返回 -1
# 查找语法：字符串序列.find(子串, 开始位置下标, 结束位置下标)
# - 开始和结束位置下标可以省略，表示在整个字符串序列中查找

# .rfind()：和 .find() 功能相同，但查找方向为右侧 (“r”意味着:right - 右侧开始 - 从右至左的意思)

str_one = "ipad and iphone and imac and iwatch"
#          01234567890123456789012345678901234
#                    1         2         3

print(str_one.find("and")) # 5
print(str_one.find("and", 9, 21)) # 16
print(str_one.find("ands")) # -1 - 如果查找不存在，就输出 -1
print()

print(str_one.rfind("and")) # 25
print(str_one.rfind("ands")) # -1
print()


# 1.2 .index()：检测某个子串是否包含在这个字符串中，如果在,则返回这个子串开始的位置下标，否则则报异常
# 查找语法：字符串序列.index(子串, 开始位置下标, 结束位置下标)

# .rindex()：和 .index() 功能相同，但查找方向为右侧 (“r”意味着:right - 右侧开始 - 从右至左的意思)

str_two = "ipad and iphone and imac and iwatch"
#          01234567890123456789012345678901234
#                    1         2         3

print(str_two.index("and")) # 5
print(str_two.index("and", 9, 21)) # 16
### print(str_two.index("ands")) # 如果查找不存在，就报错：valueError: substring not found

print(str_two.rindex("and")) # 25
#### print(str_two.rindex("ands")) # 如果查找不存在，就报错：valueError: substring not found
print()


# 1.3 .count()：返回某个子串在字符串中的次数
# 查找语法：字符串序列.index(子串, 开始位置下标, 结束位置下标)
# - 开始和结束位置下标可以省略，表示在整个字符串序列中查找

str_three = "ipad and iphone and imac and iwatch"
          #  01234567890123456789012345678901234
          #            1         2         3

print(str_three.count("and")) # 3
print(str_three.count("and", 9, 21)) # 1
print(str_three.count("ands")) # 0 - 如果不存在，则显示 0
print()


# 2.字符串的修改，包括：替换、分割、合并

# 2.1 字符串的替换 (.replace())
# - 替换语法：字符串序列.replace(旧子串, 新子串, 替换次数)
# -- 替换次数如果不写，则表示全部替换
# -- “注意”：替换次数如果超出子串出现次数，则替换次数为该子串出现次数

# - 数据类型可以分为：可变类型 (列表 或 字典) 和 不可变类型 (字符串)
# -- .replace() 函数后，原数据不可以被修改

str_four = "ipad and iPhone and imac and iwatch"
new_str_four = str_four.replace("and", "or")
    # - .replace() 有返回值，返回值是修改后的字符串
    # - new_str_four 就是给返回值定义的新变量

print(str_four)
    # 输出：ipad and iPhone and imac and iwatch
    # .replace() 有返回值，返回值是修改后的字符串，并不会修改原字符串
print(new_str_four)
    # 输出：ipad or iPhone or imac or iwatch
    # .replace() 有返回值，返回值是修改后的字符串，不是原字符串

print(str_four.replace("and", "or"))
    # 输出：ipad or iPhone or imac or iwatch
print(str_four.replace("and", "or", 1))
    # 输出：ipad or iPhone and imac and iwatch
    # 仅替换一次，且是按照 从左到右 的顺序依次替换
print(str_four.replace("and", "or", 10))
    # 输出：ipad or iPhone or imac or iwatch
    # 替换次数超出子串出现的次数，表示替换所有子串 (“注意”)
print()


# 2.2 字符串的分割 (.split())
# - 分割语法：字符串序列.split(分割字符, num)
# -- 分割的结果：分割并返回一个列表
# -- “注意”：num 表示的是分割字符出现的次数，即将来返回数据个数为：num + 1 个

str_five = "ipad and iPhone and imac and iwatch"
list_one = str_five.split("and")

print(str_five) # 输出：ipad and iPhone and imac and iwatch
print(list_one) # 输出：['ipad ', ' iPhone ', ' imac ', ' iwatch']

print(str_five.split("and"))
    # 输出：['ipad ', ' iPhone ', ' imac ', ' iwatch']
    # 被分为几个数据，并丢失用来分割的子串
print(str_five.split("and", 2))
    # 输出：['ipad ', ' iPhone ', ' imac and iwatch']
    # 出现的被分割的数据个数为 num + 1 个 (“注意”)
print()


# 2.3 字符串的合并 (.join())
# - 合并语法：字符 或 子串.join(多字符串组成的序列)
# - 合并列表里面的字符串数据为一个大字符串

list_two = ["aa", "Bb", "cc"]
new_list_two = "···".join(list_two)

print(list_two)
print(new_list_two)

print("···".join(list_two)) # 输出：aa···Bb···cc···
print()


# 3. 非重点操作函数，包括：大小写转换、删除空白字符和对齐

# 3.1 字符串的大小写转换

# 3.1.1 .capitalize()
# - 语法：字符串序列.capitalize()
# - 注意: .capitalize() 函数转换后，只有字符串的第一个字符大写，其他字符全部强制转化或保持小写

str_six = "iPad and iPhone and iMac and iWatch"

print(str_six.capitalize()) # 输出：Ipad and iphone and imac and iwatch
                            # 比较：iPad and iPhone and iMac and iWatch (原始)
print()


# 3.1.2 .title()
# - 语法：字符串序列.title()
# - 注意：将字符串的每个单词首字母转换成大写，其他字符全部强制转化或保持小写

print(str_six.title()) # 输出：Ipad And Iphone And Imac And Iwatch
                       # 比较：iPad and iPhone and iMac and iWatch (原始)


# 3.1.3 .lower()
# - 语法：字符串序列.lower()
# - 注意：将字符串中的大写转小写

print(str_six.lower()) # 输出：ipad and iphone and imac and iwatch
                       # 比较：iPad and iPhone and iMac and iWatch (原始)


# 3.1.4 .upper()
# - 语法：字符串序列.upper()
# - 注意：将字符串中的小写转大写

print(str_six.upper()) # 输出：IPAD AND IPHONE AND IMAC AND IWATCH
                       # 比较：iPad and iPhone and iMac and iWatch (原始)
print()


# 3.2 删除字符串里的空白字符

# 3.2.1 删除字符串左侧空白字符
# - 语法：字符串序列.lstrip() - “l”：left

str_se7en = "   iPad and iPhone and iMac and iWatch   "

print(str_se7en.lstrip()) # 输出：iPad and iPhone and iMac and iWatch
                          #      123                                456
                          # 比较：   iPad and iPhone and iMac and iWatch    (原始)
                          #      123                                   456


# 3.2.2 删除字符串右侧空白字符
# - 语法：字符串序列.rstrip() - “r”：right

print(str_se7en.rstrip()) # 输出：   iPad and iPhone and iMac and iWatch
                          #      123                                456
                          # 比较：   iPad and iPhone and iMac and iWatch    (原始)
                          #      123                                   456

# 3.2.3 删除字符串两侧空白字符
# - 语法：字符串序列.strip()

print(str_se7en.strip()) # 输出：iPad and iPhone and iMac and iWatch
                         #      123                             456
                         # 比较：   iPad and iPhone and iMac and iWatch    (原始)
                         #      123                                   456
print()

# 3.2.4 去除空白字符

poem = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽，\t\n",
    "黄河入海流，",
    "欲穷千里目，",
    "更上一层楼。"
    ]

for poem_str in poem:

    # 先使用 .strip() 去除字符串中的空白字符
    poem_str_fix = poem_str.strip()
    # 再使用 .center() 中间对齐
    print("|%s|" % poem_str_fix.center(15, "　")) # 引号中的空格是中文全角空格
    # 输出：|　　　　　　登鹳雀楼　　　　　|
    #      |　　　　　　王之涣　　　　　　|
    #      |　　　　　白日依山尽，　　　　|
    #      |　　　　　黄河入海流，　　　　|
    #      |　　　　　欲穷千里目，　　　　|
    #      |　　　　　更上一层楼。　　　　|
print()


# 3.3 字符串左、中、右对齐

# 3.3.1 字符串左对齐
# - 语法：字符串序列.ljust(长度, 填充字符) - “l”：left
# -- 长度：在横向多少个字符内，实现左对齐
# -- 填充字符：

str_eight = "PYTHON"

print(str_eight.ljust(10)) # 输出：PYTHON
                           # 长度：1234567890 - 在10个字符长度内实现左对齐

print(str_eight.ljust(10,"·")) # 输出：PYTHON····
                               # 填充：1234567890 - 在10个字符长度内，且不足10个的位置用“填充字符”


# 3.3.2 字符串右对齐
# - 语法：字符串序列.rjust(长度, 填充字符) - “r”：right

print(str_eight.rjust(10)) # 输出：    PYTHON
                           # 长度：1234567890 - 在10个字符长度内实现左对齐

print(str_eight.rjust(10,"·")) # 输出：····PYTHON
                               # 填充：1234567890 - 在10个字符长度内，且不足10个的位置用“填充字符”


# 3.3.3 字符串右对齐
# - 语法：字符串序列.center(长度, 填充字符)
# - 注意：.center() 的填充字符的对齐原则为：先左后右的计数方式 --- 135|246 or 13|2 or 135|24

print(str_eight.center(10)) # 输出：  PYTHON   - 填充字符对齐计数 ：135|246
                            # 长度：1234567890 - 在10个字符长度内实现左对齐

print(str_eight.center(10,"·")) # 输出：··PYTHON·· -  填充字符对齐计数 ：135|246
                                # 填充：1234567890 - 在10个字符长度内，且不足10个的位置用“填充字符”

print(str_eight.center(9)) # 输出：  PYTHON  - 填充字符对齐计数 ： 13|2
                           # 长度：123456789 - 在10个字符长度内实现左对齐

print(str_eight.center(9,"·")) # 输出：··PYTHON· - 填充字符对齐计数 ： 13|2
                               # 填充：123456789 - 在10个字符长度内，且不足10个的位置用“填充字符”

print(str_eight.center(11)) # 输出：   PYTHON   - 填充字符对齐计数 ： 135|24
                            # 长度：12345678901 - 在10个字符长度内实现左对齐

print(str_eight.center(11,"·")) # 输出：···PYTHON·· - 填充字符对齐计数 ： 135|24
                                # 填充：12345678901 - 在10个字符长度内，且不足10个的位置用“填充字符”
print()

# 诗歌对齐 - 青铜级别

poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽，",
    "黄河入海流，",
    "欲穷千里目，",
    "更上一层楼。"
    ]

for poem_str in poem:

    print(poem_str.center(15))
print()

# 诗歌对齐 - 白银级别

poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽，",
    "黄河入海流，",
    "欲穷千里目，",
    "更上一层楼。"
    ]

for poem_str in poem:

    print(f"|{poem_str.center(15)}|")
    # 输出：|      登鹳雀楼     |
    #      |      王之涣      |
    #      |     白日依山尽，    |
    #      |     黄河入海流，    |
    #      |     欲穷千里目，    |
    #      |     更上一层楼。    |
print()

# 诗歌对齐 - 黄金级别

poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽，",
    "黄河入海流，",
    "欲穷千里目，",
    "更上一层楼。"
    ]

for poem_str in poem:

    print("|%s|" % poem_str.center(15, "　")) # 引号中的空格是中文全角空格
    # 输出：|　　　　　　登鹳雀楼　　　　　|
    #      |　　　　　　王之涣　　　　　　|
    #      |　　　　　白日依山尽，　　　　|
    #      |　　　　　黄河入海流，　　　　|
    #      |　　　　　欲穷千里目，　　　　|
    #      |　　　　　更上一层楼。　　　　|
print()


# 4.字符串的判断
# 判断真假，返回结果为布尔型数据类型 (Ture / False)
# 设置下标，则在指定范围内检查，不设置下标，则全部范围内检查

# 4.1 判断子串是否以 子串 开头 (.starstwith())
# - 意义：是否以 子串 在某个区间内或元数据中 开头
# - 语法：字符串序列.startswith(子串, 开始位置下标, 结束位置下标)

str_night = "iPad and iPhone and iMac and iWatch"
          #  01234567890123456789012345678901234
          #            1         2         3

print(str_night.startswith("iPad")) # 输出：True
print(str_night.startswith("iP")) # 输出：True
print(str_night.startswith("iPd")) # 输出：False
print(str_night.startswith("iPad", 0, 5)) # 输出：True


# 4.2 判断子串是否以 子串 结尾 (.endswith())
# - 意义：是否以 子串 在某个区间内或元数据中 结尾
# - 语法：字符串序列.endwith(子串, 开始位置下标, 结束位置下标)

print(str_night.endswith("iWatch")) # 输出：True
print(str_night.endswith("iwatch")) # 输出：False - 和子串中的大小写有关系
print(str_night.endswith("ch")) # 输出：True
print(str_night.endswith("ich")) # 输出：False
print(str_night.endswith("iWatch", 28, 35)) # 输出：True - 下标：左闭右开，右侧需多数一位才能包含
print()


# 4.3 .isalpha()
# - 如果字符串中有一个字符，且所有字符都是 字母的，则返回True，否则返回False
# - 语法：字符串序列.isalpha()

str_11 = "python"
str_12 = "python381"

print(str_11.isalpha()) # True - 有一个字符是字母，且所有字符是字母，所以返回 1
print(str_12.isalpha()) # False - 有一个字符是字母，但不是所有字符是字母 (数字或空格)，所以返回 0


# 4.4 .isdigit()
# - 如果字符串只包含数字，则返回True，否则返回False
# - 不能判断小数
# - 语法：字符串序列.isdigit()

str_13 = "ascd1234"
str_14 = "1234"

print(str_13.isdigit()) # False - 并非所有字符为数字 (字母或空格)，所以返回 0
print(str_14.isdigit()) # True - 所有字符都是数字，所以返回 1


# 4.5 .isalnum()
# - 如果字符串至少有一个字符，且所有字符都是字母或数字，则返回True，否则返回False
# - 语法：字符串序列.isalnum()

str_15 = "abcde12345"
str_16 = "abcde-12345"

print(str_15.isalnum()) # True - 所有字符均是数字或字母
print(str_16.isalnum()) # False - 有非字母和数字的字符存在：“-”


# 4.6 .isspace()
# - 如果字符串中只包含空白，则返回True，否则返回False
# - 语法：字符串序列.isspace()

str_17 = "1 2 3 a b c"
str_18 = "   "
str_19 = "   \t\n\r"

print(str_17.isspace()) # False - 除空格外，还包含其他类型字符
print(str_18.isspace()) # True - 只包含空格
print(str_19.isspace()) # True - \t 或 \n 或 \r 均表示空白字符
print()

