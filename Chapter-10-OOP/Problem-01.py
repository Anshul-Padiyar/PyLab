# Problem 01: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car= Car("Ravindra", "BE 6")

print(f"Brand: {my_car.brand}")
# Output: Brand: Ravindra

print(f"Model: {my_car.model}")
# Output: Model: BE 6