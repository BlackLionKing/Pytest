"""
    Pytest介绍
        1、非常成熟的全功能测试框架
        2、支持参数化
        3、能够支持简单的单元测试和复杂的功能测试 可以用来搭配selenium/appnium自动化测试框架
        也可以用来搭配requests
        4、支持测试用例的skip xfail 自动失败重试等处理
        5、具有很多第三方插件 pytest-allure(html测试报告) pytest-xdist(cpu分发)
        6、可以和jenkins集成


    第三方包
        pytest-sugar            执行过程美化
        pytest-rerunfailures    失败重试
        pytest-xdist            多任务
        pytest-assume           断言
        pytest-html

    测试用例的识别与运行
        测试文件
            test_*.py
            *_test.py
        用例识别
            Test*类 包含的所有test_*的方法 (测试类不能带有__init__方法)
            不再class中的所有test_*方法

        pytest可以执行unittest框架写的用例和方法

    终端执行命令：
        pytest 文件名称                           执行脚本
        pytest -v 文件名称                        打印详细运行日志信息
        pytest -v -s 文件名称                     s指输出方法内的输出(print)信息
        pytest 文件名称::类名                      运行某个模块里的某个类 (::前面与后面不能加空格)
        pytest 文件名称::类名::方法名               运行某个模块里的某个类里面的方法
        pytest -v -k "类名 and not 方法名"         跳过运行某个用例 (and not等于条件)
        pytest -x 文件名                          一旦运行到报错就停止运行
        pytest 文件名称 --maxfail=num             当运行错误达到num值的时候就停止运行 (max前有两个--  且=号前后不能加空格)
        pytest -m[标记名]                         将运行有这个标记的测试用例

"""


import pytest


# 首字母需大写
class Test_demo(object):
    def test_num(self):
        assert 2 == 3

    # 使用命令行执行本文件 pytest pytest_demo.py
    def test_func(self):
        print('test_func')
        assert 2 == 2

    def test_num2(self):
        assert 2 == 3

    def test_num3(self):
        assert 2 == 3


def test_func2():
    print('test_func2')
    assert 2 == 2
