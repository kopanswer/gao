# --*-- coding:utf8 --*--

from django.db import models

class Test(models.Model):
    class Meta:
        db_table = "test"

    id = models.BigIntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, default="")
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    extra = models.CharField(max_length=300, default='')

class Offcn(models.Model):
    class Meta:
        db_table = "offcn"

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

