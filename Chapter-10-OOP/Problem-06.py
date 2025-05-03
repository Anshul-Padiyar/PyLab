# Problem 06: Add a class variable to Car that keeps track of the number of cars created.

class Car():
    car_count = 0    # class variable

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.car_count += 1
        Car.car_count +=1

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

car01 = Car("Muzuki", "Fronx")
car02= Car("Ravindra", "BE 6")

print(f"car01.car_count = {car01.car_count}")   # car01.car_count = 2
print(f"car02.car_count = {car02.car_count}")   # car02.car_count = 2
print(f"Car.car_count = {Car.car_count}")   # Car.car_count = 2 


car03=  Car("Nissanth", "Magnite")

print(f"car01.car_count = {car01.car_count}")   # car01.car_count = 3
print(f"car02.car_count = {car02.car_count}")   # car02.car_count = 3
print(f"car03.car_count = {car03.car_count}")   # car03.car_count = 3
print(f"Car.car_count = {Car.car_count}")   # Car.car_count = 3