#!/usr/bin/python2.7
import requests, json
from qiniu import Auth, put_file
import os

def upload(key):
    access_key = 'Fx9CvaSHqUFVrofBgpGxAdsR3UV0SNB2bRof6ss2'
    secret_key = 'eW8fX00uUZukKcFsZyeIWw3BTyfhyoIhGQ4j5NwN'
    q = Auth(access_key, secret_key)
    bucket_name = 'bing'
    token = q.upload_token(bucket_name, key, 3600)
    localfile = key
    put_file(token, key, localfile)

url = 'http://bing.ioliu.cn/v1?d='

for i in [url + str(d) for d in range(0,267)]:
    r = requests.get(i).json()
    imgurl = r['images'][0]['url']
    name = 'B-' + r['images'][0]['attribute']
    with open(name,'wb') as f:
        f.write(requests.get(imgurl).content)
    upload(name)
    os.remove(name)
