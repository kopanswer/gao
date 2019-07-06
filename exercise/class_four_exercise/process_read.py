#  --*-- coding:utf8 --*--

import re
import random
import time
from class_four.offcn_model import OffcnContent
import class_four.setting
from class_four.utility import util_func

class ProcessRead(object):
    def __init__(self):
        pass

    def fetch_refs(self):
        refs = {}
        for year in range(2013, 2019):
            year_url = class_four.setting.base_url.format(year=year)
            year_htm = util_func.fetch_html(year_url)
            year_dom = util_func.parse_html(year_htm)
            if not year_dom:
                continue
            position = year_dom.xpath('.//div[@class="zg_main_page"]/p//span')[0].text
            positions = int(re.compile(r'\d+').findall(position)[0])
            pages = int(positions/15) + 1
            refs[year] = (pages, positions)
        return refs

    def show_refs(self, positions):
        for year, value in positions.items():
            print year, "年有", value[0], "页，", value[1],"种岗位，"

    def fetch_pages(self, positions):
        for year, value in positions.items():
            for page in range(1,value[0]+1,1):
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
                [offcn_model.save() for offcn_model in self.pretty_trs(year, trs)]
                # 等价于：
                # for offcn_model in self.pretty_trs(year, trs):
                #     offcn_model.save()
                print "第", year, "年第" , page, "页读取成功\n"

    def pretty_trs(self, year, trs):
        records = []
        for i in range(1, len(trs), 1):
            offcn_content = OffcnContent()
            offcn_content.year = year
            offcn_content.bureau = trs[i].xpath('.//td')[0].xpath('.//a')[0].text
            offcn_content.office = trs[i].xpath('.//td')[1].text
            offcn_content.jobname = trs[i].xpath('.//td')[2].xpath('.//a')[0].text
            offcn_content.jobcode = trs[i].xpath('.//td')[3].text
            offcn_content.candidates = trs[i].xpath('.//td')[4].text
            offcn_content.applicants = trs[i].xpath('.//td')[5].text
            offcn_content.qualifieds = trs[i].xpath('.//td')[6].text
            records.append(offcn_content)
        return records

    #   进程
    def process_read(self):
        refs = self.fetch_refs()
        self.show_refs(refs)
        self.fetch_pages(refs)

process_read = ProcessRead()



