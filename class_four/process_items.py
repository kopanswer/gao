#  --*-- coding:utf8 --*--

import random
import time
from class_four.process_years import process_years
from class_four.model_items import ItemsModel
import class_four.setting
from exercise.class_four_exercise.utility import util_func

class ProcessItems(object):
    def __init__(self):
        pass

    def fetch_items(self, years):
        for year, value in years.items():
            for item in range(1,value[1]+1,1):
                item_url = class_four.setting.item_url.format(year=year, item=item)
                item_htm = util_func.fetch_html(item_url)
                item_dom = util_func.parse_html(item_htm)
                if not item_dom:
                    continue
                # Chrome Browser: xpath helper
                tables = item_dom.xpath('.//div[@class="zg_main"]//table')
                if len(tables) == 0:
                    interval = random.randint(1, 15)
                    print "[tip] url:%s 抓取失败, %s 秒后重试" % (item_url, interval)
                    time.sleep(interval)
                    continue
                item_model = self.pretty_item(year, tables)
                item_model.save()
                print "第", year, "年第" , item, "项读取成功\n"

    def pretty_item(self, year, tables):
        item_content = ItemsModel()
        item_content.year = year
        item_content.unit_site = tables[0].xpath('.//tr')[0].xpath('.//td')[0].text
        item_content.unit_sort = tables[0].xpath('.//tr')[0].xpath('.//td')[1].text
        item_content.unit_name = tables[0].xpath('.//tr')[1].xpath('.//td')[0].text
        item_content.unit_office = tables[0].xpath('.//tr')[1].xpath('.//td')[1].text
        item_content.unit_nature = tables[0].xpath('.//tr')[2].xpath('.//td')[0].text
        item_content.unit_hierarchy = tables[0].xpath('.//tr')[2].xpath('.//td')[1].text
        item_content.job_attribute = tables[1].xpath('.//tr')[0].xpath('.//td')[0].text
        item_content.job_name = tables[1].xpath('.//tr')[0].xpath('.//td')[1].text
        item_content.job_duty = tables[1].xpath('.//tr')[1].xpath('.//td')[0].text
        item_content.job_code = tables[1].xpath('.//tr')[1].xpath('.//td')[1].text
        item_content.test_category = tables[1].xpath('.//tr')[2].xpath('.//td')[0].text
        item_content.candidates = tables[1].xpath('.//tr')[2].xpath('.//td')[1].text
        item_content.major = tables[2].xpath('.//tr')[0].xpath('.//td')[0].text
        item_content.education = tables[2].xpath('.//tr')[0].xpath('.//td')[1].text
        item_content.degree = tables[2].xpath('.//tr')[1].xpath('.//td')[0].text
        item_content.politics = tables[2].xpath('.//tr')[1].xpath('.//td')[1].text
        item_content.experience = tables[2].xpath('.//tr')[2].xpath('.//td')[0].text
        item_content.TSOA = tables[2].xpath('.//tr')[2].xpath('.//td')[1].text
        item_content.WVOL = tables[2].xpath('.//tr')[3].xpath('.//td')[0].text
        item_content.CSVO = tables[2].xpath('.//tr')[3].xpath('.//td')[1].text
        item_content.SPPT = tables[2].xpath('.//tr')[4].xpath('.//td')[0].text
        item_content.arrange_exam = tables[3].xpath('.//tr')[0].xpath('.//td')[0].text
        item_content.is_more = tables[3].xpath('.//tr')[0].xpath('.//td')[1].text
        item_content.rate = tables[3].xpath('.//tr')[1].xpath('.//td')[0].text
        item_content.more_rules = tables[3].xpath('.//tr')[1].xpath('.//td')[1].text
        item_content.remark = tables[3].xpath('.//tr')[2].xpath('.//td')[0].text
        return item_content

    #   进程
    def process_items(self):
        years = class_four.process_years.process_years.fetch_years()
        self.fetch_items(years)

process_items = ProcessItems()



