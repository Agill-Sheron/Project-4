import scrapy
import os

class ConcordiaSpider(scrapy.Spider):
    name = "concordia_spider"
    allowed_domains = ["concordia.ca"]
    start_urls = ["https://www.concordia.ca/"]

    def parse(self, response):
        page_url = response.url
        page_content = response.text
        html_dir = './html'

        # Create directory if it doesn't exist
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)

        # Save the page
        filename = page_url.split('/')[-1] or 'index'
        with open(f'{html_dir}/{filename}.html', 'w', encoding='utf-8') as f:
            f.write(page_content)

        # Extract and follow links
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)
