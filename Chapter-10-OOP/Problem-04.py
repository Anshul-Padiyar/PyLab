# Problem 04: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car():
    def __init__(self, brand, model):
        self.__brand = brand    # private attribute
        self.__model = model    # private attribute

    def get_brand(self):    # getter method
        return self.__brand

    def set_brand(self, brand):    # setter method
        self.__brand = brand

    def get_model(self):    # getter method
        return self.__model

    def set_model(self, model):    # setter method
        self.__model = model

my_car = Car("Muzuki", "Baleno")

# print(my_car.__brand)
# AttributeError: 'Car' object has no attribute '__brand'

print(f"Brand: {my_car.get_brand()}")    # Brand: Muzuki
print(f"Model: {my_car.get_model()}")    # Model: Baleno

my_car.set_model("Jimny")

print(f"Brand: {my_car.get_brand()}")    # Brand: Muzuki
print(f"Model: {my_car.get_model()}")    # Model: Jimny