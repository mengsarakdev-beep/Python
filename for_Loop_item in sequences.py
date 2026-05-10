#for loop number
numbers=[1,4,2,5,3]
for num in numbers:
    print(num ** 2)
# for loop stringeach letter in a string , separated by a hyphen:
# 1 print 
str_words ="Pythonprogramming"
for letter in str_words:
    print(letter , end="-")
# 2 print only even numbers form a list:
numbers=[1,8,3,5,6,4]
for num in numbers:
    if num % 2 ==0:
        print(num)