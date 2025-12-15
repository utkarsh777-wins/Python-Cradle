#  Super method
#super() method is used to access methods of the parnet class.
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class TeslaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        

# car1 = TeslaCar("Y")  AttributeError: 'TeslaCar' object has no attribute 'type'
car1 = TeslaCar("Y", "Electric")
print(car1.type)