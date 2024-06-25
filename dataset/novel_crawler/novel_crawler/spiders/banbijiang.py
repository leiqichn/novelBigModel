import scrapy


class BanbijiangSpider(scrapy.Spider):
    name = "banbijiang"
    allowed_domains = ["read.banbijiang.com"]
    start_urls = ["http://read.banbijiang.com/xiaoshuo"]

    def parse(self, response):
        self.logger.info("Visited %s", response.url)
        field_list = response.xpath('//dl[@class="tbox"]')
        for field in field_list:
            link = field.xpath('.//a/@href').extract_first()
            print(link)
            
        
