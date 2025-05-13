# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Book:
    def __init__(self, type, category, stock):
        self.type = type
        self.category = category
        self.stock = stock
    
    def buy_one(self):
        print(f"Stock in storage is: {self.stock}")
        

class Novel(Book):
    def __init__(self, author_name, type, category, stock):
        super().__init__(type, category, stock)
        self.author_name = author_name
        
    def get_author_name(self):
        print(self.author_name)

new_novel = Novel("Jules Verne", "Paperback", "Adventures", 3)
print(new_novel.author_name)
new_novel.buy_one()

# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
class Vehicle:
    def __init__(self, wheels_number):
        self.wheels_number = wheels_number
        
class Bicycle(Vehicle):
    def __init__(self, wheels_number, brand):
        super().__init__(wheels_number)
        self.brand = brand  
        
    def move(self):
        print(f"{self.brand} moves as fast as the person can do effort in cycling :D ")
        
class Car(Vehicle):
    def __init__(self, wheels_number, brand, max_speed):
        super().__init__(wheels_number)
        self.brand = brand
        self.max_speed = max_speed
    
    def move(self):
        print(f"{self.brand} moves with maximum speed {self.max_speed} mile/hr")
        
class Plane(Vehicle):
    def __init__(self, wheels_number, brand, max_speed):
        super().__init__(wheels_number)
        self.brand = brand
        self.max_speed = max_speed
        
    def move(self):
        print(f"{self.brand} flies with maximum speed {self.max_speed} km/hr")
        
new_bicycle = Bicycle(2, "Santa Cruz")      
new_bicycle.move()

new_car = Car(4, "BMW", 200)
new_car.move()

new_plane = Plane(4, "Boeing", 606)
new_plane.move()
