"""
    场景
        case1 需要先登陆
        case2 不需要登陆
        case3 需要登陆

    用法
        在要被重复使用的方法上面加 @pytest.fixture()

        在要用到这个重复方法 的 方法参数内 加上这个 重复方法 的名字

"""

import pytest


# 需要用到登陆方法的函数 在参数内加方法名字 login
def test_case_one(login):
    print('test_case_one需要登陆')


def test_case_two():
    print('test_case_two不需要登陆')


def test_case_three(login):
    print('test_case_three需要登陆')
