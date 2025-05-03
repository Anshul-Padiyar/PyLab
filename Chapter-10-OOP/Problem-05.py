# Problem 05: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def fuel_type(self):
        return "Petrol/Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size

    def set_battery_size(self, battery_size):
        self.__battery_size = battery_size

    def fuel_type(self):
        return "Electric"
    

my_car = Car("Nissanth", "Magnite")
print(my_car.fuel_type())   # Petrol/Diesel

my_new_car = ElectricCar("GM", "Comet EV", "17.3 kWh")
print(my_new_car.fuel_type())   # Electric