
def example_func():
    print("This is an example function.")
    yield 1
    print("This is gap between yield 1 and 2.")
    yield 2
    print("This is gap between yield 2 and 3.")
    yield 3
    print("This is the end of the function.")


# 生成器
gen = example_func()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# 生成器只能使用1次
# 生成器的作用：节省内存，避免大量数据在内存中占用，可以按需生成数据


# 例子:for
# 买10000件衣服
def buy_clothes():
    clothe_list = []
    for i in range(5):
        clothe_list.append(f'Clothes number {i}')
    return clothe_list


# 调用函数
clothes_list = buy_clothes()


# 例子：生成器
def generate_clothe():
    for i in range(5):
        yield f'Clothes number {i}'


# 调用生成器
gen = generate_clothe()

print(next(gen))  # Output: Clothes number 0
print(next(gen))  # Output: Clothes number 1
print(next(gen))  # Output: Clothes number 2
print()


def generate_clothes(num):
    for i in range(num):
        yield f'Clothes number {i}'


# 使用for循环遍历生成器
for clothe in generate_clothes(5):
    print(clothe)
