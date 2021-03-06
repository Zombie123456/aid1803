# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'tencent'
    # 这里用来防止抓取数据时跳转到其他域名的网站
    allowed_domains = ['hr.tencent.com']
    
    # seed url种子URL
    start_urls = ['https://hr.tencent.com/position.php?keywords=python']

    # 每次获取response响应时会调用这个方法，
    #需要在这个地方精确的匹配信息
    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentspiderItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            yield item #返回给pipelines process_item
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
