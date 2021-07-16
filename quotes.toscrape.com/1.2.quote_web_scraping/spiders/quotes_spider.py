import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['example.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        all_quotes = response.css('div.quote')  
        # retrive all quotes title , author and tag details 
        # note it retrive 1st page all data only 

        for quotes in all_quotes:

            desc = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('div.tags a::text').extract() 
         

            yield{
                '--->> desc': desc,
                'author': author,
                'tag': tag,
            }
 