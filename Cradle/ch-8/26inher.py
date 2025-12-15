class Car:
    color = "space grey"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class TeslaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TeslaCar("Y")
car2 = TeslaCar("X")

print(car1.name)
print(car2.name)

print(car1.start())
print(car2.stop())
print(car1.color)