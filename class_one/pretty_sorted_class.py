# -*- coding:utf8 -*-

from sort_class import SortedHandler
import time

class PrettySorted(SortedHandler):
    def __init__(self,data=None):
        SortedHandler.__init__(self,data)

    def pretty(self,method=None):
        print "--sort begin--"
        start_time = time.time()
        print self.sorted(self.data,method=method)
        time.sleep(0.1)
        end_time = time.time()
        all_time = end_time - start_time
        print "--sort end，all time is %s seconds----" % str(all_time)