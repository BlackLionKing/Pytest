"""
    希望在报告中看到测试功能 子功能或者场景、测试步骤、包括测试附加信息
    解决
        功能上加    @allure.feature('功能名称')
        子功能上加  @allure.story('子功能名称')
        步骤上加    @allure.step('步骤细节')
        allure.attach('具体文本信息') 需要附加的信息 可以是数据 文本 图片 视频 网页

        如果只测试某一功能是否正常运行 可以加限制过滤
        pytest 文件名 --allure-features '功能名'
        pytest 文件名 --allure-stories '子功能名称'

    feature 与 story的关系
        feature相当于一个功能 一个大的模块 将case分类到某个feature中 在报告"功能"模块中显示 相当于测试套件
        story相当于对应这个功能或者模块下的不同场景、分支功能、属于feature之下的结构 在报告features中显示 相当于测试用例
        feature 与 story 类似于父子关系

    allure-step
        测试过程中每个步骤 一般放在具体逻辑方法中
        可以放在关键步骤中 在报告中显示
        在app web 自动测试当中 建议每切换一个新的页面当做一个step

        用法
            @allure.step()          以装饰器的形式放在类或方法上
            with allure.step()      可以放在方法里面 但是测试步骤的代码需要被该语句包含

    关联链接
        @allure.link(url, name)

    关联测试用例
        @allure.testcase(url, name)

    关联bug地址
         @allure.issue(bug_id, name)

         执行命令 后面加链接 {}内自动关联bug_id
            --allure-link-pattern=issue:bug链接{}

         完整命令:
            pytest 文件名 --allure-link-pattern=issue:链接{} --alluredir=Json目录



"""

import allure


# 功能
@allure.feature('登陆')
class Test_login(object):

    # 子功能
    @allure.story('用户名')
    def test_input_user(self):
        print('test_input_user')
        assert 1 == 2

    @allure.story('密码')
    def test_input_password(self):
        print('test_input_password')

    # 测试步骤
    @allure.step('验证码')
    def test_num(self):
        print('test_num')

    # 添加link
    @allure.link('https://www.baidu.com/', name='URL')
    def test_login(self):
        # 测试步骤
        with allure.step('登陆按钮'):
            print('提交用户名')
            print('提交密码')
        print('test_login')

    # 关联测试用例
    @allure.testcase('https://www.pgyer.com/Y7WQ', 'testcase_url')
    def test_case(self):
        print('test_case')

    """
        jira bug链接：https://jira.zc3u.com/secure/RapidBoard.jspa?rapidView=161&projectKey=NEWSAAS&view=detail&selectedIssue=NEWSAAS-59
        关联bug 第一个参数指定bug_id 第二个参数指定name
        执行命令 
            pytest 29_allure常用功能.py 
                # 指定bug链接 {}内自动关联issue装饰器内的参数
                --allure-link-pattern=issue:https://jira.zc3u.com/secure/RapidBoard.jspa\?rapidView\=161\&projectKey\=NEWSAAS\&view\=detail\&selectedIssue\={}
                # 指定json存储的文件夹 
                --alluredir=./allure_two
    """

    @allure.issue('NEWSAAS-59', 'bug_url')
    def test_bug(self):
        print('test_bug')

