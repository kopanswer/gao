#  --*-- coding:utf8 --*--

import random
import time
from class_four.process_years import process_years
import class_four.setting
from exercise.class_four_exercise.utility import util_func

class ProcessVarbs(object):
    def __init__(self):
        pass

    def fetch_varbs(self, years):
        varb_set = set()
        for year_model in years:
            year = year_model.year
            items = int(year_model.items)
            for item in range(1, items + 1, 1):
                item_url = class_four.setting.item_url.format(year=year, item=item)
                item_htm = util_func.fetch_html(item_url)
                item_dom = util_func.parse_html(item_htm)
                if not item_dom:
                    continue
                # Chrome Browser: xpath helper
                ths = item_dom.xpath('.//div[@class="zw_zwxx_jies"]//th')
                for th in ths:
                    varb_set.add(th.text)
                print "第", year, "年第", item, "种职位的变量爬取完毕 ", item_url

    def show_varbs(self, varb_set):
        for varb in varb_set:
            print varb

    #   进程
    def process_varbs(self):
        years = class_four.process_years.process_years.fetch_years()
        varb_set = self.fetch_varbs(years)
        self.show_varbs(varb_set)

process_varbs = ProcessVarbs()