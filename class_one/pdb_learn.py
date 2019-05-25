# -*- coding:utf8 -*-

def add(a, b):
    c = a + b
    return c

def minus(a, b):
    c = a - b
    return c

if __name__ == "__main__":
    import pdb;pdb.set_trace()
    a = 1
    b = 2
    c = add(a,b)
    d = minus(a,b)
    print c
    print d