'''
dump 和 dumps 是把对象序列化为字节流，叫做序列化
load 和 loads 是把字节流反序列化为对象，叫做反序列化
'''

import pickle as pkl  # 转化为二进制字节
from faker import Faker  # 用于生成假数据
import os.path  # 文件路径操作


def dump_pkl(dump_data, dump_file_path):
    with open(dump_file_path, 'wb') as pkl_file:
        pkl.dump(dump_data, pkl_file)  # 序列化并写入文件


def load_pkl(load_file_path):
    with open(load_file_path, 'rb') as pkl_file:
        existing_data = pkl.load(pkl_file)  # 反序列化
    return existing_data


def add_pkl(add_data, add_file_path):
    # 如果文件存在，则加载原有数据并追加
    if os.path.exists(add_file_path):
        with open(add_file_path, 'ab') as pkl_file:  # 使用追加二进制模式
            pkl.dump(add_data, pkl_file)
    else:
        with open(add_file_path, 'wb') as pkl_file:  # 使用写入二进制模式
            pkl.dump(add_data, pkl_file)


if __name__ == '__main__':
    # 生成假数据
    name_list = [Faker(locale='zh_CN').name() for _ in range(10)]
    dict_01 = {'name': '狂徒三', 'age': 25, 'city': '北京'}

    file_path = 'data_pickle.pkl'
    data = name_list

    # dump_pkl(data, file_path)
    loaded_list = load_pkl(file_path)
    print(loaded_list)

    add_pkl(dict_01, file_path)  # 目前写不进去？？？？？？？？？？？？？
    loaded_dict = load_pkl(file_path)
    print(loaded_dict)
