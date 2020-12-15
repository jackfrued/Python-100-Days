# -*- coding: utf-8 -*-
import scrapy

from douban.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            item = MovieItem()
            item['title'] = li.xpath('div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['score'] = li.xpath('div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['motto'] = li.xpath('div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield item
        href_list = response.css('a[href]::attr("href")').re('\?start=.*')
        for href in href_list:
            url = response.urljoin(href)
            yield scrapy.Request(url=url, callback=self.parse)
