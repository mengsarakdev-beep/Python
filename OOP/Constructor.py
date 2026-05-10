
class Student:
    def __init__(self, name, age, grade):
        print(f"Constructor called for {name}")
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 19, "B")

print(f"Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
print(f"Student 2: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")

print("\n" + "="*50 + "\n")
class Car:
    def __init__(self, brand, model, year=2024):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry")  
car2 = Car("Honda", "Civic", 2022)

print(f"Car 1: {car1.brand} {car1.model} ({car1.year})")
print(f"Car 2: {car2.brand} {car2.model} ({car2.year})")

print("\n" + "="*50 + "\n")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False
        self.reviews = []  

book1 = Book("Python 101", "John Doe", 300)
book1.reviews.append("Great book!")
book1.reviews.append("Very helpful")

print(f"Book: {book1.title}")
print(f"Author: {book1.author}")
print(f"Pages: {book1.pages}")
print(f"Read: {book1.is_read}")
print(f"Reviews: {book1.reviews}")

print("\n" + "="*50 + "\n")

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        
       
        if initial_balance < 0:
            print("Error: Balance cannot be negative!")
            self.balance = 0
        else:
            self.balance = initial_balance
        
        self.transactions = []
        self.transactions.append(f"Account created with balance: ${initial_balance}")

account = BankAccount("John Smith", 1000)
print(f"Account Holder: {account.account_holder}")
print(f"Balance: ${account.balance}")
print(f"Transaction History: {account.transactions}")


print("\nCreating account with negative balance:")
account2 = BankAccount("Jane Doe", -500)
print(f"Balance: ${account2.balance}")
