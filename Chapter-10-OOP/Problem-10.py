# Problem 10: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Engine():
    def engine_info(self):
        print("Engine Type: Electric")

class Battery():
    def __init__(self, battery_size):
        self.__battery_size = battery_size

    def battery_info(self):
        print(f"Battery Size: {self.__battery_size}")

class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        print(f"Car: {self.__brand} {self.__model}")

class ElectricCar(Car, Engine, Battery):
    def __init__(self, brand, model, battery_size):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)

my_car = ElectricCar("Ravindra", "XEV 9e", "59 kWh")

my_car.full_name()      # Car: Ravindra XEV 9e
my_car.battery_info()   # Battery Size: 59 kWh
my_car.engine_info()    # Engine Type: Electric