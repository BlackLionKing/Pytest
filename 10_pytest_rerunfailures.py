"""
    Pytest执行失败 重新运行
    场景：
        测试失败后要重新执行N次 且重新运行时要间隔N秒

    命令行执行语句
        pytest -v --reruns 执行次数 文件名称   (pytest -v --reruns 3 10_pytest_rerunfailures.py)

            实际执行次数 = 执行失败一次 + 执行次数
            -v 表示显示详细运行信息

        pytest --reruns 执行次数 --reruns-delay 间隔秒数 文件名称(pytest -v --reruns 3 --reruns-delay 2 10_pytest_rerunfailures.py)
            执行n次 间隔n秒

"""

import time


# 首字母需大写
class Test_demo(object):
    def test_func(self):
        print(time.time())
        assert 2 == 3

    def test_num(self):
        print(time.time())
        assert 2 == 2


class Test_demo_two(object):
    def test_func2(self):
        print(time.time())
        assert 2 == 5
