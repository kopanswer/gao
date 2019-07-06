#  --*-- coding:utf8 --*--

import re
from class_four.model_years import YearsModel
import class_four.setting
from exercise.class_four_exercise.utility import util_func

class ProcessYears(object):
    def __init__(self):
        pass

    def fetch_years(self):
        years = []
        for year in range(class_four.setting.minyear, class_four.setting.maxyear+1):
            year_url = class_four.setting.year_url.format(year=year)
            year_htm = util_func.fetch_html(year_url)
            year_dom = util_func.parse_html(year_htm)
            if not year_dom:
                continue
            spans = year_dom.xpath('.//div[@class="zg_main_page"]/p//span')[0].text
            year_model = self.pretty_years(year, spans)
            year_model.save()
            self.show_years(year_model)
            years.append(year_model)
        return years

    def pretty_years(self, year, spans):
        year_content = YearsModel()
        year_content.year = year
        year_content.items = str(re.compile(r'\d+').findall(spans)[0])
        year_content.pages = str(int(int(year_content.items)/15) + 1)
        return year_content

    def show_years(self, year_model):
        print "第", year_model.year, "年有", year_model.pages, "页", year_model.items, "种职位\n"

    def process_years(self):
        self.fetch_years()

process_years = ProcessYears()



