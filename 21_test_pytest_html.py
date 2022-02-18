"""
    插件安装
        pip3 install pytest-html

    执行命令
        pytest --html=report.html
        会在当前目录下创建一个report.html的测试报告

    由于命令生成的报告 css是独立的 分享报告的时候样式会丢失 为了更好的分享展示报告 合并html报告中的css
        pytest --html=report.html --self-contained-html


    前提条件
        当前目录下 测试文件需以test_开头 且文件内测试用例 同样需以test_开头

"""

import time


def test_logout_one():
    time.sleep(1)
    print('logout_one')


def test_logout_two():
    time.sleep(1)
    print('logout_two')


def test_logout_three():
    time.sleep(1)
    print('test_logout_three')


def test_logout_four():
    time.sleep(1)
    print('test_logout_four')
