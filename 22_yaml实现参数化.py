"""
    yaml实现list
    list
        - 10
        - 20
        - 30
    yaml实现dict
    dict
        key: value
        by: id

    yaml实现嵌套
        -
            - key: value
            - by: id
        相当于列表嵌套字典
        [{key: value}, {by: id},]


        二维列表
        -
            - value
            - value2

        -
            - value3
            - value4
        相当于列表嵌套列表
        [value, value2,] [value3, value4]



    pytest加载yaml
        yaml.safe_load(open("yaml文件路径"))


"""
# a = [{'a': 97}, {'b': 98}, {'c': 99}, {'d': 100}, {'e': 101}, ]
# for i in a:
#     for key, value in i.items():
#         print(key, value)

import yaml
import pytest


# a对应value value3
# b对应value2 value4
@pytest.mark.parametrize("a, b", yaml.safe_load(open('./data.yaml')))
def test_data(a, b):
    print(a + b)
