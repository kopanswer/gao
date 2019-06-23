# -*- coding:utf8 -*-

"""
@discription: 文件处理
@author: xxx
@date: 2019-03-09
"""

class FileProcess:
    def __init__(self, path="./data/test.txt"):
        self.path = path

    #  通用写法（二进制读取 read ），包含三句话：打开，读，关闭
    def read(self):
        with open(self.path, 'r') as fs:
            return "".join(fs.readlines())
            # for item in fs.readlines():
            #     result += str(item).replace("\n","").replace("\r","")
        # return result
        # return data

    def write(self, data, writetype):
        with open(self.path, writetype) as fs:
            fs.write(data)
        return "write successfully"

    def process(self):
        #   写文件
        self.write("hello world\n", "a")
        print(self.read())
        #   读文件



if __name__ == "__main__":
    fileobj = FileProcess()
    fileobj.process()