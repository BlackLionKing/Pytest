"""
    allure.attach()
    场景
        前端ui自动化测试经常需要附加图片或html 在适当的地方截图

    解决
        allure.attach()可以显示许多不同类型的附件 可以补充测试、步骤或结果

    步骤
        在测试报告里附加网页
            allure.attach(body(内容), name, attachment_type, extension)
            allure.attach('<head></head><body>首页</body>', '首页', allure.attachment_type.HTML)

        在测试报告里附加图片
            allure.attach.file(source, name, attachment_type, extension)
            allure.attach.file('./p.jpg', allure.attachment_type.JPG)

"""
import allure


# 文本内容
def test_text():
    allure.attach('text', '文本内容', allure.attachment_type.TEXT)


# html内容
def test_html():
    allure.attach('<body>html内容</body>', '网页内容', allure.attachment_type.HTML)


# 图片内容
def test_pic():
    allure.attach.file('./jpg.jpg', '图片内容', allure.attachment_type.JPG)
