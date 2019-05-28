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

    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.0(0x17000024) NetType/WIFI Language/zh_CN',
               "Cookie": "Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad={0}; Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad={0}; PHPSESSID=794dd1b7df17ed62466a286869ae2d59".format(int(time.time())),
               "Referer": "http://cone.sngzzc.com/app/index.php?i=10&c=entry&id=98518&rid=321812&do=view&m=tyzm_diamondvote&from=singlemessage&isappinstalled=0&wxref=mp.weixin.qq.com&wxref=mp.weixin.qq.com",
               "Host": "cone.sngzzc.com",
               "Origin": "http://cone.sngzzc.com",
               "X-Requested-With": "XMLHttpRequest"}
    postParams = json.dumps({"latitude": 0, "longitude": 0, "verify": 0})
    # cookie = {"Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad": int(time.time()), "Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad": int(time.time()), "PHPSESSID": "dd1f82b306d81dfa01d511f7d694a543"}
    # conn.request("POST", "http://cone.sngzzc.com/app/index.php?i=10&c=entry&rid=321812&id=98518&do=vote&m=tyzm_diamondvote", postParams, headers)
    r = requests.post("http://cone.sngzzc.com/app/index.php?i=10&c=entry&rid=321812&id=98518&do=vote&m=tyzm_diamondvote", data=postParams, headers=headers)
    print(r.text)
    print(r.headers)
    print(r.content)
    # print(r.json())
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
