#!/usr/bin/python2.7
import requests, json
from qiniu import Auth, put_file
import os

def bing():
    url = 'http://bing.ioliu.cn/v1?d=0'
    r = requests.get(url).json()
    imgurl = str(r['data']['url'])
    keyurl = str(r['data']['enddate'])
    name = 'B-' + keyurl + '.jpg'
    content = requests.get(imgurl).content
    with open(name,'wb') as f:
        f.write(content)
    return name

def upload(key):
    access_key = 'Fx9CvaSHqUFVrofBgpGxAdsR3UV0SNB2bRof6ss2'
    secret_key = 'eW8fX00uUZukKcFsZyeIWw3BTyfhyoIhGQ4j5NwN'
    q = Auth(access_key, secret_key)
    bucket_name = 'bing'
    token = q.upload_token(bucket_name, key, 3600)
    localfile = key
    put_file(token, key, localfile)

if __name__ == '__main__':
    name = bing()
    upload(name)
    os.remove(name)
