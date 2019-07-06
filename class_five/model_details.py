# --*-- coding:utf8 --*--
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()
from app_data.models.entity import Details
from class_five.utility import util_func

class DetailsModel(object):
    def __init__(self):
        self.year = ""
        self.gid = ""
        self.key = ""
        self.value = ""
        self.key_md5 = ""

    def save(self):
        self.key_md5 = util_func.generate_md5(self.key)
        Details.objects.update_or_create(
            #   过滤条件，是否等于
            year = self.year,
            gid = self.gid,
            key_md5 = self.key_md5,
            #  不用 key，因为 key 是中文，搜索效率低
            defaults=dict(
                key=self.key,
                value=self.value,
            )
        )

details_model = DetailsModel()

