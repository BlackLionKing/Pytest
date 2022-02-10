import requests
from retrying import retry

"""
    requests.utils.dict_from_cookiejar()
        response.cookies获取的是cookiejar类型
        使用requests.utils.dict_from_cookiejar()能够把cookiejar对象转换为字典
   
    request处理证书错误(ssl证书不安全)
        增加一个参数 verify=False
        requests.get(url, verify=False)
    
    超时参数
        请求很久没有返回结果 需要对请求进行强制要求 让他在特定的时间内返回结果 否则报错
        使用方法
            requests.get(url, timeout=3)
        
    retrying模块
        使用timeout参数实现超时报错 但由于部分接口加载过慢 就需要retrying实现重试
        
        使用
            使用retrying模块提供的retry模块
            通过装饰器的方式使用 让被装饰的函数反复执行
            retry中可以传入参数stop_max_attempt_number 让函数报错后继续重新执行
            如果每次都报错 整个函数报错 如果中间有一次成功 程序继续执行
        
        

"""


"""
# 处理cookie
url = 'http://www.baidu.com'
response = requests.get(url)
# 输出 <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(response.cookies)
# 手动输入 没有联想
cookie = requests.utils.dict_from_cookiejar(response.cookies)
# 输出 {'BDORZ': '27315'}
print(cookie)
"""

"""
# 处理证书错误
url = "https://www.12306.cn/mormhweb/"
response = requests.get(url, verify=False)
print(response.content.decode())
"""

"""
# 超时参数 超过三秒就报错
response = requests.get(url='http://www.google.com/', timeout=5)
# 输出 socket.timeout: timed out
print(response.content.decode())
"""


# 重试三次
# _受保护的函数 没有实际代码意义
@retry(stop_max_attempt_number=3)
def _func1():
    # 超时5秒
    response = requests.get(url='http://www.google.com/', timeout=5)
    # 返回
    return response.content.decode()


# 捕获异常
try:
    content = _func1()
except Exception as e:
    print(e)
    # 报错就置为None
    content = None

print(content)

