#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-10-9 10:49
    @Author  : Joseph
    @File    : rearch_poi.py
    @Software: PyCharm
    @Description :
'''
import json

import requests


def get_poi(keyword):
    url = "https://h5.ele.me/restapi/bgs/poi/search_poi_nearby_alipay"
    param = {
        "keyword": keyword
    }
    headers = {
        'Cookie': "SID=D0hkTsFU4Lt9DQUhn0O85Qyxfa2rmIUw8dqg",
        'Cache-Control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=param)
    print(response.text)
    poi_data = json.loads(response.text)
    return poi_data[0]


if __name__ == '__main__':
    get_poi("北京益园文创基地")
