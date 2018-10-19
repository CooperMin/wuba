# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
import time

class WubaPipeline(object):
    def __init__(self):
        host = settings['MS_HS']
        port = settings['MS_PR']
        db = settings['MS_DB']
        user = settings['MS_US']
        passwd = settings['MS_PD']
        self.client = pymysql.connect(
            host = host,
            port = port,
            db = db,
            user = user,
            passwd = passwd
        )
        self.cursor = self.client.cursor()

    def process_item(self, item, spider):
        insInfo = """
            insert into wbInfo (city,borough,street,username,tel,price,realsize,area,towards,realEstateE,
                                bankcard,realName,weixin,zhima,zhimaFen,writeTime,huxingshi,huxingwei,huxingting,jushishuru,
                                HireType,MinPrice,userid,title,xiaoqu_lon,xiaoqu_lat,xiaoqu_name,city_ln,borough_ln,street_ln,
                                pageUrl)
            VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
                    "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
                    "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
                    "{}")
                """.format(item['city'],item['borough'],item['street'],item['username'],item['tel'],item['price'],item['realsize'],item['area'],item['towards'],item['realEstateE'],
                           item['bankcard'],item['realName'],item['weixin'],item['zhima'],item['zhimaFen'],item['writeTime'],item['huxingshi'],item['huxingwei'],item['huxingting'],item['jushishuru'],
                           item['HireType'],item['MinPrice'],item['userid'],item['title'],item['xiaoqu_lon'],item['xiaoqu_lat'],item['xiaoqu_name'],item['city_ln'],item['borough_ln'],item['street_ln'],
                           item['pageUrl'])
        insbase = """
                insert into wbbase(userid,username,tel,bankcard,realName,weixin,zhima,zhimaFen)
                values ("{}","{}","{}","{}","{}","{}","{}","{}")
                """.format(item['userid'],item['username'],item['tel'],item['bankcard'],item['realName'],item['weixin'],item['zhima'],item['zhimaFen'])
        inshx = """
                insert into wbhuxing (city,borough,street,username,tel,price,realsize,area,towards,realEstateE,
                                      huxingshi,huxingwei,huxingting,jushishuru,HireType,MinPrice,userid,title,xiaoqu_lon,xiaoqu_lat,
                                      xiaoqu_name,pageUrl,writeTime)
                values ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
                        "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",
                        "{}","{}","{}")
                """.format(item['city'],item['borough'],item['street'],item['username'],item['tel'],item['price'],item['realsize'],item['area'],item['towards'],item['realEstateE'],
                           item['huxingshi'],item['huxingwei'],item['huxingting'],item['jushishuru'],item['HireType'],item['MinPrice'],item['userid'],item['title'],item['xiaoqu_lon'],item['xiaoqu_lat'],
                           item['xiaoqu_name'],item['pageUrl'],item['writeTime'])
        insadd = """
                insert into wbadd (city,borough,street,city_ln,borough_ln,street_ln)
                values ("{}","{}","{}","{}","{}","{}")
                """.format(item['city'],item['borough'],item['street'],item['city_ln'],item['borough_ln'],item['street_ln'])
        try:
            self.cursor.execute(insInfo)
            self.client.commit()
            localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'表【wbInfo】数据插入成功！(当前时间：{localTime})')
        except Exception as e:
            self.client.rollback()
            print('\n\033[1;31m{0} Warning：表【wbInfo】数据插入失败！ {0}\033[0m'.format(23 * '+'))
            print('\033[1;31m{1}{0}{1} \033[0m'.format(e, 6 * '+'))
            print('\033[1;31m{0}\033[0m\n'.format(65 * '+'))
        try:
            self.cursor.execute(insbase)
            self.client.commit()
            localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'表【wbbase】数据插入成功！(当前时间：{localTime})')
        except Exception as e:
            self.client.rollback()
            print('\n\033[1;31m{0} Warning：表【wbbase】数据插入失败！ {0}\033[0m'.format(23 * '+'))
            print('\033[1;31m{1}{0}{1} \033[0m'.format(e, 6 * '+'))
            print('\033[1;31m{0}\033[0m\n'.format(65 * '+'))
        try:
            self.cursor.execute(inshx)
            self.client.commit()
            localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'表【wbhuxing】数据插入成功！(当前时间：{localTime})')
        except Exception as e:
            self.client.rollback()
            print('\n\033[1;31m{0} Warning：表【wbhuxing】数据插入失败！ {0}\033[0m'.format(23 * '+'))
            print('\033[1;31m{1}{0}{1} \033[0m'.format(e, 6 * '+'))
            print('\033[1;31m{0}\033[0m\n'.format(65 * '+'))
        try:
            self.cursor.execute(insadd)
            self.client.commit()
            localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f'表【wbadd】数据插入成功！(当前时间：{localTime})')
        except Exception as e:
            self.client.rollback()
            print('\n\033[1;31m{0} Warning：表【wbadd】数据插入失败！ {0}\033[0m'.format(23 * '+'))
            print('\033[1;31m{1}{0}{1} \033[0m'.format(e, 6 * '+'))
            print('\033[1;31m{0}\033[0m\n'.format(65 * '+'))


    def connect_close(self,spider):
        self.client.close()
