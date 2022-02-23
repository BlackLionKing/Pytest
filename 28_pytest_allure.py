"""
    allure是轻量级支持多语言的测试报告工具
    可以为dev/qa提供详尽的测试报告、测试步骤、测试日志
    由Java语言开发 支持pytest、js、php
    可以集成到jenkins

    mac安装allure
        brew install allure

    python安装依赖包
        pip3 install allure-pytest

    官方文档
        https://docs.qameta.io/allure/#_flaky_tests


    生成报告命令
        pytest 28_pytest_allure.py(文件名) --alluredir=./allure(目录名)     生成json数据 (存储测试结果的路径)
        allure serve ./allure(目录名)                                      在线生成测试报告并运行

        从结果生成报告
            allure generate ./allure(JSON目录名) -o ./report(html报告目录)/ --clean          生成报告(将json数据与html报告关联)
            allure open -h 127.0.0.1 -p 8883 ./report(html目录名)/                          打开报告



"""


def test_demo1():
    print('test_demo1')


def test_demo2():
    print('test_demo2')


def test_demo3():
    print('test_demo3')


def test_demo4():
    print('test_demo4')
