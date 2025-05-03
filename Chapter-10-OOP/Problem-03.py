# Problem 03: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = ElectricCar("Zata", "Curvv EV", "55 kWh")

print(f"Brand: {my_car.brand}")     # Brand: Zata
print(f"Model: {my_car.model}")     # Model: Curvv EV
print(f"Model: {my_car.battery_size}")    # Model: 55 kWh

print(f"Full name: {my_car.full_name()}")
# Output: Full name: Zata Curvv EV