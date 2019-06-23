# -*- coding:utf8 -*-

"""
@discription: 变量和字符串格式化
@author: xxx
@date: 2019-03-09
"""

def show_variable():
    """
    这是一个展示变量的函数
    """
    #   静态类型：先定义后赋值
    #   动态类型：先赋值后定义
    a = 1
    print(type(a))
    b = 1.1
    print(type(b))
    c = "abc"
    print(type(c))
    d = (1,2)
    print(type(d))
    e = [1,2,3]
    print(type(e))
    #   ctrl + /    注释及恢复
    b = e
    print(type(b))

def str_format(name, age):
    """
    字符串格式化
    """
    # hello_str = "hello %s, my age is %d" % (name, age)
    hello_str = "hello %s, my age is %s" % (name, str(age))
    print(hello_str)

def use_list():
    """
    列表
    增删改查：元素而不是下标
    """
    new_list = []
    new_list_b = [1,2,3]

    #   增
    new_list.append(1)
    new_list.append("123")
    new_list.append(22)
    new_list += new_list_b  #   拼接：不去重的 merge
    print(new_list)

    #   删
    # new_list.remove("123")
    # new_list.remove(new_list[0])
    # print(new_list)

    #   改
    # new_list[0] = 2
    # print(new_list)

    #   查
    #   1.下标查
    # print(new_list[0])
    # print(new_list_b)
    #   2.遍历
    # use_circle(new_list)
    # use_circle(new_list_b)
    #   3.特性
    #       a.顺序存储，dict 和 set 是随机存储
    #       b.数据可以被修改（覆盖）
    #       c.元素可以支持多种数据类型，甚至包括 dict 和 set
    #   4.切片
    #       list[a:b] -> [a,b-1]
    #       输出的还是 list
    # print(new_list[1:3])

def test_list(items):
    #   逻辑 [1,2,3] -> [3,2,1]
    l = len(items)
    result = []
    while l > 0:
        result.append(items[l-1])
        l -= 1
    #   反转列表
    return result

def use_tuple():
    """
    元组：(1,2,3)
    """
    #   顺序存储
    #   元素可以支持多种数据类型
    #   数据不能被修改，只能读不能写，这是与 list 最大区别
    tp = (1,2,3,)
    tp += (4,)
    print(tp)
    print(tp[0])
    print(tp[-1])

def use_dict():
    one = {}
    two = dict()
    #   增
    one["k"] = "v"
    print(one)

    #   删
    one.pop("k")
    print(one)

    #   改
    one["k"] = "u"
    print(one)

    #   .items() 查找所有键值对
    # for k, v in one.items():
    #     print("Key is :%s" % k)
    #     print("Value is :%s" % v)

    # for k in one.keys():
    #     v = one[k]
    #     print("Key is :%s" % k)
    #     print("Value is :%s" % v)

    #   特性
    #       key 支持字符串，浮点，整型
    #       value 支持任意数据类型
    #       随机存储，不管输入顺序如何，输出顺序随机

def use_set():

    names = set()
    #   自动去重
    names.add("tom")
    print(names)

    name = names.pop()
    print(names)
    print(name)
    #   pop() 随机删除集合中的一个元素，并返回被删除的对象

    names.add("tom")
    names.add("tom")
    names.add("tom")
    names.add(1)
    print(names)

    #   特性
    #       自动去重
    #       元素删除随机，插入随机
    #       元素支持多种数据结构

def test_dict(students, name):
    #   students 是一个 dict，姓名分数键值表
    #   给一个 name. 查询他的成绩
    #   若不在 dict 里面返回 0
    for k, v in students.items():
        if name == k:
            return v
    return 0
    # students.get(name,0)
    #   get() 相当于把上面的循环封装一下


def use_circle(items):
    for item in items:
        print(item)

#   系统入口变量 __name__
if __name__ == "__main__":
    # print(__name__)
    # print("hello world")
    # show_variable()
    # str_format("xiaoming", 10)
    # use_list()
    # print(test_list([1,2,3,"str","123"]))
    # use_tuple()
    # use_dict()
    # use_set()