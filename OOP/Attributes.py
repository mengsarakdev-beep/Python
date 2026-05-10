
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False

phone1 = Phone("Apple", "iPhone 15", 999)
phone2 = Phone("Samsung", "S24", 899)


print(f"Phone 1: {phone1.brand} {phone1.model} - ${phone1.price}")
print(f"Phone 2: {phone2.brand} {phone2.model} - ${phone2.price}")
print(f"Phone 1 is on: {phone1.is_on}")
print(f"Phone 2 is on: {phone2.is_on}")

print("\n" + "="*50 + "\n")


class Car:
    total_cars = 0
    wheels = 4
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        
        Car.total_cars += 1
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
        print(f"Wheels: {Car.wheels}")
        print(f"Speed: {self.speed} km/h")
        print(f"Total cars created: {Car.total_cars}\n")

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

car1.display_info()
car2.display_info()
car3.display_info()

print(f"Total cars: {Car.total_cars}")

print("\n" + "="*50 + "\n")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -${amount}")
        else:
            print("Insufficient funds")
    
    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Transaction History:")
        for transaction in self.transactions:
            print(f"  - {transaction}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(100)
account.show_details()

print("\n" + "="*50 + "\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
print(f"Initial: {person.name}, {person.age}")


person.email = "john@example.com"
person.phone = "123-456-7890"

print(f"After adding: {person.name}, {person.age}")
print(f"Email: {person.email}")
print(f"Phone: {person.phone}")


person.age = 31
print(f"Updated age: {person.age}")

print("\n" + "="*50 + "\n")


class Product:
    def __init__(self, name, price, quantity):
       
        self.name = name
 
        self.price = price
    
        self.quantity = quantity
       
        self.reviews = []
      
        self.stock_history = {}
     
        self.in_stock = quantity > 0
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def add_stock(self, quantity):
        self.quantity += quantity
        self.in_stock = True
    
    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"In Stock: {self.in_stock}")
        print(f"Reviews: {self.reviews}")

product = Product("Laptop", 999.99, 5)
product.add_review("Great quality!")
product.add_review("Fast delivery")
product.display_product()
