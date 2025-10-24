
import json
import os


def json_dump(dump_data, dump_file_path):
    with open(dump_file_path, mode='w', encoding='utf-8') as json_file:
        # 01号位使用dump[]，02号位就需要用append()
        json.dump([dump_data], json_file, ensure_ascii=False, indent=4)  # 01号位


def json_load(load_file_path):
    with open(load_file_path, mode='r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
        return existing_data


def json_add(add_data, add_file_path):
    if os.path.exists(add_file_path):
        with open(add_file_path, mode='r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
        existing_data.append(add_data)  # 将新数据添加到现有数据中  # 02号位
        json_dump(existing_data, add_file_path)  # 保存现有数据到文件中
    else:
        json_dump(add_data, add_file_path)  # 文件不存在，则直接保存新数据到文件中


if __name__ == '__main__':
    # 1.dumps()方法将Python对象编码为JSON字符串
    data_dict = {'name': '狂徒三', 'age': 25, 'city': '北京'}
    file_path = 'data_json.json'

    new_dict_01 = {'name': '狂徒四', 'age': 26, 'city': '上海'}

    json_dump(data_dict, file_path)
    json_load(file_path)
    loaded_dict = json_load(file_path)
    print(loaded_dict)

    json_add(new_dict_01, file_path)
    loaded_new_dict = json_load(file_path)
    print(loaded_new_dict)
