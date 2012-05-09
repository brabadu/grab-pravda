# -*- coding: utf-8 -*-
import datetime

from spiders.base import BaseHubSpider
from grab.spider import Task
from grab.error import DataNotFound

from .models import Post


class PravdaArchiveSpider(BaseHubSpider):
    # initial_urls = ['http://www.pravda.com.ua/rus/archives']
    base_url = 'http://www.pravda.com.ua/'

    def task_initial(self, grab, task):
        grab_date = datetime.date.today() - datetime.timedelta(1)

        for i in xrange(30):
            yield Task('archive_day', url='/rus/archives/date_{0}/'.format(grab_date.strftime('%d%m%Y')))
            grab_date -= datetime.timedelta(1)
            self.items_total += 1

        print '=' * 20, 'Last day processed', grab_date + datetime.timedelta(1)

    def task_archive_day(self, grab, task):
        dd = grab.xpath_list('//dl[@class="news4"]/dd')[0]
        header_css_classes = dd.attrib.get('class', '').split(' ')
        first_url = dd.find('a').get('href')
        yield Task('news', url=first_url, header_css_classes=header_css_classes)

    def task_news(self, grab, task):
        title = grab.xpath_text('//h1[@class="title"]')
        print title

        content = grab.xpath_text('//div[@class="text"]')
        print content

        url = task.url
        print url

        tags = grab.xpath_list('//div[@class="text"]/p[@class="tags"]/a')
        print ", ".join([t.text_content() for t in tags])

        published_date = grab.xpath_text('//span[@class="dt2"]')
        print published_date

        header_css_classes = task.get('header_css_classes')
        title_red = 'flash' in header_css_classes
        print 'Red title:', title_red

        title_bold = 'hl' in header_css_classes
        print 'Bold title:', title_bold

        title_uppercased = title.isupper()
        print 'Upper title:', title_uppercased

        try:
            comments_number = int(grab.xpath_text('//div[@class="rpad"]/a[@class="but5"]'))
        except (ValueError):
            comments_number = None
        print "Comments:", comments_number

        has_photo = None
        print 'Has photo:', has_photo

        try:
            has_video = bool(grab.xpath_text(grab.xpath_text('//div[@class="rpad"]/span[@class="stext"]/b')))
        except (DataNotFound):
            has_video = None
        print 'Has video:', has_video

        Post.objects.create(
            title=title,
            content=content,
            url=url,
            tags=tags,
            published_date_str=published_date,
            title_red=title_red,
            title_bold=title_bold,
            title_uppercased=title_uppercased,
            has_video=has_video,
            comments_number=comments_number,
        )
        print '=' * 20, 'Items total', self.items_total
        grab.sleep(2, 10)