# **外卖运营数据爬取**
##1.获取一个坐标（一个店铺的位置）
  * 通过百度地图开放平台获取地址编码
  
  * URL = http://api.map.baidu.com/geocoder/v2/?address=&output=json&ak=&ret_coordtype=gcj02ll
  * AK = 1Wb5b9QMPzxput1CpMazlaSd81lLHtyw
  * 例：http://api.map.baidu.com/geocoder/v2/?output=json&ak=1Wb5b9QMPzxput1CpMazlaSd81lLHtyw&address=益园文创基地
  * {
        status: 0,
        result: {
            location: {
                lng: 116.24196723411502,
                lat: 39.958382784988025
            },
            precise: 0,
            confidence: 50,
            comprehension: 100,
            level: "工业园区"
         }
     }
  * 通过python-geohash算法计算坐标（latitude,longitude）的geohash值
##2.获取这个店铺周围外卖商家信息
* 通过饿了么、美团外卖移动端接口获取商家数据 

* 饿了么：https://h5.ele.me/
* 美  团：http://m.waimai.meituan.com/waimai/mindex/home




##3.遍历第二步商家ID，获取其店铺内商品列表（SKU）




---
