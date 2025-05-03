# Problem 08: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model
    
my_car = Car("Zata", "Nexon")

# my_car.model = "Nano"
# AttributeError: property 'model' of 'Car' object has no setter

# print(my_car.model())
# TypeError: 'str' object is not callable

print(my_car.model)    # Nexon