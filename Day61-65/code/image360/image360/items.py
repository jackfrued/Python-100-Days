# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):

    price = scrapy.Field()
    deal = scrapy.Field()
    title = scrapy.Field()


class BeautyItem(scrapy.Item):

    title = scrapy.Field()
    tag = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    url = scrapy.Field()
