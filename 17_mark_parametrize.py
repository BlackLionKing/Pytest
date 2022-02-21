"""
    @pytest.mark.parametrize(argnames, argvalues) 允许在测试函数或类中和fixtures定义多组参数
    argnames: 要参数化的变量 类型：string, list, tuple
    argvalues: 要参数化的值  类型：list list(tuple)



"""

import pytest

"""
# 未参数化的代码
def test_one():
    assert 1 == 2


def test_two():
    assert 2 == 2
"""


"""
    @pytest.mark.parametrize(参数名, 对应的参数值)
        
        
    如果只有一个参数 里面则是值的列表如 
        @pytest.mark.parametrize("username", ["yy", "yy2", "yy3"])

    如果有多个参数例 则需要用元组来存放值 一个元组对应一组参数的值 如
        @pytest.mark.parametrize("name,pwd", [("yy1", "123"), ("yy2", "123"), ("yy3", "123")])
        
    
    test_three 方法参数传入test_input, expected
    
    
"""


# 利用参数化之后的代码
# test_input参数  对应 "3+5" "2+4"
# expected参数    对应 8 6 50
# @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 50)])
# def test_three(test_input, expected):
#     # eval()函数 把字符串内的数据转换为表达式
#     assert eval(test_input) == expected


"""
    @pytest.mark.parametrize()装饰测试类
    会将数据集合传递给类的所有测试用例方法

"""

"""
@pytest.mark.parametrize("num1, num2, sum", [(1, 2, 1), (2, 2, 4)])
class Test_demo(object):

    # 两个参数值 执行两次 一条成功 一条失败
    def test_one(self, num1, num2, sum):
        assert num1 + num2 == sum

    def test_two(self, num1, num2, sum):
        assert num1 * num2 == sum
"""


"""
    笛卡尔积 多个参数化装饰器
    一个函数或一个类可以装饰多个 @pytest.mark.parametrize 
    当参数化装饰器有很多个的时候，用例数都等于n*n*n*n*
    这种方式，最终生成的用例数是n*m
    输出结果：
        1a / 2a / 3a / 1b / 2b / 3b
    

"""

"""
@pytest.mark.parametrize('list1', [1, 2, 3])
@pytest.mark.parametrize('list2', ['a', 'b'])
def test_one(list1, list2):
    print(list1, list2)
"""

"""
    参数化 传入字典数据
"""


"""
@pytest.mark.parametrize("dic", ({'num': 1}, {20: 20}))
def test_one(dic):
    # 两个参数 执行两次 {'num': 1}  {20: 20}
    print(dic)
"""

"""
    参数化 标记数据marks=
        测试数据跳过 / 未定义 
    
    pytest.mark.xfail       未定义case
    pytest.mark.skip        跳过case
    pytest.mark.skipif()    条件成立则跳过case
"""

"""
@pytest.mark.parametrize("test_input, expected", [("3 + 3", 5), ("2 * 3", 6),
                                                  # 预计失败的测试数据 在测试结果中显示xpassed
                                                  pytest.param("6 * 9", 54, marks=pytest.mark.xfail),
                                                  # 跳过此条测试数据 在测试结果中显示skipped
                                                  pytest.param("6 * 5", 30, marks=pytest.mark.skip),
                                                  # 如果2==3条件成立 则跳过此条测试数据
                                                  pytest.param("6 * 5", 30, marks=pytest.mark.skipif("2 == 3")),
                                                  ])
def test_one(test_input, expected):
    assert eval(test_input) == expected
"""
