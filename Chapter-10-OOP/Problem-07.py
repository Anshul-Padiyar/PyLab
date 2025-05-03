# Problem 07: Add a static method to the Car class that returns a general description of a car.

class Car():
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

    @staticmethod
    def general_description():
        return "When everything is coming your way, you're in the wrong lane."


my_car = Car("Zata", "Curvv")

# print(my_car.general_description())

print(Car.general_description())
# Output: When everything is coming your way, you're in the wrong lane.