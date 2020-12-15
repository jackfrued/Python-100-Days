# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from pymongo import MongoClient
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


logger = logging.getLogger('SaveImagePipeline')


class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(url=item['url'])

    def item_completed(self, results, item, info):
        logger.debug('图片下载完成!')
        if not results[0][0]:
            raise DropItem('下载失败')
        return item

    def file_path(self, request, response=None, info=None):
        return request.url.split('/')[-1]


class SaveToMongoPipeline(object):

    def __init__(self, mongo_url, db_name):
        self.mongo_url = mongo_url
        self.db_name = db_name
        self.client = None
        self.db = None

    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('MONGO_URL'),
                   crawler.settings.get('MONGO_DB'))

