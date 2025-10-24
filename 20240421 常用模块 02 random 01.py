import random

print(random.randint(10, 20))  # 随机整数
print(random.random())  # 随机浮点数，0-1之间
print(random.uniform(1, 10))  # 随机浮点数，1-10之间
print(random.choice([1, 2, 3, 4, 5]))  # 从列表中随机选择一个元素
print(random.sample([1, 2, 3, 4, 5], 3))  # 从列表中随机选择3个元素，不重复
print(random.shuffle([1, 2, 3, 4, 5]))  # 将列表随机打乱
print(random)

# 随机生成密码
# 1.六位验证码，一个一个生成
# 2.可能会有数字、大小写字母、特殊字符
# ascii_letters 所有字母


def generate_random_numbers():
    return random.randint(0, 9)


def generate_random_upper_letters():
    return chr(random.randint(65, 90))  # ascii码 65-90 是大写字母


def generate_random_lower_letters():
    return chr(random.randint(97, 122))  # ascii码 97-122 是小写字母


def generate_random_special_characters():
    special_characters = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    return random.choice(special_characters)


def generate_password():
    password = ""
    for i in range(6):
        if i % 2 == 0:  # 偶数位
            password += str(generate_random_numbers())
        elif i % 3 == 0:  # 第三位
            password += str(generate_random_upper_letters())
        elif i % 5 == 0:  # 第五位
            password += str(generate_random_lower_letters())
        else:  # 其他位
            password += str(generate_random_special_characters())
    return password


print(generate_password())


def generate_verify_code(length=4):
    code_list = []
    for i in range(length):
        random_category = random.randint(1, 3)  # 随机生成 1-3 的类别（数字、大写字母、小写字母）
        if random_category == 1:  # 数字类别，产生随机数字
            code_list.append(str(generate_random_numbers()))
        elif random_category == 2:  # 大写字母类别，产生随机大写字母
            code_list.append(str(generate_random_upper_letters()))
        elif random_category == 3:  # 小写字母类别，产生随机小写字母
            code_list.append(str(generate_random_lower_letters()))
    code_result_before = ''.join(code_list)
    random.shuffle(code_list)  # 随机打乱
    code_result_after = ''.join(code_list)
    yield code_result_before
    yield code_result_after


verify_codes = generate_verify_code()
print(generate_verify_code())
print(next(verify_codes))  # 产生随机打乱前的验证码
print(next(verify_codes))  # 产生随机打乱后的验证码
