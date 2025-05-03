# Problem 02: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Ezuzu", "V-cross")

print(f"Brand: {my_car.brand}")
# Output: Brand: Ezuzu

print(f"Model: {my_car.model}")
# Output: Model: V-cross

print(f"Full Name: {my_car.full_name()}")
# Output: Full Name: Ezuzu V-cross