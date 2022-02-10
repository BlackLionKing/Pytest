import requests

"""
    requests
        底层实现是urllib
        在python2 及 python3中通用 方法一致
        能够自动帮助我们解压响应内容
"""

"""
    发送get请求 获取响应
    response常用属性
        text                响应体 str类型
            解码类型：自动根据http头部 Content-Type 对响应的编码作出有根据的推测 进行解码
            修改编码方式：response.encoding = 'utf8'
            
        content             响应体 bytes类型
            解码类型：没有指定
            修改编码方式：response.content.decode('utf8')
            
        status_code         响应状态码
        request.headers     响应对应的请求头
        headers             响应头
        requests._cookies   响应对应请求的cookie
        cookies             响应的cookie (经过了set-cookie动作)
        
        更推荐使用response.content.decode()的方式获取响应的html页面
"""

"""
# 发送请求
url = 'https://www.baidu.com'
response = requests.get(url)
# 获取响应头
print(response.headers)
# 对响应解码
response.encoding = 'utf8'
# 获取响应内容
print(response.text)
"""
"""
# 下载图片
# url = 'https://www.baidu.com/img/bd_logo1.png'
# response = requests.get(url)

# 创建一个文件 以二进制写入
# with open('baidu.png', 'wb') as file:
#     file.write(response.content)
"""


"""
    发送带header的请求
"""

"""
url = 'https://www.baidu.com'
# 携带user-agent请求头 模拟浏览器发送请求 字典类型
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
response = requests.get(url, headers=headers)
# 打印请求头信息
print(response.request.headers)
# 打印响应体 并 解码
print(response.content.decode())
"""


"""
    发送带参数的请求
    参数：
        URL地址中 很多参数字段是没用的
        ?后面的就是请求参数
    
    请求参数的形式 字典：
        kw = {'wd': '值值'}
    
    使用方法
        requests.get(url, params = kw)
        
"""
# URL写上参数 直接发送
# url = 'https://www.baidu.com/s?wd=python'
# url不携带参数 ?号带不带没有区别
url = 'https://www.baidu.com/s'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
# 拼接参数 字典类型 等同于ie=UTF-8&&wd=python
params = {'ie': 'UTF-8', 'wd': 'python'}
response = requests.get(url, headers=headers, params=params)
print(response.content.decode())
