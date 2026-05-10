# 1 . check if a number is positive.
number =10
if number==10:
    print(" The number is positive")

# 2 . check if a number is even .
if number % 2 == 0:
    print("The number is even .")
    
# 3 . check if a number is divisible by 5.
if number % 5==0:
    print("The number is divisible by 5.")
    
# 4 . check if a string starts with A.
text='Apple'
if text.startswith('A'):
    print("The string starts with 'A'.")

# 5 check if a variable is greater then 100.
value = 150
if value>100:
    print("The vlue is greater than 100.")
    
# 6 check if a lsit contains more then 5 elements.
my_list =[1,2,3,4,5,6]
if len(my_list) > 5:
    print("The lsit contains more then 5 elements")

# 7 check if a variable is of type int .
var=42
if isinstance(var,int):
    print("The variable is of type integer.")
    
# 8 check if a given character,is a vowel.
char='e'
if char in 'aeiouAEIOU':
    print("The character is a vowel.")
    
# 9 check if a year is a leap year.
year= 2024
if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
    print("The year is a leap year.")
    
# 10 check if a number is a multiple of 10.
if number % 10==0:
    print("The number is a multiple of 10")
    
# 11 check if a string contains the word "Python".
sentence="I love python programming."
if "python" in sentence:
    print("The string contains the word Python.")
    
# 12 check if a number is within the range 1 to 100.
num=50
if 1<= num <= 100:
    print("The number is within the range 1 to 100.")
    
# 13 check if a tuple is empty.
my_tuple=()
if not my_tuple:
    print("The tuple is empty.")
    
# 14 check if a dictionary has a specific key.
my_dict={"name":"John","age":30}
if "name" in my_dict:
    print("The dictionary has the key 'name'.")
    
# 15 Check if a number is negative.
if number < 0:
    print("The numbere is negative.")

# 16 check if a string lenght is greater than 5.
if len(text)>5:
    print("The string lenght is greater than 5.")

# 17 check if the sum of two numbers is greater than 50.
a,b =30,25
if a+b>50:
    print("The sum of two numbers is greater than 50.")
    
# 18 check if a list contains the number 7.
if 7 in my_list:
    print("The list contains the number 7.")
    
#19 check if a variable is not 'None'.
variable="Hello"
if variable is not None:
    print("The variable is not 'None'")
    
# 20 check if a string ends with a period( ' . ' ).
sentence="I love python programming."
if sentence.endswith("."):
    print("The string ends with a period.")