import requests
import json
import re
import datetime

print('000')

yh = []

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"永辉已兑换._{current_time}.txt"

print('111')

#获得输入的手机号
input_str = input("请输入手机号，用逗号分隔：")
phone = input_str.split(',')

#打开文档
with open('yonghui.txt', 'r',encoding = 'utf-8') as f:
    text = f.read()

# 匹配链接的正则表达式
regex =  r'https:\/\/dev\.coc\.10086\.cn\/coc3\/gr\/static-2c\/rightsget\/#\/yongHuiRights\?coupon=\w+'

# 使用re.findall()方法提取所有匹配的链接
links = re.findall(regex, text)

print('links')
print(links)

for i in phone:
    for j in links:
        session = requests.session()
        use_phone = i
        use_token = j[76:]
        use_url = j

        form_data = json.dumps({
            "token": use_token,
            "serverNum": use_phone,
            "frontOrderUrl": use_url,
            "channelId": "",
            "from": ""
        })

        req_header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "222",
            "Content-Type": "application/json;charset=UTF-8",
            "Dnt": "1",
            "Host": "dev.coc.10086.cn",
            "Origin": "https://dev.coc.10086.cn",
            "Referer": "https://dev.coc.10086.cn/coc3/gr/static-2c/rightsget/",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

        url = "https://dev.coc.10086.cn/coc3/coc3-market-order/api/external/order/confirmYhCard"

        response = session.post(url=url, headers=req_header, data=form_data)

        pattern = r'"couponUrl":"(.*?)"'
        result = re.search(pattern, response.text)



        if result:
            link = result.group(1)

            bheaders = {
                'Host': 'exch.jf180.vip',
                'Accept': 'application/json, text/plain, */*',
                'Sec-Fetch-Site': 'same-origin',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Sec-Fetch-Mode': 'cors',
                'Content-Type': 'application/json',
                'Origin': 'https://exch.jf180.vip',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1',
                'Referer': link,
                'Content-Length': '52',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'empty',
            }


            s_data = json.dumps({"couponEncrypt": link[28:]})
            response1 = session.post(url='https://exch.jf180.vip/api/exchange-h5/order/getAccountUse',
                                    headers=bheaders,data=s_data)
            tmp=requests.get("https://exch.jf180.vip/api/exchange-h5/order/use/result?mobile=&code="+link[28:]).text
            pattern1 = r'https:\/\/cardup\.cn\/[a-zA-Z0-9]+'
            match_obj = re.search(pattern1, tmp)
            if match_obj:
                print(match_obj.group(0))
                yh.append(match_obj.group(0))
        else:
            print("未找到链接")

yh= list(set(yh))
for n in yh:
    with open(filename, 'a') as f:
        f.write(n + '\n')