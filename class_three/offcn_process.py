# -*- coding:utf8 -*-

import re
import random
import threading
import time

import settings
from util import fetch_util


class OffcnProcess(object):
    def __init__(self):
        pass

    def get_trs(self, url):
        dom = fetch_util.get_dom(fetch_util.fetch_html(url))
        table = dom.xpath('.//table')[0]
        trs = table.xpath('.//tr')
        return trs

    def get_pretty_data(self, trs):
        result = []
        for tr in trs:
            zhaokao_count = tr.xpath('.//td')[-5].text
            baokao_count = tr.xpath('.//td')[-5].text
            result.append((zhaokao_count, baokao_count))
        return result

    def save(self, data):
        # [(c1, c1), ....]
        for item in data:
            pass

    def process(self):
        for i in range(settings.offcn_max_pages):
            url = settings.offcn_base_url.format(page=i + 1)
            trs = self.get_trs(url)
            print "current page:%d, fetch count:%d" % (i+1, len(trs))
            if len(trs) < 3:
                print "max_page is %d, end!" % (i + 1)
                return
            data = self.get_pretty_data(trs[1:])
            self.save(data)


offcn_process = OffcnProcess()