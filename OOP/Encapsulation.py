
class PublicExample:
    def __init__(self, name):
        self.name = name 

obj = PublicExample("John")
print(f"Public Name: {obj.name}")
obj.name = "Jane"
print(f"Modified Name: {obj.name}")

print("\n" + "="*50 + "\n")


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance  
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Public method to access balance"""
        return self._balance

account = BankAccount("Alice", 1000)
print(f"Initial Balance: ${account.get_balance()}")
account.deposit(500)
print(f"After Deposit: ${account.get_balance()}")


print(f"Direct access (bad practice): ${account._balance}")

print("\n" + "="*50 + "\n")


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.__student_id = student_id  
        self.__grades = [] 
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            return True
        return False
    
    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)
    
    def get_student_id(self):
        """Public method to safely access private data"""
        return self.__student_id
    
    def get_grades(self):
        """Public method to safely access grades"""
        return self.__grades.copy() 
student = Student("Bob", "S12345")
print(f"Student Name: {student.name}")
print(f"Student ID (via method): {student.get_student_id()}")

student.add_grade(85)
student.add_grade(90)
student.add_grade(88)

print(f"Grades: {student.get_grades()}")
print(f"Average: {student.get_average():.2f}")


try:
    print(f"Direct private access: {student.__student_id}")  
except AttributeError as e:
    print(f"Error: Private attribute cannot be accessed directly")
    print(f"(Actually stored as: _{Student.__name__}__student_id)")

print("\n" + "="*50 + "\n")


class Temperature:
    def __init__(self, celsius):
        self.__celsius = None
        self.set_celsius(celsius) 
    
    def set_celsius(self, value):
        """Setter with validation"""
        if isinstance(value, (int, float)):
            self.__celsius = value
        else:
            print("Temperature must be a number")
    
    def get_celsius(self):
        """Getter"""
        return self.__celsius
    
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32
    
    def get_kelvin(self):
        return self.__celsius + 273.15

temp = Temperature(25)
print(f"Celsius: {temp.get_celsius()}°C")
print(f"Fahrenheit: {temp.get_fahrenheit():.2f}°F")
print(f"Kelvin: {temp.get_kelvin():.2f}K")

temp.set_celsius(30)
print(f"\nUpdated Celsius: {temp.get_celsius()}°C")

# Invalid input
temp.set_celsius("invalid")

print("\n" + "="*50 + "\n")


class Circle:
    def __init__(self, radius):
        self.__radius = None
        self.set_radius(radius)  
    
    def set_radius(self, radius):
        """Setter with validation"""
        if radius > 0:
            self.__radius = radius
            return True
        else:
            print("Radius must be positive")
            return False
    
    def get_radius(self):
        """Getter"""
        return self.__radius
    
    def get_area(self):
        """Calculate area"""
        return 3.14159 * (self.__radius ** 2)
    
    def get_circumference(self):
        """Calculate circumference"""
        return 2 * 3.14159 * self.__radius

circle = Circle(5)
print(f"Radius: {circle.get_radius()}")
print(f"Area: {circle.get_area():.2f}")
print(f"Circumference: {circle.get_circumference():.2f}")

print(f"\nSetting new radius:")
if circle.set_radius(7):
    print(f"New Radius: {circle.get_radius()}")
    print(f"New Area: {circle.get_area():.2f}")

print(f"\nTrying invalid radius:")
if not circle.set_radius(-3):
    print(f"Radius remains: {circle.get_radius()}")
