from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from lesson7.shopparser import settings
from lesson7.shopparser.spiders.leroymerlinru import LeroymerlinruSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinruSpider)

    process.start()
