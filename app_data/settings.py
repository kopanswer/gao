# -*- coding:utf8 -*-
import os

SECRET_KEY = '5n_=nvbtprsei+93l1im%)+4skc4*x37va_3xi0p75_e3b4rxt'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTALLED_APPS = [
    'app_data'
]

# DATABASES = {
#    'mydata': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME':   'mydata',
#        'USER': 'root',
#        'PASSWORD': '123456',
#        'HOST': '127.0.0.1',
#        'PORT': 3306,
#    }
# }

DATABASES = {
    'teach': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'teach',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '47.100.201.90',
        'PORT': 3306,
    }
}

DATABASES['default'] = DATABASES['teach']

DEBUG = True


class DBRouter(object):
    tables = (
        'offcn',
        'test'
        )

    def db_for_read(self, model, **hints):
        db = None
        tbl = model._meta.db_table
        if tbl in self.tables:
            db = 'teach'
        return db

    def db_for_write(self, model, **hints):
        db = None
        tbl = model._meta.db_table
        if tbl in self.tables:
            db = 'teach'
        return db


DATABASE_ROUTERS = ['app_data.settings.DBRouter', ]

TIME_ZONE = 'Asia/Shanghai'

USE_TZ = False
