# -*- coding:utf8 -*-

"""
@discription: 多线程
@author: xxx
@date: 2019-03-09
"""

import threading
from demo4 import FileProcess
from queue import Queue


#   有一个线程读文件，往队列里面送
#   有三个线程读队列，然后计算
#   结果汇总 （SPooling技术）

#   全局变量
work_queue = Queue()
file_process = FileProcess()    #   有默认参数
send_status = False
sum = 0

def send_queue():
    global send_status
    data = file_process.read()
    for item in data.split('\n'):
        if not item.replace("\n","").replace("\r",""):
            continue
        work_queue.put(item)
    send_status = True

def calc_thread():
    global sum
    while not (work_queue.empty() and send_status):
        num = work_queue.get()
        sum += int(num)
        print("%d \n" % sum)

def start():

    #   一个读取线程
    threading.Thread(target=send_queue).start()

    #   三个计算线程
    for i in range(3):
        threading.Thread(target=calc_thread).start()

#   输入输出解耦

if __name__ == "__main__":

    start()