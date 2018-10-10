#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    @Time    : 2018-10-10 20:03
    @Author  : Joseph
    @File    : meituan_start.py
    @Software: PyCharm
    @Description :
'''
from meituan import meituan_restaurant_info
from meituan.meituan_menu import get_all_rst_menu
from meituan.meituan_restaurant_info import get_restaurant_data_count

if __name__ == '__main__':  # 程序运行入口
    keyword = "石家庄市西里北街菜市场"
    count = 20  # 20的整倍数
    sortId = 1  # 销量最高
    # sortId = 5  # 距离最近
    secondCategoryId = 101262  # 快餐便当
    get_restaurant_data_count(keyword, count, sortId)

    excel_name = meituan_restaurant_info.excelName(keyword)
    get_all_rst_menu(excel_name)
