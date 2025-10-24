
'''
实参
1.位置实参：按照函数定义的顺序，按顺序传递实参
2.关键字实参：按照关键字传递实参，关键字实参必须以关键字形式传递，关键字实参的顺序无关紧要
3.混合参数：位置实参和关键字实参可以混合使用，先位置参数，后关键字参数

形参
1.位置形参：按照函数定义的顺序，按顺序接收实参
2.关键字形参：按照关键字接收实参，关键字形参必须以关键字形式接收，关键字形参的顺序无关紧要
3.动态传参：函数调用时，可以动态传递实参，实参可以是任意数量的，不受函数定义的限制
4.混合形参：位置形参和关键字形参可以混合使用，先位置形参，后关键字形参
'''

from faker import Faker


# 传统传参
def eat(main, sides, drink, dessert):
    print(f'I helped you order {main}, {sides}, {drink}, {dessert}.')
    print('Enjoy your meal!')


eat('fish and chips', 'veges', 'tea', 'cake')
print()


# 动态传参

# * 代表“任意多个”，即“不定长”，可以接收任意数量的参数
# 形参位置：多个参数，一次性接收
# 形参结果：被打包成“元组”呈现
def order(*goodies):  # 默认写法：*args
    print(f'I will prepare you {goodies}.')
    print('Enjoy your meal!')


order('fish and chips')
order('fish & chips', 'veges')
order('fish & chips', 'veges', 'tea', 'cake')
print()


# ** 代表“任意多个关键字参数”，即“不定长关键字”，可以接收任意数量的关键字参数
# 关键字参数：多个参数，一次性接收
# 关键字结果：被打包成“字典”呈现
def order_with_options(**options):  # 默认写法：**kwargs
    print(f'I will prepare you {options}.')
    print('Enjoy your meal!')


order_with_options(main='fish and chips')
order_with_options(main='fish & chips', sides='veges')
order_with_options(main='fish & chips', sides='veges', drink='tea', dessert='cake')
print()

# 参数：位置参数 > *args > 默认值参数 > **kwargs


def func(*args, **kwargs):
    print(args)
    print(kwargs)


example_list = [Faker(locale='zh_CN').name() for _ in range(5)]


def func_list(*args):
    print(args)


func_list(
    example_list[0],
    example_list[1],
    example_list[2],
    example_list[3],
    example_list[4]
)

func_list(*example_list)

# 结果是一样的
# * 可以完成dict和list的解包，** 可以完成dict的解包

example_dict = {
    'name': Faker(locale='zh_CN').name(),
    'sentence': Faker(locale='zh_CN').sentence(),
}


def func_dict(**kwargs):
    print(kwargs)


func_dict(
    name=example_dict['name'],
    sentence=example_dict['sentence'],
)
func_dict(**example_dict)

'''
* 和 **
在形参位置：表示参数的聚合，把位置参数聚合成元组，把关键字参数聚合成字典
在实参位置：表示“打散”，把可迭代对象转化为位置参数，把字典或列表化成为关键字参数
'''