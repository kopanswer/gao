# --*-- coding:utf8 --*--

"""
    背熟练
"""


import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'app_data.settings'
django.setup()

from app_data.models.entity import Test

# 创建一条数据
# Test.objects.create(
#     name='abc'
# )
#   删除一条数据（按条件删除），会返回删除的条数
# print Test.objects.filter(id=1).delete()
#
# Test.objects.filter(id=2).update(name="bcd")

# # 查询数据
# obj = Test.objects.filter(id=2).first()
# print obj.name

# 插入或更新，插入的数据如果已经存在，不更新
Test.objects.update_or_create(
    id=2,
    defaults=dict(
        name="power",
        extra=123,
    )
)
