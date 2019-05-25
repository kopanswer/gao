# -*- coding:utf8 -*-
import random

class Random_Generator(object):

    def __init__(self, min=0, max=10000, num=5000):
        self.num = num
        self.min = min
        self.max = max

    def randoms(self):
        result = []
        for i in range(self.num):
            result.append(random.randint(self.min,self.max))
        return result

