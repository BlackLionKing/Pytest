"""
    什么是单元测试
        单元测试是开发者编写的一小段代码 用于检测被检测代码的一个很小、很明确的功能是否正确
        通常而言 一个单元测试是用于判断某个特定条件下某个特定函数的行为

    单元测试什么时候开始 由谁负责
        研发负责 开发完成后开始

    单元测试覆盖率
        语句覆盖
            通过设计一定量的测试用例 保证被测试的方法每一行代码都会执行一遍
            运行测试用例的时候 被击中的代码航
        条件覆盖
        判断覆盖
        路径覆盖

    unittest
        加上htmlTestRunner可以生成html报告
        提供丰富的断言方法 验证函数等功能
        在自动化测试中提供用例组织与执行

    unittest提供了 test cases(测试用例)、 test suite(测试用例集合)、test fixture、test runner相关组件

    编写规范
        测试类必须继承 unittest.TestCase
        测试方法必须以 'test_'开头


    总结
        setUp用来为测试准备环境 tearDown用来清理环境

        setup teardown 与 setupclass tearDownClass区别
            如果想要在所有case执行之前准备一次环境 并在case执行完成后清理一次测试环境
            可以用setUpClass()与tearDownClass()方法

            如果想要在每个case执行前准备一次环境 并在每个case执行完成后清理一次测试环境
            可以用setup() 和 teardown()方法


        如果想有些方法不再本次执行使用 @unittest.skip
        符合条件则跳过case使用：
            @unittest.skipIf(1 + 1 == 2, '符合判断则跳过')

"""

import unittest


class demo_test(unittest.TestCase):
    # 执行类中所有case时 先调用setUpClass
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    # 每次执行case时 先执行setUp
    def setUp(self) -> None:
        print('setUp')

    def test_num_01(self):
        print('test_num_01')
        # 判断两个数值是否相等
        self.assertEqual(2, 2, '相等')
        # h不再tis中
        # self.assertNotIn('h', 'tis')

    # 跳过执行test_num_02用例
    @unittest.skip
    def test_num_02(self):
        print('test_num_02')
        # 判断两个数值是否相等
        self.assertEqual(2, 2, '相等')

    # 符合1 + 1 == 2的条件 则跳过test_num_03的case
    @unittest.skipIf(1 + 1 == 2, '符合判断则跳过')
    def test_num_03(self):
        print('test_num_03')
        # 判断两个数值是否相等
        self.assertEqual(2, 2, '相等')

    # 每次执行完case时 最后执行tearDown
    def tearDown(self) -> None:
        print('tearDown')

    # 执行完类中所有case时 最后调用tearDownClass
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()

# 被测试代码块
# def demo_method(a, b, x):
#     if a > 1 and b == 0:
#         x = x / a
#
#     elif a == 2 or x > 1:
#         x += 1
#
#     return x
#
#
# num = demo_method(3, 0, 3)
# print(num)
