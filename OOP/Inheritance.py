
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describe(self):
        return f"{self.name} is {self.age} years old"
    
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal): 
    def __init__(self, name, age, breed):
        super().__init__(name, age)  
        self.breed = breed
    
    def make_sound(self):  
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):  
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self): 
        return "Meow! Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture!"


dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Orange")


print(f"Dog: {dog.describe()}, Breed: {dog.breed}")
print(f"Dog sound: {dog.make_sound()}")
print(dog.fetch())

print()

print(f"Cat: {cat.describe()}, Color: {cat.color}")
print(f"Cat sound: {cat.make_sound()}")
print(cat.scratch())

print("\n" + "="*50 + "\n")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):  
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def display_info(self):
        return f"{super().display_info()} - {self.num_doors} doors"

class ElectricCar(Car):  
    def __init__(self, brand, model, num_doors, battery_capacity):
        super().__init__(brand, model, num_doors)
        self.battery_capacity = battery_capacity
    
    def display_info(self):
        return f"{super().display_info()} - Battery: {self.battery_capacity} kWh"

electric_car = ElectricCar("Tesla", "Model 3", 4, 75)
print(f"Electric Car: {electric_car.display_info()}")

print("\n" + "="*50 + "\n")


class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return "Area not calculated"

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 10, 4)
triangle = Triangle("Triangle", 6, 8)


print(f"{circle.name} area: {circle.area():.2f}")
print(f"{rectangle.name} area: {rectangle.area()}")
print(f"{triangle.name} area: {triangle.area()}")

print("\n" + "="*50 + "\n")


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_info(self):
        return f"{self.name} (ID: {self.employee_id}) - Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, team_size):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team_size = team_size
    
    def get_info(self):
        return f"{super().get_info()} - {self.team_size} team members in {self.department}"

class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
    
    def get_info(self):
        languages = ", ".join(self.programming_languages)
        return f"{super().get_info()} - Languages: {languages}"


manager = Manager("Alice", "M001", 120000, "Engineering", 5)
developer = Developer("Bob", "D001", 100000, ["Python", "JavaScript", "Java"])

print(manager.get_info())
print(developer.get_info())

print("\n" + "="*50 + "\n")


print("Checking inheritance relationships:")
print(f"developer is instance of Developer: {isinstance(developer, Developer)}")
print(f"developer is instance of Employee: {isinstance(developer, Employee)}")
print(f"manager is instance of Manager: {isinstance(manager, Manager)}")

print(f"\nDeveloper is subclass of Employee: {issubclass(Developer, Employee)}")
print(f"Manager is subclass of Employee: {issubclass(Manager, Employee)}")
print(f"Employee is subclass of Employee: {issubclass(Employee, Employee)}")
