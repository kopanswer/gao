#!/usr/bin/env python 
# -*- coding:utf-8 -*-

"""
@discription: 关联大股东 - set
@author: hjk
@date: 2019-04-22
"""

def use_set():
    new_set = set()
    forloop_set = set()
    for i in range(1,11,1):
        new_set.add(i)
    for i in new_set:
        forloop_set.add(i)
    for i in forloop_set:
        new_set.add(i+10)
    for i in new_set:
        print(i)


if __name__ == "__main__":
    use_set()












































    