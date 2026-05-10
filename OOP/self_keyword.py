
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
    
    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old")
    
    def have_birthday(self):    
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print("Person 1:")
person1.introduce()
person1.have_birthday()

print("\nPerson 2:")
person2.introduce()
person2.have_birthday()

print("\n" + "="*50 + "\n")


class Calculator:
    def __init__(self, initial_value=0):
        self.result = initial_value
    
    def add(self, number):
        self.result += number
        print(f"Added {number}. Current result: {self.result}")
        return self.result
    
    def subtract(self, number):
        self.result -= number
        print(f"Subtracted {number}. Current result: {self.result}")
        return self.result
    
    def multiply(self, number):
        self.result *= number
        print(f"Multiplied by {number}. Current result: {self.result}")
        return self.result
    
    def display(self):
        print(f"Final result: {self.result}")

calc = Calculator(10)
calc.add(5)
calc.subtract(3)
calc.multiply(2)
calc.display()

print("\n" + "="*50 + "\n")
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    
    def teach_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned: {trick}")
    
    def show_tricks(self):
        print(f"{self.name}'s tricks: {self.tricks}")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Each dog has separate tricks
dog1.teach_trick("Sit")
dog1.teach_trick("Fetch")

dog2.teach_trick("Stay")
dog2.teach_trick("Roll")

print()
dog1.show_tricks()  
dog2.show_tricks()  

print("\n" + "="*50 + "\n")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
      
        return self.width * self.height
    
    def perimeter(self):
    
        return 2 * (self.width + self.height)
    
    def describe(self):
        area = self.area()
        perimeter = self.perimeter()
        print(f"Rectangle: {self.width}x{self.height}")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

rect = Rectangle(5, 3)
rect.describe()
