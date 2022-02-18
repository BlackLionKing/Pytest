"""
    使用mark只执行某部分用例
    命令
        pytest -s -v 文件名 -m 标记名

    pytest -v -s 19_自定义标记mark.py -m logout 只会执行标记为logout的case

"""
import pytest


@pytest.mark.login
def test_login_one():
    print('login_one')


@pytest.mark.login
def test_login_two():
    print('login_two')


@pytest.mark.logout
def test_logout_one():
    print('logout_one')


@pytest.mark.logout
def test_logout_two():
    print('logout_two')
