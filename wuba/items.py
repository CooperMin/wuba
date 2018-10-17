# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class WubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()               #(1)城市
    borough = scrapy.Field()            #(2)区县
    street = scrapy.Field()             #(3)街道
    username = scrapy.Field()           #(4)用户名/姓名
    tel = scrapy.Field()                #(5)电话
    pubTime = scrapy.Field()            #(6)发布时间
    price = scrapy.Field()              #(22)价格(万元)
    realsize = scrapy.Field()           #(24)户型
    area = scrapy.Field()               #(25)面积
    towards = scrapy.Field()            #(26)朝向
    realEstateE = scrapy.Field()        #(7)产权年限
    buildYear = scrapy.Field()          #(8)建筑年代
    bankcard = scrapy.Field()           #(9)是否绑定银行卡
    realName = scrapy.Field()           #(10)是否真实姓名
    weixin = scrapy.Field()             #(11)是否绑定微信
    zhima = scrapy.Field()              #(12)是否绑定芝麻信用
    zhimaFen = scrapy.Field()           #(13)芝麻分
    wirteTime = scrapy.Field()          #(14)写入时间
    huxingshi = scrapy.Field()          #(15)户型/室
    huxingwei = scrapy.Field()          #(16)户型/卫
    huxingting = scrapy.Field()         #(17)户型/厅
    jushishuru = scrapy.Field()         #(18)居室
    HireType = scrapy.Field()           #(19)租用类型
    MinPrice = scrapy.Field()           #(20)最低价格(万元)
    userid = scrapy.Field()             #(21)用户ID
    title = scrapy.Field()              #(23)标题
    xiaoqu_lat = scrapy.Field()         #(27)纬度
    xiaoqu_lon = scrapy.Field()         #(28)经度
    xiaoqu_name = scrapy.Field()        #(29)小区名
    city_ln = scrapy.Field()            #(30)城市代码
    borough_ln = scrapy.Field()         #(31)区县代码
    street_ln = scrapy.Field()          #(32)街道代码
