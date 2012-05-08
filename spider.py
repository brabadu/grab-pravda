# -*- coding: utf-8 -*-
"""
Pravda news articles spy
"""

from grab.tools.logs import default_logging

from spiders.pravda_archive import PravdaArchiveSpider
from config import default_spider_params


if __name__ == '__main__':
    default_logging()

    print "Scape python projects"
    bot = PravdaArchiveSpider(**default_spider_params())

    bot.setup_grab(timeout=4096, connect_timeout=10)
    bot.run()
    print bot.render_stats()
