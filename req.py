#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-10-8 21:32
    @Author  : Joseph
    @File    : req.py
    @Software: PyCharm
    @Description :
'''


import requests

# url = "http://i.waimai.meituan.com/ajax/v6/poi/filter?lat=39.952594&lng=116.235477&_token=eJxVT01rg0AQ/S9z6CWy7ocboxBCizkYqiV19VJ6UCNmadYE3Uab0v/eCaSEDgPvzZvHY+Yb+ngHIaNYgQPnpocQGKFkDg7YATdSBNRfMM4FWzhQ/9c85jlQ9UUE4ZvwpYPa+1V4xfku3Bn3sK+OGA2wt/YUuq4mY6lNqYlptP0sO1Ifjbs/mmZ1KO1SBCSQXAbew6Frl4zNCRfS8328DzDJKExC/LhheUP7Nyf4EHoH3XbIms2kMj3Faj1jaaGes+xrSqsqHy5blvQ5zevzJvNrlkZKJZeYp2otivHlpGs3yaixQ1RsH9snykY5g59fUdlXUQ=="
# url = "http://m.waimai.meituan.com/waimai/ajax/newm/filterconditions?initialLat=39.952594&initialLng=116.235477&actualLat=&actualLng=&geoType=2&_=1539082340997"
url = "http://m.waimai.meituan.com/waimai/ajax/newm/kingkongshoplist?startIndex=0&sortId=1&navigateType=101260&firstCategoryId=101260&secondCategoryId=101262&initialLat=39.952594&initialLng=116.235477&geoType=2"
querystring = {"platform": "3", "partner": "4", "page_index": "0", "apage": "1"}

headers = {
    'Cookie': "iuuid=1049588802437427258; waimai_cityname=%E5%9F%8E%E5%B8%82%E5%90%8D%E5%B7%B2%E5%88%A0%E9%99%A4",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }

# response = requests.request("POST", url, headers=headers, params=querystring)
response = requests.request("GET", url, headers=headers)

print(response.text)
