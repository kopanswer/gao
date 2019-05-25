# -*- coding:utf8 -*-
from sort_class import SortedHandler
from pretty_sorted_class import PrettySorted
from random_generator import Random_Generator

if __name__ == "__main__":
    # data = [3,1,2,4,10,100,5]
    #
    # #   创建类的实例
    # sorted_handler = SortedHandler(data)
    # print sorted_handler.sorted()
    # #   后面需要改
    # data = [20,10,30]
    # print sorted_handler.sorted()
    # print sorted_handler.sorted(data)
    # print sorted_handler.sorted(data,method='select')
    #
    # pretty_sorted = PrettySorted(data)
    # pretty_sorted.pretty()

    randomhandler = Random_Generator(min=0,max=10000,num=10000)
    data=randomhandler.randoms()
    # sorted_handler = SortedHandler(data=data)

    sorted_handler = PrettySorted(data=data)
    sorted_handler.pretty(method="bubble")
    sorted_handler.pretty(method="select")