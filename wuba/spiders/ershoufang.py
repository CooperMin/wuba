# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import re
import time
from wuba.items import WubaItem


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['https://sh.58.com']
    start_urls = ['http://https://sh.58.com/']


    def start_requests(self):
        hds = {
            'Host': 'sh.58.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': 1

        }
        start_url = 'https://sh.58.com/ershoufang/0/?PGTID=0d30000c-0000-2f8f-3fe6-946742aaab68&ClickID=1'
        yield Request(url=start_url,callback=self.countPage,headers=hds,dont_filter=True)

    def countPage(self,response):
        countPage = int(response.xpath('//div[@class="pager"]/a[@class="next"]/preceding-sibling::a[1]/span/text()').extract()[0])
        # countPage = 1 #测试代码，正式爬取请注释掉
        for pn in range(1,countPage+1):
            if pn == 1:
                pageUrl = 'https://sh.58.com/ershoufang/0/?PGTID=0d30000c-0000-2f8f-3fe6-946742aaab68&ClickID=1'
                referer = 'Referer: https://sh.58.com/ershoufang/?PGTID=0d200001-0000-2308-0e03-36c5cefc6be3&ClickID=1'
            else:
                pageUrl = f'https://sh.58.com/ershoufang/pn{pn}/?PGTID=0d30000c-0000-2961-e285-4f874c6a41e0&ClickID=1'
                referer = f'https://sh.58.com/ershoufang/pn{pn-1}/?PGTID=0d30000c-0000-2961-e285-4f874c6a41e0&ClickID=1'
            hdl = {
                'Host': 'sh.58.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': 1,
                'Referer': referer
            }
            yield Request(url=pageUrl, callback=self.getLink, headers=hdl,meta={'pn':pn,'pageUrl':pageUrl,'countPage':countPage},dont_filter=True)

    def getLink(self,response):
        print(response.status)
        pn = response.meta['pn']
        countPage = response.meta['countPage']
        pageUrl = response.meta['pageUrl']
        urlList = response.xpath('//ul[@class="house-list-wrap"]/li')
        for info in urlList:
            url = info.xpath('div[@class="list-info"]/h2[@class="title"]/a/@href').extract()[0]
            if 'ershoufang' in url:
                hdd = {
                    'Host': 'sh.58.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': 1,
                    'Referer': pageUrl
                }
                url = url
                print(f'页码：{pn}，链接：{url}')
                yield Request(url=url,callback=self.parse,headers=hdd,meta={'countPage':countPage,'pn':pn},dont_filter=True)
            else:
                pass


        # nextPage = response.xpath('//div[@class="pager"]/a[@class="next"]/text()').extract()[0]
        # if nextPage == '下一页':
        #     link = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract()[0]
        #     page = 'https://sh.58.com' + link

    def parse(self, response):
        item = WubaItem()
        status = response.status
        item['pageUrl'] = response.url
        countPage = response.meta['countPage']
        pn = response.meta['pn']
        print(f"状态码：{status},网址：{item['pageUrl']},共计{countPage}页，当前第{pn}页")
        jsonInfo = re.findall(r'(?<=____json4fe = )(.*)(?=;)',response.text)[1]
        item['city'] = json.loads(jsonInfo)['locallist'][0]['name']
        item['city_ln'] = json.loads(jsonInfo)['locallist'][0]['listname']
        item['borough'] = json.loads(jsonInfo)['locallist'][1]['name']
        item['borough_ln'] = json.loads(jsonInfo)['locallist'][1]['listname']
        if len(json.loads(jsonInfo)['locallist']) >= 3:
            item['street'] = json.loads(jsonInfo)['locallist'][2]['name']
            item['street_ln'] = json.loads(jsonInfo)['locallist'][2]['listname']
        else:
            item['street'] = ''
            item['street_ln'] = ''
        item['username'] = json.loads(jsonInfo)['personal']['userName']
        item['tel'] = int(response.xpath('//p[@class="phone-num"]/text()').extract()[0].replace(' ','').strip())
        # pubTime = str(json.loads(jsonInfo)['_trackParams'][17]['V'])
        # item['pubTime'] = '{0}-{1}-{2} {3}:{4}:{5}'.format(pubTime[0:4], pubTime[4:6], pubTime[6:8], pubTime[8:10],pubTime[10:12], pubTime[12:14])
        if '产权年限' in response.text:
            item['realEstateE'] = response.xpath('//span[contains(text(),"产权年限")]/following-sibling::span/text()').extract()[0]
        else:
            item['realEstateE'] = ''
        # if '建筑年代' in response.text:
        #     item['buildYear'] = response.xpath('//span[contains(text(),"建筑年代")]/following-sibling::span/text()').extract()[0]
        # else:
        #     item['buildYear'] = ''
        item['bankcard'] = json.loads(jsonInfo)['personal']['authentication']['bankCard']
        item['realName'] = json.loads(jsonInfo)['personal']['authentication']['realName']
        item['weixin'] = json.loads(jsonInfo)['personal']['authentication']['weixin']
        item['zhima'] = json.loads(jsonInfo)['personal']['authentication']['zhima']
        item['zhimaFen'] = json.loads(jsonInfo)['personal']['authentication']['zhimaFen']
        start = json.loads(jsonInfo)['start']/1000
        item['writeTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start))
        supplycount = json.loads(jsonInfo)['supplycount'].replace("'",'"')
        item['huxingshi'] = json.loads(supplycount)['paramdata']['huxingshi']
        item['huxingwei'] = json.loads(supplycount)['paramdata']['huxingwei']
        item['huxingting'] = json.loads(supplycount)['paramdata']['huxingting']
        item['jushishuru'] = json.loads(supplycount)['paramdata']['jushishuru']
        item['HireType'] = json.loads(supplycount)['paramdata']['HireType']#租用类型
        item['MinPrice'] = json.loads(supplycount)['paramdata']['MinPrice']
        item['userid'] = json.loads(jsonInfo)['userid']
        item['price'] = json.loads(jsonInfo)['webim']['price']
        item['title'] = json.loads(jsonInfo)['webim']['title']
        item['realsize'] = json.loads(jsonInfo)['webim']['labels'][0]
        item['area'] = json.loads(jsonInfo)['webim']['labels'][1]
        item['towards'] = json.loads(jsonInfo)['webim']['labels'][2]#朝向
        item['xiaoqu_lat'] = json.loads(jsonInfo)['xiaoqu']['baidulat']
        item['xiaoqu_lon'] = json.loads(jsonInfo)['xiaoqu']['baidulon']
        item['xiaoqu_name'] = json.loads(jsonInfo)['xiaoqu']['name']
        # lat = json.loads(jsonInfo)['xiaoqu']['lat']
        # lon = json.loads(jsonInfo)['xiaoqu']['lon']
        yield item

