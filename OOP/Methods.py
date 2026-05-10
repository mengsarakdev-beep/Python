
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """Method to deposit money"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Method to withdraw money"""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Withdrawal amount must be positive")
    
    def check_balance(self):
        """Method to check current balance"""
        print(f"Current balance: ${self.balance}")

account = BankAccount("123456", 1000)
account.check_balance()
account.deposit(500)
account.check_balance()
account.withdraw(200)
account.check_balance()

print("\n" + "="*50 + "\n")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        """Convert Celsius to Fahrenheit"""
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        """Convert Celsius to Kelvin"""
        return self.celsius + 273.15
    
    def get_info(self):
        """Return temperature in all scales"""
        return {
            "Celsius": self.celsius,
            "Fahrenheit": self.to_fahrenheit(),
            "Kelvin": self.to_kelvin()
        }

temp = Temperature(25)
print(f"25°C = {temp.to_fahrenheit()}°F")
print(f"25°C = {temp.to_kelvin()}K")
print(f"Temperature Info: {temp.get_info()}")

print("\n" + "="*50 + "\n")

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100")
    
    def calculate_average(self):
        """Calculate average grade"""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """Get letter grade based on average"""
        average = self.calculate_average()  
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def display_report(self):
        """Display student report"""
        avg = self.calculate_average()
        letter = self.get_letter_grade()
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f}")
        print(f"Letter Grade: {letter}")

student = Student("John")
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)
student.display_report()

print("\n" + "="*50 + "\n")

class MathOperations:
    pi = 3.14159  
    
    def __init__(self, name):
        self.name = name
    
    def instance_method(self):
        """Regular instance method - uses self"""
        return f"This is an instance method in {self.name}"
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need self"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Static method - doesn't need self"""
        return a - b
    
    @classmethod
    def from_string(cls, string_data):
        """Class method - receives class as parameter"""
        name = string_data.split()[0]
        return cls(name)

math_obj = MathOperations("Calculator")
print(math_obj.instance_method())


print(f"10 + 5 = {MathOperations.add(10, 5)}")
print(f"10 - 5 = {MathOperations.subtract(10, 5)}")

new_obj = MathOperations.from_string("MyCalculator Data")
print(f"Created from string: {new_obj.name}")
