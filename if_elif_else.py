# 1. Check if a number is positive, negative, or zero.
number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# 2. Check if a number is small (<10), medium (10–100), or large (>100).
number =55
if number < 10 :
    print("The number is small.")
elif 10 <= number <= 100:
    print("The number is medium.") 
else:
    print("The number is large.")
    
# 3. Grade a student based on their score (A, B, C, D, F).
score = 85
if score >= 90:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade : D")
else:
    print("Grade F")
    
# 4. Check the season based on the month number.
month = 7
if month in [12,1,2]:
    print("Season: winter")
elif month in [3,4,5]:
    print("Season: Spring")
elif month in [6,7,8]:
    print("Season: Summer")
else:
    print("Season: Autumn")
    
# 5. Determine if a person is a child, teenager, adult, or senior.
age = 25 
if age < 13 :
    print("Child")
elif 13 <= age <20:
    print("Teenager")
elif 20 <= age < 60:
    print("Adult")
else:
    print("Senior")
    
# 6. Determine if a day is a weekday or weekend.
day = "Saturday"
if day in ["Monday","Tuesday","Wednesday","Thursday","Friday"]:
    print("Weekday")
elif day in ["Saturday","Sunday"]:
    print("Weekday")
else:
    print("Invalid day")
    
# 7. Check if a year is ancient (<1900), modern (1900–2000), or recent (>2000).
year = 1995
if year <1900:
    print("Ancient")
elif 1900 <= year <= 2000:
    print("Medern")
else:
    print("Recent")

# 8. Determine if a string is short, medium, or long based on its length.
text ="Hello"
if len(text)<5:
    print("short")
elif 5<= len(text)<=10:
    print("Medium")
else:
    print("Long")
    
# 9. Classify a number as even, odd, or zero.
number =0
if number == 0:
    print("The number is zero.")
elif number % 2 ==0:
    print("The number is even.")
else:
    print("The numberr is odd.")
    
# 10. Determine the price category based on product cost.
price=75
if price <20 :
    print("Cheap")
elif 20<=price<=100:
    print("Affordable")
else:
    print("Expensive")
    
# 11. Classify an angle as acute, right, obtuse, or straight.
angle = 90 
if angle < 90 :
    print("Acute nagle")
elif angle ==90:
    print("Right angle")
elif 90 <angle <180:
    print("Obtuse angle")
else:
    print("Straight angle")
    
# 12. Classify a triangle based on side lengths.
a,b,c=3,4,5
if a == b == c:
    print("Equilateral triangle")
elif a == b or b== c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
# 13. Check if a character is a vowel, consonant, or other.
char ="e"
if char .lower() in "aeiou":
    print("Value")
elif char .isalpha():
    print("Consonant")
else:
    print("Other")
    
# 14. Check if a number is a single digit, double digit, or larger.
number =45 
if 0<=number <10:
    print("Single digit")
elif 10 <=number <100:
    print("Double digit")
else:
    print("Larger thn double digit")
    
# 15. Determine a traffic light color's action (red, yellow, green).
light ="green"
if light.lower() == "red":
    print("stop")
elif light.lower()=="yellow":
    print("Caution")
elif light.lower() =="green":
    print("Go")
else:
    print("Invalid light color")
    
# 16. Classify a temperature as cold, warm, or hot.
tempeerature =25
if tempeerature <15:
    print("Cold")
elif 15 <= tempeerature <= 30:
    print("Hot")
    
# 17. Determine a student's result: pass, merit, or distinction.
marks = 78 
if marks < 50:
    print("Fail")
elif 50 <= marks <75:
    print("Pass")
elif 75 <= marks <90:
    print("Merit")
else:
    print("Distinction")
    
# 18. Classify an animal as mammal, bird, or reptile.
animal ="parrot"
if animal in ["dog", "cat", "human"]:
    print("Mammal")
elif animal in ["eagle","parrot","penguin"]:
    print("Bird")
elif animal in ["snake", "lizard","turtle"]:
    print("Reptile")
else:
    print("Unknow category")
    
# 19. Determine if a vehicle is a bike, car, or truck.
vehicle = "bike"
if vehicle == "bike":
    print("Two - wheeler")
elif vehicle == "car":
    print("Four-wheeler")
elif vehicle == "truck":
    print("Heavy vehicle")
else:
    print("Unknow vehicle type")

# 20. Classify a sports player as beginner, intermediate, or advanced
experience = 3
if experience < 1:
    print("Beginner")
elif 1 <= experience <= 3:
    print("Intermediate")
else:
    print("Advanced")
    