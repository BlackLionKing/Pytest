import pytest

"""
    可以理解成一个专门存放fixture的配置文件

    不需要导入conftest.py 可以跨.py文件调用 
    配置文件名称是固定的 不能更改名称
    系统执行到参数时 先从文件中查找是否有这个名字的变量 之后在conftest.py中找是否有
    
    场景
        接口共同需要的token
        共同需要的测试用例数据

"""


# 需要被重复使用的方法 加@pytest.fixture() 联想文件14
@pytest.fixture()
def login():
    print('login方法')


# 配置mark自定义标签 联想文件19
def pytest_configure(config):
    # 标签名集合
    marker_list = ["login", "logout"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
