# Chapter 10: Object-Oriented Programming

## Key Concepts

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code into objects that contain both data and code. It provides a clear modular structure for programs, making it good for defining abstract data types, and is excellent for large, complex, and actively updated programs.

## Core Concepts with Examples

### 1. Class and Object
**Definition:** A class is a blueprint for creating objects (instances) that share similar properties and methods.

**Example:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Ravindra", "BE 6")
```

### 2. Methods and Self
**Definition:** Methods are functions defined inside a class that can access and modify object attributes using 'self'.

**Example:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
```

### 3. Inheritance
**Definition:** Inheritance allows a class to inherit attributes and methods from another class.

**Example:**
```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
```

### 4. Encapsulation
**Definition:** Encapsulation is the bundling of data and methods that operate on that data within a single unit (class) and restricting access to internals.

**Example:**
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand    # private attribute
    
    def get_brand(self):    # getter method
        return self.__brand
        
    def set_brand(self, brand):    # setter method
        self.__brand = brand
```

### 5. Polymorphism
**Definition:** Polymorphism allows objects of different classes to be treated as objects of a common base class, with each class implementing methods in its own way.

**Example:**
```python
class Car:
    def fuel_type(self):
        return "Petrol/Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"
```

### 6. Class Variables
**Definition:** Class variables are shared by all instances of a class.

**Example:**
```python
class Car:
    car_count = 0  # class variable
    
    def __init__(self, brand, model):
        Car.car_count += 1
```

### 7. Static Methods
**Definition:** Static methods are methods that don't require access to instance-specific data and can be called without creating an instance.

**Example:**
```python
class Car:
    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation"
```

### 8. Property Decorators
**Definition:** Property decorators allow you to define methods that can be accessed like attributes, providing more control over attribute access.

**Example:**
```python
class Car:
    @property
    def model(self):
        return self.__model
```

### 9. Instance Checking
**Definition:** isinstance() function is used to check if an object is an instance of a specified class or its subclasses.

**Example:**
```python
my_tesla = ElectricCar("Tesla", "Model 3", "75kWh")
print(isinstance(my_tesla, Car))        # True
print(isinstance(my_tesla, ElectricCar)) # True
```

### 10. Multiple Inheritance
**Definition:** Multiple inheritance allows a class to inherit from multiple parent classes.

**Example:**
```python
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)
```

## Interview Tips
- Always mention real-world analogies when explaining OOP concepts
- Focus on how these concepts help in code organization and reusability
- Be prepared to explain the differences between inheritance and composition
- Know when to use class methods vs static methods vs instance methods
- Understand the practical applications of encapsulation and data hiding