"""
    按优先级进行一定范围测试
    场景
        通常测试有p0、冒烟测试、上线回测。
        按优先级来分别执行 比如上线要把主流程和重要模块都跑一遍

    解决
        通过pytest.mark标记
        通过allure.feature allure.story

        也可以通过 allure.severity来附加标记
            级别：Trivial(不重要) Minor(不太重要) Normal(正常问题) Critical(严重) Blocker(阻塞)

    步骤
        在类/方法/函数上增加装饰器
        @allure.severity(allure.severity_level.TRIVIAL)

        执行命令
            pytest 文件名 --alluredir=Json目录 --allure-severities 优先级参数(如normal, critical)

    在pycharm中配置运行优先级的命令参数
        1、edit configurations -> additional arguments
           把优先级命令参数复制到里面 --allure-severities 优先级参数(如normal, critical)

        2、在python文件中指定main()函数 pytest.main() 执行main函数


"""
import pytest

import allure


# 装饰在类上面 则类下面所有的方法都会执行
# @allure.severity(allure.severity_level.NORMAL)
class Test_login(object):
    def test_input_user(self):
        print('test_input_user')
        assert 1 == 2

    @allure.severity(allure.severity_level.NORMAL)
    def test_input_password(self):
        print('test_input_password')

    def test_num(self):
        print('test_num')

    def test_login(self):
        print('test_login')

    def test_case(self):
        print('test_case')

    def test_bug(self):
        print('test_bug')


@allure.severity(allure.severity_level.TRIVIAL)
def test_func():
    print('test_func')
    assert 1 == 2


if __name__ == '__main__':
    pytest.main('-v -s')
