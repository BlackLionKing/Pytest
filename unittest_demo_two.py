import unittest

"""
    执行测试用例
    
    测试套件
        多个测试用例的集合就是测试套件 通过测试套件来管理多个用例
            创建套件
            suite = unittest.TestSuite()
            执行套件
            unittest.TextTestRunner().run(suite)
        
        将函数(每条用例)添加到套件中
            suite.addTest(类名("函数名"))
        
        将测试类添加到套件并执行
            加载测试类
            unittest.TestLoader().loadTestsFromTestCase(类名)
            创建测试套件 将测试类加到套件中
            suite = unittest.TestSuite([类名, ])
            执行
            unittest.TextTestRunner().run(suite)
            

"""


class demo_one(unittest.TestCase):

    def test_one(self):
        print('test_1')

    def test_two(self):
        print('test_2')


class demo_two(unittest.TestCase):

    def test_three(self):
        print('test_3')

    def test_four(self):
        print('test_4')


if __name__ == '__main__':
    # 创建测试套件
    # suite = unittest.TestSuite()
    # 将测试用例 加到测试套件中(类名(函数名))
    # suite.addTest(demo_one("test_one"))
    # suite.addTest(demo_two("test_three"))
    # 执行测试套件
    # unittest.TextTestRunner().run(suite)

    # 加载测试类
    # demoTwo = unittest.TestLoader().loadTestsFromTestCase(demo_two)
    # 创建测试套件 将测试类加到套件中
    # suite = unittest.TestSuite([demoTwo, ])
    # 执行
    # unittest.TextTestRunner().run(suite)

    pass
