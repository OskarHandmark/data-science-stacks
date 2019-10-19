# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name            = 'myspider'
    allowed_domains = ['w3schools.com']
    start_urls      = ['https://www.w3schools.com/']

    def parse(self, response):
        yield {
            'val': 1
        }

