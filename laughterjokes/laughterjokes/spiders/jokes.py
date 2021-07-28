import scrapy
from ..items import LaughterjokesItem

class JokesSpider(scrapy.Spider):
    name = 'jokes'
    allowed_domains = ['www.laughfactory.com/jokes/family-jokes']
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes/']

    def parse(self, response):
        items = LaughterjokesItem()
        all_jokes = response.css("div.jokes")

        for joke in all_jokes:
            title = joke.css("div.joke-text p::text").extract() 
            like = joke.css("div.likes-dislikes-count a.like span::text").extract()
            dislike=joke.css("div.likes-dislikes-count a.dislike span::text").extract()

            items['title']= title
            items['like'] = like
            items['dislike'] =dislike

            yield items

