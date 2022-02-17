"""
    Preferences -> python integrated tools -> default test runner 选择 pytest
        就可以在pycharm中右键运行pytest

"""

import pytest


class Test_demo(object):
    def test_num(self):
        assert 2 == 3

    def test_func(self):
        print('test_func')
        assert 2 == 2

    def test_num2(self):
        assert 2 == 3

    def test_num3(self):
        assert 2 == 3


class Test_demo_two(object):
    def test_num(self):
        assert 2 == 3

    def test_func(self):
        print('test_func')
        assert 2 == 2

    def test_num2(self):
        assert 2 == 3

    def test_num3(self):
        assert 2 == 3


if __name__ == '__main__':
    # 运行Test_demo_two类下的test_func方法
    pytest.main(["-v", '-s', "Test_demo_two::test_func"])
