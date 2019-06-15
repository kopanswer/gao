# --*-- coding:utf8 --*--
"""
包的排序：
    系统包     without pip install
    自定义包
    第三方包
    每个模块按照 A-Z升序排序
"""
import random
import re
import threading
import time
import settings
from util import fetch_util

class HandlerProcess(object):
    def __init__(self):
        pass

    def fetch_bit_names(self, topn = 1000):
        html = fetch_util.fetch_html(settings.base_url)
        # slugs = eval(html)
        # print slugs[0]["slug"]
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
            trs = dom.xpath('.//table[@class="table"]/tbody//tr[@class="text-right"]')
            if len(trs) < 1:
                retry_insec = random.randint(1,15)
                print "[tip] url: %s, fetch trs len(%d), retry after %s s" % (
                    his_url,
                    len(trs),
                    retry_insec
                )
                time.sleep(retry_insec)
            continue
        return trs

    def fetch_bit_history(self, name, start, end):
        # print "name: %s start: %s end: %s" % (name, start, end)
        hist_url = settings.history_url.format(coin=name, start=start, end=end)
        # print hist_url
        # html = fetch_util.fetch_html(hist_url)
        # dom = fetch_util.get_dom(html)          #   分层：第三方包只在专门的层里面调用：from lxml import etree
        trs = self.fetch_trs(hist_url)     #   xpath 结构
        # print "trs length: %s" % len(trs)
        print "name:%s date:%s trs:%s" % (name, start, end)
        for tr in trs:
            #   原始数据抓取
            date = tr.xpath('.//td')[0].text
            close = tr.xpath('.//td')[-3].xpath('@data-format-value')[0]
            volume = tr.xpath('.//td')[-2].xpath('@data-format-value')[0]
            market_cap = tr.xpath('.//td')[-1].xpath('@data-format-value')[0]
            #   数据预处理/清洗
            data = self.data_preprocess([name, date, close, volume, market_cap])
            self.save(data)

    def save(self, data):
        #   date, name, close, volume, market_cap
        # print data
        pass

    def process(self):
        # self.fetch_bit_names()
        names = self.fetch_bit_names(topn=1000)
        for coin in names:
            threading.Thread(target=self.fetch_bit_history, args=(coin, "20190101", "20190615", )).start()
        # self.fetch_bit_history(name="bitcoin", start="20130101", end="20190614")

handler_process = HandlerProcess()