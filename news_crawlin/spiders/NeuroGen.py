from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news_crawlin.utils import create_csv
from datetime import date


class NeuroSpider(CrawlSpider):
    name = 'neuro'
    allowed_domains = ['www.neurogenbd.com']
    start_urls = [
        'http://www.neurogenbd.com/health-blog/?fbclid=IwAR004cK0Ys6yWBHXTniPo5Jy_j4cfoItkVwb5815jwPp50M5DPv7aGjFPQw',
        'http://www.neurogenbd.com/health-blog/page/2/?fbclid=IwAR004cK0Ys6yWBHXTniPo5Jy_j4cfoItkVwb5815jwPp50M5DPv7aGjFPQw'
    ]

    rules = (
        Rule(LinkExtractor(allow='/20[0-9][0-9]/[0-9][0-9]/[0-9][0-9]'), callback='parse_item', follow=False),
    )

    id = -1

    def parse_item(self, response):
        self.id += 1
        title = response.xpath("//div[@class='w-blog-post-body']/h1/text()").getall()[0]
        content = response.xpath("//div[@class='l-section-h i-cf']/p/text()").getall()
        url = response.url
        published_date = response.xpath("//div[@class='w-blog-post-meta']/time/text()").getall()
        scraped_date = str(date.today())
        domain = 'www.neurogenbd.com'

        for con in content[:-3]:
            res = [self.id, title, con, url, published_date, scraped_date, domain]
            create_csv(res)
            self.id += 1

        yield {}
