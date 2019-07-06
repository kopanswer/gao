# --*-- coding:utf8 --*--
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
from app_data.models.entity import Years

class YearsModel(object):
    def __init__(self):
        self.year = ""
        self.items = ""
        self.pages = ""

    def save(self):
        Years.objects.update_or_create(
            #   过滤条件，是否等于
            year = self.year,
            defaults=dict(
                items=self.items,
                pages=self.pages,
            )
        )

years_model = YearsModel()