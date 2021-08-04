# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteWebScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    tag = scrapy.Field()
    desc = scrapy.Field()
    author = scrapy.Field() 


    
