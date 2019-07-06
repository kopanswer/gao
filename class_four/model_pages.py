# --*-- coding:utf8 --*--
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
from app_data.models.entity import Pages

class PagesModel(object):
    def __init__(self):
        self.year = ""
        self.bureau = ""
        self.office = ""
        self.jobname = ""
        self.jobcode = ""
        self.candidates = ""
        self.applicants = ""
        self.qualifieds = ""

    def save(self):
        Pages.objects.update_or_create(
            #   过滤条件，是否等于
            year = self.year,
            bureau = self.bureau,
            office = self.office,
            jobname = self.jobname,
            jobcode = self.jobcode,
            defaults=dict(
                candidates=self.candidates,
                applicants=self.applicants,
                qualifieds=self.qualifieds,
            )
        )

pages_model = PagesModel()