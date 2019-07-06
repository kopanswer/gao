#  --*-- coding:utf8 --*--

import random
import time
from class_four.process_years import process_years
from class_four.model_pages import PagesModel
import class_four.setting
from exercise.class_four_exercise.utility import util_func

class ProcessPages(object):
    def __init__(self):
        pass

    def fetch_pages(self, years):
        for year_model in years:
            year = year_model.year
            pages = int(year_model.pages)
            for page in range(1,pages+1,1):
                page_url = class_four.setting.page_url.format(year=year, page=page)
                page_htm = util_func.fetch_html(page_url)
                page_dom = util_func.parse_html(page_htm)
                if not page_dom:
                    continue
                # Chrome Browser: xpath helper
                table = page_dom.xpath('.//table')[0]
                trs = table.xpath('.//tr')
                if len(trs) == 0:
                    interval = random.randint(1, 15)
                    print "[tip] url:%s 抓取失败, %s 秒后重试" % (page_url, interval)
                    time.sleep(interval)
                    continue
                [pages_model.save() for pages_model in self.pretty_pages(year, trs)]
                print "第", year, "年第" , page, "页读取成功\n"

    def pretty_pages(self, year, trs):
        records = []
        for i in range(1, len(trs), 1):
            page_content = PagesModel()
            page_content.year = year
            page_content.bureau = trs[i].xpath('.//td')[0].xpath('.//a')[0].text
            page_content.office = trs[i].xpath('.//td')[1].text
            page_content.jobname = trs[i].xpath('.//td')[2].xpath('.//a')[0].text
            page_content.jobcode = trs[i].xpath('.//td')[3].text
            page_content.candidates = trs[i].xpath('.//td')[4].text
            page_content.applicants = trs[i].xpath('.//td')[5].text
            page_content.qualifieds = trs[i].xpath('.//td')[6].text
            records.append(page_content)
        return records

    #   进程
    def process_pages(self):
        years = class_four.process_years.process_years.fetch_years()
        self.fetch_pages(years)

process_pages = ProcessPages()



