#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-9-29 21:40
    @Author  : Joseph
    @File    : geocoding.py
    @Software: PyCharm
    @Description :
'''

import json
from urllib import parse, request
import geohash
import setting


def get_geocoding(city, keyword):
    params = {
        "city": city,
        "address": keyword,
        "output": "json",
        "ret_coordtype": "gcj02ll",
        "ak": setting.BAIDU_AK
    }
    params = parse.urlencode(params)  # 请求参数编码
    req_full_url = setting.BASE_URL + params  # 重新生成url请求
    print(req_full_url)
    web_page = request.urlopen(req_full_url)
    geohash_result = web_page.read().decode("utf-8")
    print(geohash_result)
    if geohash_result != "{}":
        json_data = json.loads(geohash_result)
        if json_data['status'] is 0:
            result = json_data['result']['location']
            result['geohash'] = get_geohash(result['lat'], result['lng'])
        return json_data['result']['location']
    else:
        return


def get_geohash(lat, lng):
    return geohash.encode(lat, lng)


if __name__ == '__main__':
    # print(str(get_geocoding('北京', '益园文创基地')))
    print(str(get_geocoding('北京市', '中关村')))
