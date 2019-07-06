# --*-- coding:utf8 --*--
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
from app_data.models.entity import Items

class ItemsModel(object):
    def __init__(self):
        self.year = ""
        self.unit_site = ""
        self.unit_sort = ""
        self.unit_name = ""
        self.unit_office = ""
        self.unit_nature = ""
        self.unit_hierarchy = ""
        self.job_attribute = ""
        self.job_name = ""
        self.job_duty = ""
        self.job_code = ""
        self.test_category = ""
        self.candidates = ""
        self.major = ""
        self.education = ""
        self.degree = ""
        self.politics = ""
        self.experience = ""
        self.TSOA = ""
        self.WVOL = ""
        self.CSVO = ""
        self.SPPT = ""
        self.arrange_exam = ""
        self.is_more = ""
        self.rate = ""
        self.more_rules = ""
        self.remark = ""

    def save(self):
        Items.objects.update_or_create(
            #   过滤条件，是否等于
            year = self.year,
            unit_name = self.unit_name,
            unit_office = self.unit_office,
            job_name = self.job_name,
            job_code = self.job_code,
            job_duty = self.job_duty,
            defaults=dict(
                unit_site = self.unit_site,
                unit_sort = self.unit_sort,
                unit_nature = self.unit_nature,
                unit_hierarchy = self.unit_hierarchy,
                job_attribute = self.job_attribute,
                test_category = self.test_category,
                candidates = self.candidates,
                major = self.major,
                education = self.education,
                degree = self.degree,
                politics = self.politics,
                experience = self.experience,
                TSOA = self.TSOA,
                WVOL = self.WVOL,
                CSVO = self.CSVO,
                SPPT = self.SPPT,
                arrange_exam = self.arrange_exam,
                is_more = self.is_more,
                rate = self.rate,
                more_rules = self.more_rules,
                remark = self.remark,
            )
        )
