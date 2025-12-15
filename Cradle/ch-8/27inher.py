# Types
'''
-Single Inheritance --single base & derived class

-Multi-level Inheritance --parent-child-they become parent - child

-Multiple Inheritance --inheriting the property of multiple classes


'''
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class TeslaCar(Car):
    def __init__(self, brand):
        self.name = brand

class X(TeslaCar):      #Multi-level Inheritance
    def __init__(self, type):
        self.type = type

car1 = X("Electric")
car1.start()