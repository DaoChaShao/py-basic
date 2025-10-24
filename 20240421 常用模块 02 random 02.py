
import random

"""
random.random() 是 Python 中 random 模块中的一个函数，
用于生成一个 0 到 1 之间的随机浮点数。

准确来说，如果你执行 if random.random() < 0.3 这个语句，
生成的概率大约是 30% 而不是 33%。
因为 random.random() 函数会生成一个范围在 [0.0, 1.0) 内的随机浮点数，
它可以取到 0.0 但不包括 1.0。
因此，它实际上在这个范围内生成的随机数大约有 30% 的机会小于 0.3。
"""

# 生成一个随机数
random_number = random.randint(0, 9)

# 根据一定的概率来决定是否生成三个相同的随机数
probability_pc = round(random.random(), 2)
print(probability_pc)
probability_hb = 0.3
if probability_pc <= probability_hb:  # 这里的 0.3 是一个示例概率值，你可以根据需要调整
    random_numbers = [random_number] * 3
else:
    random_numbers = [random.randint(0, 9) for _ in range(3)]

print(random_numbers)

