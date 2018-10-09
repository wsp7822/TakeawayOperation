#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-9-29 21:53
    @Author  : Joseph
    @File    : setting.py
    @Software: PyCharm
    @Description :
'''
# 商家基本信息文件保存路径
RESTAURANT_INFO_DIR = "C:\\Users\\dell\\Desktop\\temp\\爬虫饿了么"

# 商家ID，经纬度坐标
RESTAURANT_ID_INFO = "C:\\Users\\dell\\Desktop\\temp\\爬虫饿了么\\keyword.xlsx"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Refer": "https://h5.ele.me/shop/",
    "Cookie": "SID=D0hkTsFU4Lt9DQUhn0O85Qyxfa2rmIUw8dqg"
}

# Baidu Map API AK (http://api.map.baidu.com)
BAIDU_AK = "1Wb5b9QMPzxput1CpMazlaSd81lLHtyw"
BASE_URL = 'http://api.map.baidu.com/geocoder/v2/?'

# 饿了么相关RUL
ELEME_RESTAURANT_URL = "https://h5.ele.me/restapi/shopping/v3/restaurants?"
RESTAURANT_ID = ""
ELEME_MENU_URL = "https://h5.ele.me/pizza/shopping/restaurants/%s/batch_shop"

# 美团相关URL
MEITUAN_BASE_URL = ""
MEITUAN_MENU_URL = ""


# Mysql Setting
# WAIMAI_PLATFORM 外卖平台，仅用来选择数据库名称
WAIMAI_PLATFORM = "eleme"
# MYSQL_DBNAME_LIST 指定各外卖平台爬取时存取数据使用的数据库
MYSQL_DBNAME_LIST = {
    "eleme": "eleme",
    "meituan": "meituan",
    "baidu": "baidu"
}
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = MYSQL_DBNAME_LIST[WAIMAI_PLATFORM]
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306

