#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-10-9 10:05
    @Author  : Joseph
    @File    : eleme_start.py
    @Software: PyCharm
    @Description :
'''

from eleme import eleme_restaurant_info
from eleme.eleme_menu import get_all_rst_menu
from eleme.eleme_restaurant_info import get_restaurant_data_count

if __name__ == '__main__':  # 程序运行入口
    # city = '石家庄市'
    # name = ''
    keyword = '石家庄市西里北街菜市场'
    count = 20
    # order_by = 6  # 按销量排序
    order_by = 5  # 按距离最近排序
    restaurant_category_ids = 1  # 简餐便当
    get_restaurant_data_count(keyword, count, order_by, restaurant_category_ids)
    # time.sleep(2)
    excel_name = eleme_restaurant_info.excelName(keyword)
    get_all_rst_menu(excel_name)
