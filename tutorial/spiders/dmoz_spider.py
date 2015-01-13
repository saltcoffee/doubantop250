import scrapy
from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    url_list = []
    for i in xrange(0, 10):
        url_list.append("http://movie.douban.com/top250?start=" + str(i*25) + "&filter=&type=")
    allowed_domains = ["douban.com"]
    start_urls = url_list
    def parse(self, response):
        item = TutorialItem()
        item['title'] = []
        item['link'] = []
        item['rank'] = []
        for sel in response.xpath('//ol/li'):
            #item = TutorialItem()
            item['title'].append(sel.xpath('.//img/@alt').extract()[0])
            item['link'].append(sel.xpath('.//a[@class]/@href').extract()[0])
            item['rank'].append(sel.xpath('.//em[@class]/text()').extract()[0])
        return item
        #self.decode_list(title)
        #self.decode_list(link)
        #self.decode_list(rank)


    def decode_list(self, list):
        for item in list:
            print item
