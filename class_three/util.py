# --*-- coding:utf8 --*--
import time
import settings
import requests
from lxml import etree

class FetchUtil(object):
    def __init__(self):
        pass

    def fetch_html(self, url, retry=10, timeout=20):
        while retry > 0:
            rsp = requests.get(url, timeout=timeout)
            if rsp.status_code == 200:
                return rsp.text
            retry -= 1
            time.sleep(1)
        return ""

    def parse_date(self, origin_date):
        year = origin_date.split(",")[-1]
        day = origin_date.split(" ")[1].split(",")[0]
        month = settings.month_map[origin_date.split(" ")[0]]     #   字典，用中括号
        return "%s%s%s" % (year, month, day)

    def get_dom(self, html):
        dom = etree.HTML(html)
        return dom

    def parse_dom(self, dom, rule):
        pretty_dom = dom.xpath(rule)
        return len(pretty_dom) > 0, pretty_dom

    def deal_missing_value(self, origin_value):
        if "-" == origin_value:
            return 0.00
        return origin_value

    # def get_attr_by_dom(self, dom, attr, index=0):
    #     values = dom.xpath(attr)
    #     try:
    #         pretty_dom = dom.xpath(rule)[index]
    #         return pretty_dom
    #     except Exception as e:
    #         return None
    #     if len(values) < 1: #   属性是否是空值
    #         return ""       #   "" 空值
    #     return values[0]


fetch_util = FetchUtil()


