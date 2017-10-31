#!/usr/bin/env python3.5
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name='shiyanlou-courses'
    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.xpath('//li[@itemprop="owns"]'):
            yield{
                'name':course.xpath('.//div/h3/a/text()').re_first('\n        (.+)'),
                'update_time':course.xpath('.//div/relative-time/@datetime').extract_first()
            }
