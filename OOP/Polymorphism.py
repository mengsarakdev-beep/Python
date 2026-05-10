
class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
    
    def fly(self):
        pass

class Parrot(Bird):
    def speak(self):
        return f"{self.name} says: Hello! How are you?"
    
    def fly(self):
        return f"{self.name} is flying in circles"

class Eagle(Bird):
    def speak(self):
        return f"{self.name} shrieks: SCREEEECH!"
    
    def fly(self):
        return f"{self.name} is soaring high in the sky"

class Penguin(Bird):
    def speak(self):
        return f"{self.name} squawks: Wark wark!"
    
    def fly(self):
        return f"{self.name} cannot fly, but swims instead"


birds = [Parrot("Polly"), Eagle("Eddie"), Penguin("Percy")]

print("Bird Sounds:")
for bird in birds:
    print(bird.speak())

print("\nBird Movement:")
for bird in birds:
    print(bird.fly())

print("\n" + "="*50 + "\n")

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

class Duck:
    def make_sound(self):
        return "Quack!"

def animal_concert(animals):
    """This works with any object that has make_sound method"""
    for animal in animals:
        print(animal.make_sound())

animals = [Dog(), Cat(), Cow(), Duck()]
print("Animal Concert:")
animal_concert(animals)


class Robot:
    def make_sound(self):
        return "Beep boop!"

animals.append(Robot())
print("\nAnimal Concert with Robot:")
animal_concert(animals)

print("\n" + "="*50 + "\n")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """String representation"""
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")

v3 = Vector(2, 3)
print(f"v1 == v3: {v1 == v3}")

print("\n" + "="*50 + "\n")


class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        """Process payment using different methods"""
        return payment_method.pay(amount)

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ({self.card_number})"

class PayPal:
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal ({self.email})"

class Bitcoin:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin ({self.wallet_address})"


processor = PaymentProcessor()

credit_card = CreditCard("1234-5678-9012-3456")
paypal = PayPal("user@example.com")
bitcoin = Bitcoin("1A1z7agoat2oPYGyvVX9K")

print(processor.process_payment(credit_card, 100))
print(processor.process_payment(paypal, 50))
print(processor.process_payment(bitcoin, 75))

print("\n" + "="*50 + "\n")


class Animal:
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Snake(Animal):
    def make_sound(self):
        return "Hisss!"

class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def make_all_sounds(self):
        """Polymorphism - same method works for all animal types"""
        print("Zoo Sounds:")
        for animal in self.animals:
            print(f"  - {animal.make_sound()}")


zoo = Zoo()
zoo.add_animal(Lion())
zoo.add_animal(Snake())
zoo.add_animal(Elephant())
zoo.add_animal(Lion())

zoo.make_all_sounds()

print("\n" + "="*50 + "\n")


def show_details(obj):
    """Works with any object that has show method"""
    if hasattr(obj, 'show'):
        obj.show()
    else:
        print(f"{obj} doesn't have show method")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Person: {self.name}, Age: {self.age}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def show(self):
        print(f"Book: '{self.title}' by {self.author}")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show(self):
        print(f"Car: {self.brand} {self.model}")


print("Displaying different objects:")
show_details(Person("John", 30))
show_details(Book("Python 101", "Sarak"))
show_details(Car("Toyota", "Camry"))
