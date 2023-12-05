from scrapy.crawler import CrawlerProcess
from scrapy_spider import ConcordiaSpider
import os

def start_crawling(start_url, max_urls, depth_limit, html_dir='./html'):
    if os.path.exists(html_dir):
        if os.listdir(html_dir):  # Check if /html directory is not empty
            print("/html directory is not empty. Skipping crawling step.")
            return

    # Create the directory if it doesn't exist
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    # Run the spider
    process = CrawlerProcess({
        'DEPTH_LIMIT': depth_limit,  
        'CLOSESPIDER_PAGECOUNT': max_urls,
        'ROBOTSTXT_OBEY': True,
        'LOG_LEVEL': 'CRITICAL',
    })
    process.crawl(ConcordiaSpider, start_urls=[start_url], allowed_domains=["concordia.ca"])
    process.start()