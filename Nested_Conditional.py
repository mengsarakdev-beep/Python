# 1. Check if a number is positive and even.
number = 12 
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive but odd")
        
# 2. Check if a number is negative and divisible by 3.
number = -9
if number < 0:
    if number % 3 == 0 :
        print("The number is negative and divisible by 3.")
    else:
        print("The number is negative but not divisible by 3.")
else:
    print("The numbeer is not negative.")
    
# 3. Check if a year is a leap year and divisible by 100.
year = 2000 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if year % 100 == 0:
        print("The year is a leap year and divisble by 100.")
    else:
        print("The year is a leap year but not divisible by 100.")
else:
    print("The year is not  leap year.")
    
# 4. Check if a string starts with "A" and ends with "Z".
text = "AmaaingZ"
if text.startswith("A"):
    if text.endswith("Z"):
        print("The string starts with 'A' and ends with 'Z'.")
    else:
        print("The string starts with 'A' but does not end with 'Z'.")
else:
    print("The string does not start with 'A'.")
    
# 5. Check if a number is even and greater than 50.
number = 52 
if number % 2 == 0:
    if number > 50:
        print("The number is even and greater than 50.")
    else:
        print("The number is even but not greater than 50")
else:
    print("The number is not even.")
        
# 6. Check if a variable is not None and is of type str.
var = "Hello"
if var is not None:
    if isinstance(var,str):
        print("The variable is not None and is a string.")
    else:
        print("The variable is not None but is not a string.")
else:
    print("The variable is None.")
    
# 7. Check if a string length is greater than 10 and contains the word "Python".
text = "Ilove python programming."
if len(text) > 10:
    if "python" in text:
        print("The string lenggth is greater than 10 and contains 'Python'.")
    else:
        print("The string length is greater than 10 but does not does not contain 'Python'.")
else:
    print("The string lenght is not greater than 10.")
    
# 8. Check if a list is not empty and has more than 5 elements.
my_list = [1,2,3,4,5,6]
if my_list:
    if len(my_list) > 5:
        print("The list is not empty and has ore than 5 elements.")
    else:
        print("The list is not empty but has 5 or fewer elements.")
else: 
    print("The list is empty.")
# 9. Check if a number is divisible by 2, 3, and 5.
number = 30
if number % 2 == 0:
    if number % 3 == 0:
        if number % 5 == 0:
            print("The number is divisible by 2 , 3 ,and 5.")
        else:
            print("The number is divisable by 2.")

    # 10. Check if a person is eligible to vote based on age and citizenship.
age = 20
citizenship = "USA"
if age >= 18:
    if citizenship == "USA":
        print("The person is eligible to vote.")
    else:
        print("The person is not a citizen.")
else:
    print("The person is not old enough to vote.")

# 11. Check if a student passed both Math and Science exams.
math_score, science_score = 75, 85
if math_score >= 50:
    if science_score >= 50:
        print("The student passed both Math and Science.")
    else:
        print("The student passed Math but failed Science.")
else:
    print("The student failed Math.")

# 12. Check if a person is eligible for a senior discount (age > 60) and a loyalty program.
age = 65
loyalty = True
if age >= 60:
    if loyalty:
        print("The person is eligible for a senior discount and loyalty program.")
    else:
        print("The person is eligible for a senior discount but not loyalty program.")
else:
    print("The person is not eligible for a senior discount.")

# 13. Check if a file path ends with '.py' and starts with 'project_'.
file_path = "project_main.py"
if file_path.endswith(".py"):
    if file_path.startswith("project_"):
        print("The file path ends with '.py' and starts with 'project_'.")
    else:
        print("The file path ends with '.py' but does not start with 'project_'.")
else:
    print("The file path does not end with '.py'.")

# 14. Check if a triangle is equilateral and right-angled.
a, b, c = 3, 4, 5
if a == b == c:
    print("The triangle is equilateral.")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is neither equilateral nor right-angled.")

# 15. Check if a string contains uppercase letters and digits.
text = "Hello123"
if any(char.isupper() for char in text):
    if any(char.isdigit() for char in text):
        print("The string contains both uppercase letters and digits.")
    else:
        print("The string contains uppercase letters but no digits.")
else:
    print("The string does not contain uppercase letters.")

# 16. Check if a dictionary has a specific key and value.
my_dict = {"name": "John", "age": 30}
if "name" in my_dict:
    if my_dict["name"] == "John":
        print("The dictionary has the key 'name' with value 'John'.")
    else:
        print("The dictionary has the key 'name' but with a different value.")
else:
    print("The dictionary does not have the key 'name'.")

# 17. Check if a number is odd and within the range 1-100.
number = 35
if number % 2 != 0:
    if 1 <= number <= 100:
        print("The number is odd and within the range 1-100.")
    else:
        print("The number is odd but not within the range 1-100.")
else:
    print("The number is not odd.")

# 18. Check if a string starts with "H", contains "e", and ends with "o".
text = "Hello"
if text.startswith("H"):
    if "e" in text:
        if text.endswith("o"):
            print("The string starts with 'H', contains 'e', and ends with 'o'.")
        else:
            print("The string starts with 'H' and contains 'e' but does not end with 'o'.")
    else:
        print("The string starts with 'H' but does not contain 'e'.")
else:
    print("The string does not start with 'H'.")

# 19. Check if a tuple contains exactly 3 elements, all integers.
my_tuple = (1, 2, 3)
if len(my_tuple) == 3:
    if all(isinstance(x, int) for x in my_tuple):
        print("The tuple contains exactly 3 elements, all integers.")
    else:
        print("The tuple contains 3 elements but not all are integers.")
else:
    print("The tuple does not contain exactly 3 elements.")

# 20. Check if a number is divisible by 4 and not divisible by 8.
number = 12
if number % 4 == 0:
    if number % 8 != 0:
        print("The number is divisible by 4 and not divisible by 8.")
    else:
        print("The number is divisible by 4 and also divisible by 8.")
else:
    print("The number is not divisible by 4.")
    