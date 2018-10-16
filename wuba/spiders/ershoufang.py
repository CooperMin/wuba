# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


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
            # 'Cookie': 'f=n; commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; userid360_xml=726A92634D7A7D35CAD7CA8F4E07D275; time_create=1542266421957; id58=c5/njVvASOW4H5VdAx9hAg==; 58tj_uuid=201f13b0-3c75-4368-8b5b-dd9cb2804f5a; new_uv=4; wmda_uuid=81cbba759cb249e8999e6e0cbb0879f4; wmda_new_uuid=1; wmda_visited_projects=%3B6333604277682%3B1732039838209; als=0; xxzl_deviceid=dpBoZISfMhLCL4GQXYIk9%2FksGoO60%2Bs6V5bMmhUkq2rF%2BOOxP%2BCUXOK1u73OAVgr; city=sh; XQH=%7B%22w%22%3A%5B%7B%22id%22%3A%222241971%22%2C%22t%22%3A1539338904928%7D%5D%7D; Hm_lvt_ae019ebe194212c4486d09f377276a77=1539338905; __utma=253535702.265205006.1539338907.1539338907.1539338907.1; __utmz=253535702.1539338907.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ppStore_fingerprint=961E4D56CA27D69289344FF6CF33BB968B8A63DF43B5FEA2%EF%BC%BF1539339022669; cookieuid1=mgjwFVvFjtNxd3hXAwX8Ag==; wmda_session_id_1732039838209=1539673794529-cb1a6144-7b19-5288; new_session=0; qz_gdt=; utm_source=; spm=; init_refer=; hasLaunchPage=%7Cd_car_ershouche_35622739630649%7C; launchFlag=1; gr_user_id=c437c82f-11ba-496f-a317-ed001fd07b05; gr_session_id_bb4f3b01548ff31c=8aa3348f-18b8-428b-9cc9-7997d024b544; gr_session_id_bb4f3b01548ff31c_8aa3348f-18b8-428b-9cc9-7997d024b544=true; 58home=sh; f=n; JSESSIONID=5B0D1D5B7B9BBE85155BD723C65A7981; wmda_session_id_6333604277682=1539674420069-d6944c6e-123c-a514; xzfzqtoken=CGz4izHvTFNcfXTqR71sIe0C%2FTCix1eMWMtpKASM6XucUKH%2FYotZ4C7BFGBbFchKin35brBb%2F%2FeSODvMgkQULA%3D%3D',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': 1

        }
        start_url = 'https://sh.58.com/ershoufang/0/?PGTID=0d30000c-0000-2f8f-3fe6-946742aaab68&ClickID=1'
        yield Request(start_url,callback=self.countPage,headers=hds)

    def countPage(self,response):
        countPage = int(response.xpath('//div[@class="pager"]/a[@class="next"]/preceding-sibling::[-1]/text()').extaract()[0])
        for pn in range(1,countPage+1):
            pageUrl = f'https://sh.58.com/ershoufang/pn{pn}/?PGTID=0d30000c-024f-0f3f-3dc9-0896cc812167&ClickID=1'
            urlList = response.xpath('//ul[@class="house-list-wrap"]/li').extract()
            for url in urlList:
                url = url.xpath('//div[@class="list-info"]/h2/title/a/@href').extract()[0]
                if 'ershoufang' in url:
                    address = url.xpath('string(//div[@class="list-info"]/p[2])').extract()[0]
                    hdd = {
                        'Host': 'sh.58.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        # 'Cookie': 'f=n; commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; userid360_xml=726A92634D7A7D35CAD7CA8F4E07D275; time_create=1542266421957; id58=c5/njVvASOW4H5VdAx9hAg==; 58tj_uuid=201f13b0-3c75-4368-8b5b-dd9cb2804f5a; new_uv=4; wmda_uuid=81cbba759cb249e8999e6e0cbb0879f4; wmda_new_uuid=1; wmda_visited_projects=%3B6333604277682%3B1732039838209; als=0; xxzl_deviceid=dpBoZISfMhLCL4GQXYIk9%2FksGoO60%2Bs6V5bMmhUkq2rF%2BOOxP%2BCUXOK1u73OAVgr; city=sh; XQH=%7B%22w%22%3A%5B%7B%22id%22%3A%222241971%22%2C%22t%22%3A1539338904928%7D%5D%7D; Hm_lvt_ae019ebe194212c4486d09f377276a77=1539338905; __utma=253535702.265205006.1539338907.1539338907.1539338907.1; __utmz=253535702.1539338907.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ppStore_fingerprint=961E4D56CA27D69289344FF6CF33BB968B8A63DF43B5FEA2%EF%BC%BF1539339022669; cookieuid1=mgjwFVvFjtNxd3hXAwX8Ag==; wmda_session_id_1732039838209=1539673794529-cb1a6144-7b19-5288; new_session=0; qz_gdt=; utm_source=; spm=; init_refer=; hasLaunchPage=%7Cd_car_ershouche_35622739630649%7C; launchFlag=1; gr_user_id=c437c82f-11ba-496f-a317-ed001fd07b05; gr_session_id_bb4f3b01548ff31c=8aa3348f-18b8-428b-9cc9-7997d024b544; gr_session_id_bb4f3b01548ff31c_8aa3348f-18b8-428b-9cc9-7997d024b544=true; 58home=sh; f=n; JSESSIONID=5B0D1D5B7B9BBE85155BD723C65A7981; wmda_session_id_6333604277682=1539674420069-d6944c6e-123c-a514; xzfzqtoken=CGz4izHvTFNcfXTqR71sIe0C%2FTCix1eMWMtpKASM6XucUKH%2FYotZ4C7BFGBbFchKin35brBb%2F%2FeSODvMgkQULA%3D%3D',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': 1
                    }
                    url = url
                    yield Request(url)
                else:
                    pass


        # nextPage = response.xpath('//div[@class="pager"]/a[@class="next"]/text()').extract()[0]
        # if nextPage == '下一页':
        #     link = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract()[0]
        #     page = 'https://sh.58.com' + link

        else:
            pass


    def parse(self, response):
        pass
