
def example_func():
    print("This is an example function.")
    a = yield 1
    print("This is gap between yield 1 and 2.", a)
    b = yield 2
    print("This is gap between yield 2 and 3.", b)
    yield 3
    print("This is the end of the function.")


gen = example_func()

result_01 = next(gen)  # 第一次执行必须用next()
print(result_01)  # 1

result_02 = gen.send('Hello World!')  # send()方法可以向生成器发送数据，重新赋值给yield表达式（yield 1）
print(result_02)  # 2

result_03 = gen.send('Goodbye World!')  # send()方法可以向生成器发送数据，重新赋值给yield表达式（yield 2）
print(result_03)  # 3
