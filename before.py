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

for i in [url + str(d) for d in range(1,266)]:
    r = requests.get(i).json()
    imgurl = r['data']['url']
    name = 'B-' + r['data']['enddate'] + '.jpg'
    with open(name,'wb') as f:
        if requests.get(imgurl).content:
            f.write(requests.get(imgurl).content)
            upload(name)
            os.remove(name)
