"""
    pytest框架结构
        pytest类似的setup teardown同样更灵活

        模块级(setup_module / teardown_module) 模块始末 全局(优先级最高) 执行一次
        函数级(setup_function / teardown_function) 函数用例生效(不在类中) 执行几个函数就跟随执行几次
        类级  (setup_class / teardown_class) 只在类中前后运行一次
        方法级(setup_method / teardown_method) 开始于方法始末 (在类中) 执行几个方法就跟随执行几次
        类里面的(setup / teardown) 运行在调用方法的前后

        python 3.8 setup 与 setup_method 不能同时存在 否则只会执行 setup_method

        其他版本
            会先执行 setup_method 在执行 setup

"""

import pytest


# 模块级 setup
def setup_module():
    print('setup_module')


# 函数级 setup
def setup_function():
    print('setup_function')


# 测试用例 函数
def test_case():
    print('test_case')
    assert 1 == 1


# 测试用例 函数
def test_case_two():
    print('test_case_two')
    assert 1 == 1


# 函数级 teardown
def teardown_function():
    print('teardown_function')


# 模块级 teardown
def teardown_module():
    print('teardown_module')


# 测试用例 类
class Test_demo(object):
    # 类级 setup
    def setup_class(self):
        print('setup_class')

    # 方法级 setup_method
    def setup_method(self):
        print('setup_method')

    # 方法级 setup
    def setup(self):
        print('setup')

    # 测试用例 方法
    def test_class_case(self):
        print('test_class_case')
        assert 1 == 1

    def test_class_case_two(self):
        print('test_class_case_two')
        assert 1 == 1

    # 方法级 teardown
    def teardown(self):
        print('teardown')

    # 方法级 teardown_method
    def teardown_method(self):
        print('teardown_method')

    # 类级 teardown
    def teardown_class(self):
        print('teardown_class')


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
