"""
    带上cookie的作用
        能够访问登录后的界面
        一套cookie对应的是一个用户信息

    requests处理cookie的三种方法
        1。cookie字符串放在headers中
        2。把cookie字典传给请求方法的cookies参数接收
        3。使用requests提供的session模块
            实现客户端和服务端的会话保持
            保存cookie 下一次请求会带上前一次的cookie
            实现和服务端的长链接 加快请求速度
            使用方法
                session = requests.session()
                response = session.get(url,headers)
            session实例在请求了一个网站后 对方服务器设置在本地的cookie会保存在session中
            下一次在使用session请求对方服务器的时候 会带上前一次的cookie

"""

import requests
from requests import utils

# 模拟登陆 访问登陆接口
url = 'http://172.16.2.19:8096/api/user/login'
# cookie存放在headers中
headers = {'Cookie': 'uid=20; SECKEY_ABVK=3PInt4rdcBsmEO/Y9vJMibwEvEiI574NlBrGAcocemc%3D; BMAP_SECKEY=0TBp_-bbotETRw266s1nJprOkUr7alKWuKHu8zZ4ZmtPFIuvHpB-1l5WuWIOYnqEvFc7OZFBlZT-mNoG3IEhsTgDKhNLU4V1jt2p2Sge7wIjvmqmPYu-zfKH24gippM9KjtTTiia_diPbcLjeQBBoRUg0ZRLWhj_DS5rmi5GadsUqXFyjdF5f-b02IP2KtHH; JSESSIONID=D839179EEC24F25AF7E9928FC18AB5BD; token=40e9e756e237218b', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
# 携带参数
data = {'username': 'liujian', 'password': 123456, 'code': 123344, 'timestamp': 1644473282, 'sign': '4efb9a7412'}
# 发送post请求
response = requests.post(url, headers=headers, data=data)
# 使用requests.session处理cookie
# session = requests.session()
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
# 发送请求
# response = session.post(url, headers=headers, data=data)

# response.cookies是CookieJar类型
# 使用requests.utils.dict_from_cookiejar，能够实现把cookiejar对象转化为字典
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
print(response.content.decode())

"""
    解决RequestsDependencyWarning警告
        升级requests模块

"""
