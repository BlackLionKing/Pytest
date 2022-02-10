import requests
"""
    requests使用代理
    为什么使用代理？
        让服务器以为不是同一个客户端在请求
        防止真实ip泄漏

    访问流程：
        浏览器 <-> requests <-> 代理 <-> requests <-> web服务

    正向代理：对于浏览器知道服务器的真实地址，例如VPN
    反向代理：浏览器不知道服务器的真实地址，例如nginx

    使用代理 proxies参数
    类型：字典
        requests.get(url, headers, params, proxies)

    例如 指定好协议类型
    proxies = {
      "http": "http://12.34.56.79:9527",
      "https": "https://12.34.56.79:9527",
      }
"""


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'}

url = 'http://ip.chinaz.com/'

ip_port = '101.236.35.98:8866'  # 西刺代理 <千万不要复制页面上的内容>

proxies = {
    "http": "http://{}".format(ip_port),
    "https": "https://{}".format(ip_port),
}

resp = requests.get(url, headers=headers, proxies=proxies)

print(resp.text)
