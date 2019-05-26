# -*- coding:utf8 -*-

class Fruit(object):
    def __init__(self, name=None):
        self.name = name

    def eat(self):
        print "eating %s" % self.name
