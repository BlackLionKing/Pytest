import time

import allure
import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
"""
    chrome dirver链接
        http://chromedriver.storage.googleapis.com/index.html
    
    mac配置chrome driver教程
        https://zhuanlan.zhihu.com/p/112406390

"""


@allure.testcase('https://www.baidu.com/', '链接')
@allure.feature('搜索')
@pytest.mark.parametrize('data', (['allure', 'pytest', 'unittest']))
def test_selenium_attach(data):

    with allure.step('打开百度'):
        # 关联webdriver
        driver = webdriver.Chrome()
        # get请求
        driver.get('http://www.baidu.com/')

    with allure.step('搜索关键字' + data):
        # 拿到百度输入框的id 并 输入值
        driver.find_element_by_id('kw').send_keys(data)
        # 暂停2秒
        time.sleep(2)

        # 拿到百度一下的id 并 点击
        driver.find_element_by_id('su').click()
        # 暂停2秒
        time.sleep(2)

    with allure.step('保存图片'):
        # 截图保存图片
        driver.save_screenshot('./pic_' + data + '.jpg')
        # 将图片保存到报告中
        allure.attach.file('./pic_' + data + '.jpg', '测试图片', allure.attachment_type.JPG)

    with allure.step('关闭浏览器'):
        driver.quit()


if __name__ == '__main__':
    pytest.main('-v -s')
