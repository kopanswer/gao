# -*- coding:utf8 -*-

"""
@discription: 面向对象
@author: xxx
@date: 2019-03-09
"""

#   类型命名规则：驼峰式
#   每个单词首字母大写，例如：WorldWidWeb2

#   构造函数：类中的初始化函数叫做

#   封装：一个个模块，用简单的话调用
#   抽象：把物理世界变成计算机内虚拟的对象的过程

class SchoolPeople:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    #   继承（函数）
    def valid(self):
        if self.position == "student":
            print("身份是学生")
        else:
            print("身份是老师")




class Student(SchoolPeople):
    # 初始化
    def __init__(self, name, position, score):
        self.name = name
        self.position = position
        self.score = score

    #   多态：继承的基础上修改
    def valid(self):
        if self.position == "student":
            print("身份可能是学生")
        else:
            print("身份是老师")

#   练习
#   两个类 Student 和 Audio
#   Audio 广播不及格的学生

class Audio:
    def __init__(self):
        self.Students = []

    def add_student(self, student):
        #   添加学生
        self.Students.append(student)

    def broadcast(self):
        #   将不及格的学生及其成绩 print 出来
        for s in self.Students:
            name = s.name
            score = s.score
            if score < 60:
                print("the unqualified student is: %s" % name)
                print("His/Her score is: %d" % score)


if __name__ == "__main__":
    # 实例化一个对象

    # xiaoming = Student(name="xiaoming", score=90, position="student")
    # print(xiaoming.position)
    # xiaoming.valid()

    xiaoa = Student(name="xiaoa", score=90, position="student")
    xiaob = Student(name="xiaob", score=20, position="student")
    xiaoc = Student(name="xiaoc", score=59, position="student")

    audio = Audio()
    audio.add_student(xiaoa)
    audio.add_student(xiaob)
    audio.add_student(xiaoc)
    audio.broadcast()
