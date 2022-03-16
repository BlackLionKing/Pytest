import requests
import pystache


"""
    哪些地方用到post请求
        登陆注册
        需要传输大文本内容(post请求对数据长度没有要求)

    get post请求可传递的值大小 http协议对其没有限制 有限制的是服务器和浏览器

    requests发送post请求
    data类型：字典
        requests.post(url, data, headers)

"""
# 指定url
url = 'https://fanyi.baidu.com/langdetect'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
data = {'query': '托尔斯泰'}
print(type(data))
# 发送data
# response = requests.post(url, data=data, headers=headers, verify=False)

# 将mustache内 value变量 替换成真实数据
test_json = {'value': '托尔斯泰'}
r = pystache.Renderer()
# 加载模版test 并进行数据替换
content = r.render_name('test', test_json)
# 将str转换为dict
dict_content = eval(content)
print(type(dict_content))

# 发送json
response = requests.post(url, json=dict_content, headers=headers, verify=False)
print(response.json())

