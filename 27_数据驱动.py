"""
    数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变
    简单来说 就是参数化的应用 数据量小的测试用例可以使用代码的参数化来实现数据驱动
    数据量大的情况下 建议大家使用一种结构化的文件(json yaml等) 来对数据进行存储 然后在测试用例中读取这些数据

    数据驱动应用场景
        app web 接口自动化测试
            测试步骤的数据驱动
            测试数据的数据驱动
            配置的数据驱动
"""
import pytest
import yaml


class Test_demo(object):
    @pytest.mark.parametrize('env', yaml.load(open('./test.yml'), Loader=yaml.Loader))
    def test_yaml(self, env):
        if 'dev' in env:
            # 取字典里的值
            print(env['dev'])
        elif 'test' in env:
            # 取字典里的值
            print(env['test'])
