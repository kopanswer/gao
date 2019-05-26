# -*- coding:utf8 -*-

from fruit_class import Fruit

class Apple(Fruit):
    def __init__(self,name=None):
       Fruit.__init__(self,name)

    def eat_apple(self):
        print "peeling %s" % self.name
        self.eat()
        print "throwing %s" % self.name

