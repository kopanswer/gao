# -*- coding:utf8 -*-

data = [1,2,3,3,2,1]

#   写一个函数，输出没有重复的数值
#   1.循环    2.数据结构强制转换
def nonrepeat1():
    a=[]
    for i in data:
        if i not in a:
            a.append(i)
    return a

def nonrepeat2():
    return list(set(data))

if __name__ == "__main__":
    print nonrepeat1()
    print nonrepeat2()

