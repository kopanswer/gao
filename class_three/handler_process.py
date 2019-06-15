# -*- coding:utf8 -*-
# 包的排序
# 1 系统包
# 2 自己写的包
# 3 第三方包
# 4 每个模块按照a-z升序

import re
import random
import threading
import time

import settings
from util import fetch_util


class HandlerProcess(object):
    def __init__(self):
        pass

    def fetch_bit_names(self, topn=1000):
        html = fetch_util.fetch_html(settings.base_url)
        bit_names = re.compile('"slug": "(.*?)"', re.S).findall(html)
        return bit_names[:topn]

    def data_preprocess(self, data):
        name, date, close, volume, market_cap = data
        date = fetch_util.parse_date(origin_date=date)
        close = "%.4f" % float(fetch_util.deal_missing_value(close))
        volume = "%.4f" % float(fetch_util.deal_missing_value(volume))
        market_cap = "%.4f" % float(fetch_util.deal_missing_value(market_cap))
        return name, date, close, volume, market_cap

    def fetch_trs(self, his_url):
        while True:
            html = fetch_util.fetch_html(his_url)
            dom = fetch_util.get_dom(html)
            if not dom:
                continue
            trs = dom.xpath('.//table[@class="table"]/tbody//tr')
            if len(trs) < 1:
                retry_insec = random.randint(1, 15)
                print "[tip] url:%s, fetch trs len(%d), retry after %s s" % (
                    his_url,
                    len(trs),
                    retry_insec
                )
                time.sleep(retry_insec)
                continue
            return trs

    def fetch_bit_history(self, name, start, end):
        # print "name:%s start:%s end:%s" % (name, start, end)
        his_url = settings.history_url.format(coin=name, start=start, end=end)
        trs = self.fetch_trs(his_url)
        print "name:%s date:%s trs:%s" % (name, start, len(trs))
        for tr in trs:
            # 1. 原始数据抓取
            date = tr.xpath('.//td')[0].text
            close = tr.xpath('.//td')[-3].xpath('@data-format-value')[0]
            volume = tr.xpath('.//td')[-2].xpath('@data-format-value')[0]
            market_cap = tr.xpath('.//td')[-1].xpath('@data-format-value')[0]

            # 2. 数据预处理/清洗
            data = self.data_preprocess([name, date, close, volume, market_cap])

            # 3. 数据存储
            self.save(data)

    def save(self, data):
        # name, date, close, volume, market_cap
        # print data
        pass

    def process(self):
        names = self.fetch_bit_names(topn=100)
        for coin in names:
            self.fetch_bit_history(coin, "20190101", "20190615")
            # threading.Thread(target=self.fetch_bit_history,
            #                  args=(coin, "20190101", "20190615",)).start()


handler_process = HandlerProcess()
