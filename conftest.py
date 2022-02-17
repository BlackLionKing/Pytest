import pytest

"""
    不需要导入conftest.py 可以跨.py文件调用 
    配置文件名称是固定的 不能更改名称
    系统执行到参数时 先从文件中查找是否有这个名字的变量 之后在conftest.py中找是否有
    
    场景
        接口共同需要的token
        共同需要的测试用例数据

"""


# 需要被重复使用的方法 加@pytest.fixture()
@pytest.fixture()
def login():
    print('login方法')
