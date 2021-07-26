# -*- coding: utf-8 -*-
'''
Created on 2019年7月30日

@author: likecan
'''
# 用于编辑接口测试的主要函数，即接口信息发送的函数
import requests, chardet, json


class interfacetest_main:

    def __init__(self, url, net_type, data=None, header=None):
        self.data = data
        self.header = header
        self.net_type = net_type
        self.url = url

    def net_send(self):
        net_response = None
        if self.net_type.lower() == 'get':
            net_response = requests.get(self.url, params=self.data, headers=self.header)
        elif self.net_type.lower() == 'post':
            net_response = requests.post(self.url, params=self.data, headers=self.header)
        return net_response.ok

    def interface_send(self, url, data=None, post_type='get'):
        if data:
            if not isinstance(data, dict):
                return None
        interface_return = getattr(requests, post_type.lower())(url, data).json()
        return json.dumps(interface_return, sort_keys=True, indent=2)

# if __name__=='__main__':
#     header={'Host': 'www.baidu.com',
#           'Connection': 'keep-alive',
#           'Upgrade-Insecure-Requests': '1',
#           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#           'Accept-Encoding': 'gzip, deflate, br',
#           'Accept-Language': 'zh-CN,zh;q=0.9',
#           'Cookie': 'BAIDUID=71ADB86F20AA50972B1240BC19DA21C0:FG=1; BIDUPSID=71ADB86F20AA50972B1240BC19DA21C0; PSTM=1552612555; BD_UPN=12314353; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; MCITY=-180%3A; BDRCVFR[OLBHF9POoOt]=mk3SLVN4HKm; delPer=0; H_PS_PSSID=; BDUSS=EgtcmNpNjl5b0ZjOFNlcEUwRnAydHJWa3c4R01HNHRKZlpwTEdZSVI4TWd2V2xkSUFBQUFBJCQAAAAAAAAAAAEAAACdSngLbGtjNTY2MzE1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAwQl0gMEJdW; BD_HOME=1; BDRCVFR[WxkyScJ6Xrn]=mk3SLVN4HKm; BD_CK_SAM=1; PSINO=7; pgv_pvi=1961394176; pgv_si=s5785531392; H_PS_645EC=2c3aMJ0fA4EkeqxOQAOWXGBR9hvcfqNne3XRinys7vN0r2n3wkPpFZfLNlpuqCO9LlMo3jAn; sug=3; sugstore=1; ORIGIN=0; bdime=0; WWW_ST=1564623720117; ISWR=13; ISSW=1'}
#     data=None
#     res = requests.get('https://www.baidu.com/')
#     print(res.ok)
# #     interface_demo = interfacetest_main()
# #     interface_demo.net_send()
