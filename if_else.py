# 1 check if a number is a positive or negative.
number =-5
if number >0:
    print("The number is a positive.")
else:
    print("The number is a negative.")
    
# 2 check if a number is even or odd.
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
# 3 check if a string is empty or not.
text = " "
if len(text) == 0:
    print("The sring is empty.")
else:
    print("The string is not empty.")
    
# 4 check if a number is divisible by 3.
if number % 3 == 0:
    print("The number is divisible by 3.")
else:
    print("The number is not divisible by 3.")

# 5 check is a variable is a boolean or not.
var = True
if isinstance(var,bool):
    print("The variable is a boolean.")
else:
    print("The variable is not a boolean.")
    
# 6 check if a string starts with a capital letter.
text = "Hello"
if text[0].isupper():
    print("The string starts with a capital letter.")
else:
    print("The string does not start with a capital letter.")
    
# 7 check if the length of a list is even or odd.
my_list=[1,2,3,4]
if len(my_list) % 2 == 0:
    print("The lenght of the list is even.")
else:
    print("The lenght of the list is odd.")
    
# 8 check if a number is prime or not.
num = 7
if num > 1 :
    for i in range(2, int (num ** 0.5)+1):
        if num % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is  prime.")
else:
    print("The number is  prime.")
    
# 9 check if a year is a leap year or not.
year=2025
if (year % 4 == 0 and year % 100 != 0) or (year % year == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
    
# 10 check if a number is in a list.
if 7 in my_list:
    print("The number is in the list.")
else:
    print("The number is not in the list.")
    
# 11 check is a number is greater than 10 0r not.
if number >10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")

# 12 check if two numbers are equal or not.
a,b=5,10
if a==b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# 13 check if a number is divisble by both 3 and 5.
if number % 3==0 and number % 5 ==0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
    
# 14 check if a string contains only alphabels.
text="Hello123"
if text.isalpha():
    print("The string contains only alphabels")
else:
    print("The string does not contain only alphabets.")
    
# 15 check if the first character of a string is uppercase or lowercase. 
if text[0].isupper():
    print("The first character is uppercase.")
else:
    print("The first character is lowercase.")
    
# 16 check if a string contains spaces or not.
text="NoSpacesHere"
if " " in text:
    print("The string contains spaces.")
else:
    print("The string does not contain spaces.")
    
#17 check if the absolute value of a number is greater than 10.
if abs(number)>10:
    print("The absolute value of the number is greater than 10.")   
else:
    print("The absolute value of the number is not greater than 10.") 

# 18 Check if the lengh of a string is exactly 8 characters.
text = "MyString"
if len(text)==8:
    print("The string has exactly 8 characters.")
else:
    print("The string does not have exactly 8 characters.")
    
# 19 check if a file path ends with '. txt'.
file_path = "example.txt"
if file_path.endswith(".txt"):
    print("The file path ends with .txt.")
else:
    print("The file path does not end with .txt.")
    
# 20 Check if the temperature is above or below freezing point.
temperature = -5
if temperature>=0:
    print("The temperature is above freezing point")
else:
    print("The temerature is below freezing point.")
    
    
    
    
    