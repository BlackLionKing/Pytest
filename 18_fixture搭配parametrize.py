"""
    fixture单独使用

    1、在方法上添加装饰器
        pytest.fixture(params=[1, 2, 3, 'test'])
    2、指定方法的参数名为request
        request.param 表示
    3、每个参数都会被传递执行一次 假设参数列表内有四个参数 则测试方法会执行四次

"""


import pytest

"""
# 指定四个参数
@pytest.fixture(params=[1, 2, 3, 'test'])
def test_data(request):
    # 将参数返回
    return request.params


# 测试方法会根据参数个数 而 决定执行多少次
def test_one(test_data):
    print(test_data)
"""


"""
    fixture 与 parametrize 搭配使用
    
    indirect=True 参数
        就是为了把user, paw 当作函数去执行
    
    def test_login(user, paw):
        这里的user, paw 是为了接收fixture返回的值
    
    @pytest.mark.skip() 跳过此条case  在测试结果中显示skipped
    @pytest.mark.xfail() 预计失败case 在测试结果中显示xpassed
    
    
    

"""


@pytest.fixture()
def user(request):
    name = request.param
    return name


@pytest.fixture()
def paw(request):
    paw = request.param
    return paw


data = [("user1", "paw1"), ("user2", "paw2")]


# user 对应 user1 / user2
# paw 对应 paw1 / paw2
@pytest.mark.parametrize("user, paw", data, indirect=True)
def test_login(user, paw):
    print(user, paw)


# 跳过执行此条case
@pytest.mark.skip()
def test_order(user, paw):
    print('跳过执行此条case')


@pytest.mark.xfail()
@pytest.mark.parametrize("user, paw", data, indirect=True)
def test_pay(user, paw):
    print(user, paw)
