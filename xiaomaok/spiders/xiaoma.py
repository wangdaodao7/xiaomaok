# -*- coding: utf-8 -*-
import scrapy
from xiaomaok.items import XiaomaokItem
from scrapy.http import Request


class XiaomaSpider(scrapy.Spider):
    name = 'xiaoma'
    allowed_domains = ['wwww.masok.cn']
    base_url = 'http://www.masok.cn/forum.php?mod=forumdisplay&fid=108&filter=author&orderby=dateline&page='

    #集合法写需要爬的网址
    # start_urls = ['http://www.masok.cn/forum.php?mod=forumdisplay&fid=108&filter=author&orderby=dateline&page={}'.format(str(x)) for x in range(1, 130)]

    #多个网址的爬取函数
    def start_requests(self):
        for x in range(1, 12):
            url = self.base_url + '{}'.format(str(x))
            yield Request(url, self.parse)
       
            

    def parse(self, response):
        tiezi = response.xpath('//*[@*]/tr')

        item = XiaomaokItem()
        for t in tiezi[4:]:
            #extract为提取文本为list的函数，scrapy必须要用的
            item['title'] = t.xpath('./th/a/text()').extract()[0]
            item['looks'] = t.xpath('./td/em/text()').extract()[0]
            item['date'] = t.xpath('./td/em/span/text()').extract()[0]
            item['replies'] = t.xpath('./td/a/text()').extract()[2]
            # print(item)
            yield item
        

