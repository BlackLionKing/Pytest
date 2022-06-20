import requests
import re

# 图片地址url
url = 'https://api.m.jd.com/ware/detail/getIntroduceInfo'

# 请求头
headers = {
    'cookie':
        'shshshfpa=b4d67afb-b64c-13bc-5040-797f123e9e78-1655278059; __jdv=122270672|direct|-|none|-|1655278059234; __jdu=16552780592342010836988; shshshfpb=ilIjLJyYAo1Ra-kg1tAwjMA; areaId=1; ipLoc-djd=1-2802-54745-0; __jdc=122270672; ip_cityCode=2802; 3AB9D23F7A4B3C9B=NZFXCBW3YQHY7UXL6O6AFN5IYVLTFQBZGG5J4B4FZX7AWJLVWJ7XNGPKW45NA7GY2FQPVHGZE6RTQFGSQE7R7PE7LA; visitkey=21905034944548948; wxa_level=1; retina=1; cid=9; jxsid=16552797068506880007; webp=1; mba_muid=16552780592342010836988; sc_width=400; equipmentId=NZFXCBW3YQHY7UXL6O6AFN5IYVLTFQBZGG5J4B4FZX7AWJLVWJ7XNGPKW45NA7GY2FQPVHGZE6RTQFGSQE7R7PE7LA; deviceVersion=102.0.5005.61; deviceName=Chrome; sk_history=10039552855611%2C; warehistory="10039552855611,10039552855611,10039552855611,10039552855611,"; wqmnx1=MDEyNjM1MnQvLi5wYzAyMW0xMzU4bC5pIG8uZTVsQSBlaTcoTGtjQ2UuMCBsZjU2M1lkZjQzVlJERkgmUg%3D%3D; __jda=122270672.16552780592342010836988.1655278059.1655282381.1655284812.3; __jdb=122270672.1.16552780592342010836988|3.1655284812; mba_sid=16552848128496406264859151107.1; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1655284814803_1; __jd_ref_cls=MDownLoadFloat_AppArouseA1; __wga=1655284815278.1655284815278.1655282382882.1655279710351.1.3; PPRD_P=UUID.16552780592342010836988-LOGID.1655284815308.199045033; _gia_s_local_fingerprint=089a312483edea8a62390f60eb3da5f0; fingerprint=089a312483edea8a62390f60eb3da5f0; deviceOS=android; deviceOSVersion=6.0; _gia_s_e_joint={"eid":"NZFXCBW3YQHY7UXL6O6AFN5IYVLTFQBZGG5J4B4FZX7AWJLVWJ7XNGPKW45NA7GY2FQPVHGZE6RTQFGSQE7R7PE7LA","ma":"","im":"","os":"Android 6.x","ip":"1.119.196.77","ia":"","uu":"","at":"6"}; shshshfp=9e9cdc146979f36333da41265ea14073; shshshsID=0f811ccb77b8c79ba591a87997e1b025_1_1655284818773',
    'User-Agent':
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36',
    'referer':
        'https://item.m.jd.com/',
    }

# 参数
params = {
        'loginType': 2,
        'appid': 'm_core',
        'uuid': '21905034944548948',
        'functionId': 'item_intruduce_info',
        'body': '{"externalLoginType":1,"par":"100011657503_d100011657503_normal"}'}

# 发送请求
res = requests.get(url, params, headers=headers)

# 正则匹配url
re_list = re.findall('background-image:url\((.*?)\)', res.text)

# 循环发送下载图片
i = 0
for img_url in re_list:
    pic_url = 'https:' + img_url
    img_headers = {
            'User-Agent':
                    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36',
            'referer':
                    'https://item.m.jd.com/'
    }
    img_res = requests.get(pic_url, headers=img_headers)

    with open('./pic/%d.jpg' % i, 'wb') as f:
        f.write(img_res.content)

    i += 1
 
