# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):

    # def __init__(self, server, port):
    #     pass

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.settings['MONGO_SERVER'],
    #                crawler.settings['MONGO_PORT'])

    def process_item(self, item, spider):
        return item
