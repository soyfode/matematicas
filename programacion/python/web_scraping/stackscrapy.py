from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
 
# Stack Overflow Questions
class StackOverflowQuestion(Item):
    title = Field()
    id = Field()
 
class StackOverflowSpider(Spider):
    name = 'stackoverflow'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }
    start_urls = ['https://stackoverflow.com/questions/']
 
    def parse(self, response):
        questions_container = Selector(response)
        questions = questions_container.xpath('//*[@id="question-summary-74296267"]/div[2]')
        id = 0
        for question in questions:
 
            item = ItemLoader(StackOverflowQuestion(), question)
            item.add_xpath('title', './/h3/a/text()')
 
            item.add_value('id',id)
            id += 1
 
            yield item.load_item()
