# -*- coding:utf8 -*-

class SortedHandler(object):
    def __init__(self,data=None):
        self.data=data
        #   pass

    def bubble(self,data=None):
        if not data:
            data = self.data
        for i in range(len(data)):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
        return data

    def select(self,data=None):
        if not data:
            data = self.data
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    temp = data[j]
                    data[j] = data[i]
                    data[i] = temp
        return data

    def sorted(self,data=None,method="bubble"):
        if not data:
            data = self.data
        if method == "bubble":
            return self.bubble(data)
        if method == "select":
            return self.select(data)
        return self.bubble(data)

#   实例化（在电脑里申请内存）
#   sorted_handler = SortedHandler()