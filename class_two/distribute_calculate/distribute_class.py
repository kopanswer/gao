# -*- coding:utf8 -*-

import threading
from Queue import Queue
import time
import random

sum_queue = Queue()

class DistributeHandler(object):
    def __init__(self, tasks, work_nums):
        """
        :param tasks: 任务列表
        :param work_nums:  机器数量
        """
        self.tasks = tasks
        self.work_nums = work_nums
        self.worker_status = self.init_tasks_status()

    def init_tasks_status(self):
        status = []
        for i in range(self.work_nums):
            status.append(False)
        return status

    def assign_tasks(self):
        results = []
        batch_size = len(self.tasks) / self.work_nums
        for i in range(self.work_nums - 1):
            start = i * batch_size
            end = start + batch_size
            results.append(self.tasks[start: end])
        remain_start = batch_size * (self.work_nums - 1)
        results.append(self.tasks[remain_start: len(self.tasks)])
        return results

    def distribute_calc(self, results):
        threads = []
        currentID = 0
        for task in results:
            threads.append(threading.Thread(target=self.calc, args=(task, currentID,)))
            currentID += 1
        [thread.start() for thread in threads]

    def calc(self, task, workerID):
        """
        单纯进行计算
        :param task: 任务列表
        :return:
        """
        s = 0
        for i in task:
            s += i
        time.sleep(random.randint(1, 3))

        self.worker_status[workerID] = True
        sum_queue.put((workerID, s))

        print "workerID:%s\n计算的范围是:%s\n结果是:%s\n" % (str(workerID), str(task), str(s))

        return s

    def is_finish(self):
        for status in self.worker_status:
            if not status:
                return False
        return True

    def sum_calc(self):
        s = 0
        while True:
            if not sum_queue.empty():
                workID, result = sum_queue.get()
                s += result
                print "work_id:%s, result:%s" % (str(workID), str(result))
            if self.is_finish() and sum_queue.empty():
                print "finish"
                break
        return s

    def show(self, s):
        while True:
            if self.is_finish() and sum_queue.empty():
                print "===============结果如下================="
                print "任务:%s\n机器数:%d\n最终计算结果:%s\n" % (str(self.tasks), self.work_nums, str(s))
                break
            else:
                print "正在计算"
                time.sleep(0.2)

    def process(self):
        # 1 分配任务
        results = self.assign_tasks()
        # 2 分布式计算
        self.distribute_calc(results)
        # 3 结果汇总
        s = self.sum_calc()
        # 4 展示
        self.show(s)
