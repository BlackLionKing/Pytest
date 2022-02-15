"""
    执行测试用例
        匹配某个目录下所有以unittest开头的py文件 执行这些文件下的所有用例

        unittest.defaultTestLoader.discover.discover()方法可以一次调用多个文件并执行
        test_dir 被测试脚本的目录路径
        pattern 文件名称匹配规则

    测试用例执行过程

"""

import unittest

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, 'unit*.py')
unittest.TextTestRunner().run(discover)
