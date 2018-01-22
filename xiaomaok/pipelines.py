# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaomaokPipeline(object):
    def process_item(self, item, spider):
        with open('txt\\1323.txt', 'a') as code:
            code.write('￥'.join([item['title'], item['replies'], item['looks'], item['date']])+'\n')

        
