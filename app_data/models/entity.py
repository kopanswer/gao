# --*-- coding:utf8 --*--

from django.db import models

# class Test(models.Model):
#     class Meta:
#         db_table = "test"
#
#     id = models.BigIntegerField(primary_key=True, auto_created=True)
#     name = models.CharField(max_length=100, default="")
#     create_time = models.DateTimeField(auto_now_add=True)
#     modify_time = models.DateTimeField(auto_now=True)
#     extra = models.CharField(max_length=300, default='')

class Years(models.Model):
    class Meta:
        #   命名 mysql 数据库为 years
        db_table = "years"

    #   类似在 NaviCat 里面设置变量
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    year = models.CharField(max_length=10, default="")
    items = models.CharField(max_length=255, default="")
    pages = models.CharField(max_length=255, default="")

class Pages(models.Model):
    class Meta:
        #   命名 mysql 数据库为 pages
        db_table = "pages"

    #   类似在 NaviCat 里面设置变量
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    year = models.CharField(max_length=10, default="")
    bureau = models.CharField(max_length=255, default="")
    office = models.CharField(max_length=255, default="")
    jobname = models.CharField(max_length=255, default="")
    jobcode = models.CharField(max_length=255, default="")
    candidates = models.CharField(max_length=255, default="")
    applicants = models.CharField(max_length=255, default="")
    qualifieds = models.CharField(max_length=255, default="")
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    extra = models.CharField(max_length=255, default="")

class Items(models.Model):
    class Meta:
        #   命名 mysql 数据库为 items
        db_table = "items"

    #   面板数据
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    year = models.CharField(max_length=10, default="")
    #   单位信息
    unit_site = models.CharField(max_length=255, default="")
    unit_sort = models.CharField(max_length=255, default="")
    unit_name = models.CharField(max_length=255, default="")
    unit_office = models.CharField(max_length=255, default="")
    unit_nature = models.CharField(max_length=255, default="")
    unit_hierarchy = models.CharField(max_length=255, default="")
    #   职位信息
    job_attribute = models.CharField(max_length=255, default="")
    job_name = models.CharField(max_length=255, default="")
    job_duty = models.CharField(max_length=255, default="")
    job_code = models.CharField(max_length=255, default="")
    test_category = models.CharField(max_length=255, default="")
    candidates = models.CharField(max_length=255, default="")
    #   报考条件
    major = models.CharField(max_length=255, default="")
    education = models.CharField(max_length=255, default="")
    degree = models.CharField(max_length=255, default="")
    politics = models.CharField(max_length=255, default="")
    experience = models.CharField(max_length=255, default="")
    TSOA = models.CharField(max_length=255, default="")
    WVOL = models.CharField(max_length=255, default="")
    CSVO = models.CharField(max_length=255, default="")
    SPPT = models.CharField(max_length=255, default="")
    #   其他信息
    arrange_exam = models.CharField(max_length=255, default="")
    is_more = models.CharField(max_length=255, default="")
    rate = models.CharField(max_length=255, default="")
    more_rules = models.CharField(max_length=255, default="")
    remark = models.CharField(max_length=255, default="")


