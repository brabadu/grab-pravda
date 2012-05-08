# -*- coding: utf-8 -*-
import datetime

from spiders.base import BaseHubSpider
from grab.spider import Task


class PravdaArchiveSpider(BaseHubSpider):
    # initial_urls = ['http://www.pravda.com.ua/rus/archives']
    base_url = 'http://www.pravda.com.ua/rus/archives'

    def task_initial(self, grab, task):
        grab_date = datetime.date.today() - datetime.timedelta(1)

        while self.items_total < 1000:
            yield Task('archive_day', url='/date_{0}/'.format(grab_date.strftime('%d%m%Y')))
            grab_date -= datetime.timedelta(1)
            self.items_total += 501

    def task_archive_day(self, grab, task):
        print '\n'.join(el.get('href') for el in grab.xpath_list('//dd/a'))
