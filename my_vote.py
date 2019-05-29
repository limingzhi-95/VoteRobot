#encoding=utf-8

import sys
import time
import random
import string
import json
import http.client
import urllib.parse
import requests


def voteOnce():
    # conn = http.client.HTTPConnection("cone.sngzzc.com")

    headers = {
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044704 Mobile Safari/537.36 MMWEBID/7979 MicroMessenger/7.0.4.1420(0x2700043B) Process/tools NetType/WIFI Language/zh_CN",
        'Host': "cone.sngzzc.com",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        # 'referer': "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx79dfbd36ddd5b765&redirect_uri=http%3A%2F%2Fcone.sngzzc.com%2Fapp%2Findex.php%3Fi%3D10%26c%3Dauth%26a%3Doauth%26scope%3Dsnsapi_base&response_type=code&scope=snsapi_base&state=we7sid-04467c5f03501a0874a243d0d635e537#wechat_redirect",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    print(headers)

    r = requests.get("http://cone.sngzzc.com/app/index.php?i=10&c=entry&id=98518&rid=321812&do=view&m=tyzm_diamondvote&from=singlemessage&isappinstalled=0", headers=headers)
    print(r.text)
    print(r.headers)
    print(r.content)
    print(r.cookies)
    print(r.url)
    # print(r.json())
    r.close()
    # print(conn.getresponse().msg)
    # conn.close()


if __name__ == '__main__':
    voteOnce()
    # voteController(38, 3)
