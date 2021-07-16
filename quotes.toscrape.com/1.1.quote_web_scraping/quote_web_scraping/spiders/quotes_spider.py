import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['example.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        all_quotes = response.css('div.quote')[0]  
        
        # retrive 1st quotes title , author and tag details 

        desc = all_quotes.css('span.text::text').extract()
        author = all_quotes.css('.author::text').extract()
        tag = all_quotes.css('div.tags a::text').extract() 
         

        yield{
            '--->> desc': desc,
            'author': author,
            'tag': tag,
        }
 