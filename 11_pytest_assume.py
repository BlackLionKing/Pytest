"""
    pytest_assume
    一个方法中写多条断言 第一条执行失败后 下面就无法执行 现在要求失败后继续执行后面的逻辑

    执行语句
        pytest.assume(1==4) ()里面为表达式
"""

import pytest


# 首字母需大写
class Test_demo(object):
    def test_num(self):
        # 添加断言
        pytest.assume(1 == 2)
        pytest.assume(1 == 1)
