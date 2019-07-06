#  --*-- coding:utf8 --*--

import os
import django
import time
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
from app_data.models.entity import Details
from class_five.process_years import process_years
from class_five.model_details import DetailsModel
import class_five.setting
from exercise.class_four_exercise.utility import util_func


class ProcessDetails(object):
    def __init__(self):
        pass

    def fetch_details(self, years):
        errors = 0
        details = []
        for year_model in years:
            year = year_model.year
            items = int(year_model.items)
            for item in range(1, items + 1, 1):
                item_url = class_five.setting.item_url.format(year=year, item=item)
                item_htm = util_func.fetch_html(item_url)
                item_dom = util_func.parse_html(item_htm)
                if not item_dom:
                    continue
                # Chrome Browser: xpath helper
                ths = item_dom.xpath('.//div[@class="zw_zwxx_jies"]//th')
                tds = item_dom.xpath('.//div[@class="zw_zwxx_jies"]//td')
                if len(ths)+1!=len(tds):
                    errors += errors
                if errors > 0:
                    print "ths 和 tds 数量不匹配"
                details = details + self.pretty_detail(year, item, ths, tds)
                [detail.save() for detail in details]
                details = []
                print "第", year, "年第", item, "种职位详细信息爬取成功。"

        return details

    def pretty_detail(self, year, item, ths, tds):
        details = []
        for i in range(len(tds)-1):
            detail_content = DetailsModel()
            detail_content.year = year
            detail_content.gid = item
            #   如果 key 或 value 为空，就不需要存储
            if not(ths[i].text and tds[i].text):
                continue
            detail_content.key = ths[i].text.encode("utf8")
            detail_content.value = tds[i].text.encode("utf8")
            details.append(detail_content)
        detail_content = DetailsModel()
        detail_content.year = year
        detail_content.gid = item
        detail_content.key = "备注"
        detail_content.value = tds[-1].text.encode("utf8")
        details.append(detail_content)
        return details

    def monitor(self):
        #   一直运行
        while True:
            print "当前抓取数量：%s" % Details.objects.all().count()
            time.sleep(3)

    #   进程
    def process(self):
        import threading
        threading.Thread(target=self.monitor).start()
        years = process_years.process()
        self.fetch_details(years)

process_details = ProcessDetails()






