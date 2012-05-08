# -*- coding: utf-8 -*-
from grab.spider import Spider


class BaseHubSpider(Spider):
    initial_urls = ['http://www.pravda.com.ua/']

    items_total = 0

    def log_progress(self, str):
        self.items_total += 1
        print "(%d) Item scraped: %s" % (self.items_total, str)
