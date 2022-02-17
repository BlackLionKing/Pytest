"""
    测试方法后 销毁清除数据如何进行？
    通过在同一模块中加入yield关键字 yield被调用第一次返回yield之前的语句 最后一次执行它下面的语句返回

    如果其中一个用例出现异常 不影响yield后面的teardown执行 并且在用例全部执行完之后 会唤醒teardown执行yield之后的内容

    用法
        @pytest.fixture(scope=module)
            scope=module 表示当前模块可用 默认为Function函数可用
            作用域为模块时 在整个模块只调用一次



"""


import pytest


# 整个模块 只执行一次open方法
@pytest.fixture(scope="module")
def open():
    # 调用test_search函数前 先执行下面打印语句
    print('打开浏览器')

    # 打开浏览器输出 执行完后 会将OPEN函数挂起

    # 执行到本模块最后一个函数 yield函数用来唤醒teardown 会输出yield关键字后面的内容
    yield

    print('关闭浏览器')


def test_search(open):
    print('test_search')


def test_search_two(open):
    print('test_search_two')


def test_search_three(open):
    print('test_search_three')


def test_search_four():
    print('test_search_four')


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
