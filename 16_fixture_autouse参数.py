"""

    场景：
        以不想测试方法有改动为基础 自动实现在执行测试方法前先执行某个方法

    在方法上面加
        @pytest.fixture(autouse = True) autouse默认为false

        测试方法就都会先执行一遍open 省略了在case方法的参数里加open函数名的步骤

"""

import pytest


# 测试函数都会先执行一遍open方法
@pytest.fixture(autouse=True)
def open():
    print('打开浏览器')


# 不用在参数里加open 默认先执行open方法
def test_search():
    print('test_search')


def test_search_two():
    print('test_search_two')


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
