import scrapy
from scrapy_anime_data.items import Rank

class AnimeDataSpider(scrapy.Spider):
    name = "anime_data"
    start_urls = ["https://myanimelist.net/topanime.php?type=bypopularity"]

    def parse(self, response):
        animes = response.xpath("//tr[@class='ranking-list']")

        for anime in animes:
            rank = Rank()
            rank['position'] = anime.xpath('td[1]//span//text()').extract_first()
            rank['name'] = anime.xpath('td[2]//div[@class="di-ib clearfix"]//a//text()').extract_first()
            rank['score'] = anime.xpath('td[3]//div[@class="js-top-ranking-score-col di-ib al"]//span//text()').extract_first()
            yield rank
