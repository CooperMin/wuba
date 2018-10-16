# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['https://sh.58.com']
    start_urls = ['http://https://sh.58.com/']


    def start_requests(self):
        hds = {
            
        }
        start_url = 'https://sh.58.com/ershoufang/0/?PGTID=0d30000c-0000-2329-d1f4-e3ba4743859f&ClickID=1'
        yield Request()

    def nextPage(self,response):


    def parse(self, response):
        pass
