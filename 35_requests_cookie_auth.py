import requests
from requests.auth import HTTPBasicAuth
"""
    auth
        授权 发送账号密码 服务器进行解密 然后与数据库数据校验 
        在requests参数中指定auth参数
    cookie
        可使用headers参数携带
        可使用cookies参数携带
        
    
"""
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # headers中携带cookie
    'Cookie': 'cookies'
}
test_json = {'kw': 'mustache'}
# 发送json
# response = requests.post(url, data=test_json, headers=headers, verify=False,)

# 携带auth参数
# response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))

# 携带cookie参数
response = requests.get('https://api.github.com/user', cookies={'cookie': 'cookievalue'})

print(response.cookies)

"""
    get()   
        每次会自动关闭链接
    session().get()
        不关闭链接 保持会话 再次使用该session对象访问其他页面时 都会默认使用该session之前的cookie参数
        可以自动处理cookie 
"""
# print(requests.session().get('https://www.baidu.com'))
