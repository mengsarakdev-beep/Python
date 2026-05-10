# VlaueError
try:
    name =int(input ("User input your name."))
except ValueError:
    print("Invalid input! place enter a string.")
    
# SyntaxError
try:
    if True
        pass
except SyntaxError:
    print("Error: Syntax incroect!")
    
#ZeroDivisionError
try:
    number=10/0 #note % / //
except ZeroDivisionError:
    print("Cannot devide by Zero.")
    
#NameError
try:
    print(name)
except NameError:
    print("Error name is not definde!")

#TypeError
try:
    num=3+'3'
except TypeError:
    print("Cannot concatenate str and int")
    
#IndexError
try:
    My_list=[1,2,3,4,5]
    print(My_list[5])
except IndexError:
    print("Index 5 no in list.")
    
#FileNotFoundError
try:
    with open ("nonexistent_file.txt",'r') as f:
        data=f.read()
except FileNotFoundError:
    print("file does not exist.")

# Custom Exception
class CustomError(Exception): 
    """A custom exception class.""" 
    pass
try: 
    raise CustomError("An error occurred.") 
except CustomError as e: 
    print(f"Caught an exception: {e}")
    
    