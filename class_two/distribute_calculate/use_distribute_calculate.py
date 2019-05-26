# -*- coding:utf8 -*
from distribute_class import DistributeHandler

if __name__ == "__main__":
    tasks = [item for item in range(1,105)]
    hander = DistributeHandler(tasks=tasks,work_nums=10)
    hander.process()