# Problem 09: Demonstrate the use of isinstance() to check if my_car is an instance of Car and ElectricCar.

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
    

my_car = ElectricCar("Ravindra", "XEV 9e", "59 kWh")

print(f"Is instance of Car Class: {isinstance(my_car, Car)}") 
# Output: Is instance of Car Class: True

print(f"Is instance of ElectricCar Class: {isinstance(my_car, ElectricCar)}")
# Output: Is instance of ElectricCar Class: True