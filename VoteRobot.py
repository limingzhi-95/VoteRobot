#encoding=utf-8

import sys
import time
import random
import string
import json
import http.client
import urllib.parse
import requests


# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = 'owzeBj'
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString

# 对指定的作品（zpid）投一张票
def voteOnce():
    # conn = http.client.HTTPConnection("cone.sngzzc.com")

    headers = {
        'Host': "cone.sngzzc.com",
        'Connection': "keep-alive",
        'Content-Length': "31",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Origin': "http://cone.sngzzc.com/",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044704 Mobile Safari/537.36 MMWEBID/7979 MicroMessenger/7.0.4.1420(0x2700043B) Process/tools NetType/WIFI Language/zh_CN",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Referer': "http://cone.sngzzc.com/app/index.php?i=10&c=entry&id=98518&rid=321812&do=view&m=tyzm_diamondvote&from=singlemessage,https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx79dfbd36ddd5b765&redirect_uri=http%3A%2F%2Fcone.sngzzc.com%2Fapp%2Findex.php%3Fi%3D10%26c%3Dauth%26a%3Doauth%26scope%3Dsnsapi_base&response_type=code&scope=snsapi_base&state=we7sid-7fa4219be5968e8a163d1b5499fcdced#wechat_redirect",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,en-US;q=0.9",
        'Cookie': "PHPSESSID=04467c5f03501a0874a243d0d635e537;Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad={0};Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad={0}".format(str(int(time.time()))),
        'Cache-Control': "no-cache",
    }
    print(headers)
    postParams = json.dumps({"latitude": 0, "longitude": 0, "verify": 0})
    body = {
        "latitude": 0,
        "longitude": 0,
        "verify": 0
    }
    # cookie = {"Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad": int(time.time()), "Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad": int(time.time()), "PHPSESSID": "dd1f82b306d81dfa01d511f7d694a543"}
    # conn.request("POST", "http://cone.sngzzc.com/app/index.php?i=10&c=entry&rid=321812&id=98518&do=vote&m=tyzm_diamondvote", postParams, headers)
    r = requests.post("http://cone.sngzzc.com/app/index.php?i=10&c=entry&rid=321812&id=98518&do=vote&m=tyzm_diamondvote", headers=headers, data="latitude=0&longitude=0&verify=0")
    print(r.text)
    print(r.headers)
    print(r.content)
    print(r.url)
    r.close()
    # print(conn.getresponse().msg)
    # conn.close()

# 投票控制器：指定作品（zpid）和投票张数（voteNum），并随机出投票间隔时间
def voteController(zpid, voteNum):
    print('======== Start to vote zpid({0}), Total votes: {1}'.format(zpid, voteNum))
    for i in range(voteNum):
        voteOnce(zpid)
        randomSleepTime = random.randint(1, 4)
        print('{0} tickets has been voted, the next ticket will be voted after {1} seconds.'.format(i+1, randomSleepTime))
        time.sleep(randomSleepTime)
    print('======== Voting Ended!')


if __name__ == '__main__':
    voteOnce()
    # voteController(38, 3)
