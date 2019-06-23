# -*- coding:utf8 -*-


"""
@discription: 函数
@author: xxx
@date: 2019-03-09
"""

def add1(a,b):
    return a+b

#   默认参数
def add2(a=1,b=2):
    return a+b

#   可变参数
def sum(*numbers, tip):      #   * 代表参数有若干个，传入的参数是对的，然后把 args 封装为一个 tuple
    print(type(numbers))
    sum = 0
    for number in numbers:
        sum += number
    print(tip)
    return sum

#   关键词参数
def print_map(**kw):        #   ** 传入的参数是独立的，然后把 kw 封装成一个字典
    print(type(kw))
    for k, v in kw.items():
        print(k,v)

#   通用函数（无论参数怎样，都可以运行）
def common_func(*args, **kw):
    print(type(args))
    print(args)
    print(kw)


#   递归函数
def fi(n):
    #   1   函数一定要有入口和出口，入口是参数，出口是最后一个return

    #   先考虑极端情况
    if n <= 0:
        return 0
    if n <= 2:
        return 1

    return fi(n-1) + fi(n-2)





if __name__ == "__main__":
    # print(add1(1,2))
    # print(add2())
    # print(add2(3))
    # print(add2(b=5))
    # print(sum(1))
    # print(sum(1,3))
    # print(sum(1,3,5,7,2,4,6,8))

    # result = sum(1,2,3,tip="finished")
    # print(result)

    # print_map(name="tom", age="18", name2="jack", key="value")

    # common_func(1,2,"b",3,a=1,b="kw")

    print(fi(3))


