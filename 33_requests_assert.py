import requests
# 解析模版(json xml等)引擎
import pystache
# 解析json
from jsonpath import jsonpath
import pytest
# 断言工具hamcrest 可以组合创建灵活的匹配器进行断言
from hamcrest import *


class Test_demo(object):

    # 每个方法执行前运行一次
    def setup(self):
        self.url = 'https://fanyi.baidu.com/sug'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

        # 将mustache内 value变量 替换成真实数据
        test_json = {'value': 'mustache'}
        r = pystache.Renderer()
        # 加载模版test_two 并进行数据替换
        content = r.render_name('test_two', test_json)

        # 将str转换为dict
        self.dict_content = eval(content)
        # 发送json
        self.response = requests.post(self.url, data=self.dict_content, headers=self.headers, verify=False)

    def test_assert(self):
        print(self.response.json()['data'][0]['v'])
        # 进行断言 返回内容中是否包含 "胡子"
        """
            断言条件
                in 包含
                ==
                != 
                is 是否同一内存地址
                isinstance(x, dict) x是否是dict类型

        """
        assert "胡子" in self.response.json()['data'][0]['v']

    def test_assert_two(self):
        print(jsonpath(self.response.json(), '$..v')[0])
        # jsonpath提取数据后 进行断言
        assert "胡子" in jsonpath(self.response.json(), '$..v')[0]

    def test_assert_three(self):
        print(jsonpath(self.response.json(), '$..v')[0])
        # assert_than断言
        # 是否包含胡子字符串
        assert_that(jsonpath(self.response.json(), '$..v')[0], contains_string("胡子"))


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
