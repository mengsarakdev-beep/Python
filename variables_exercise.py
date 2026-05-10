# 1
name ="Your Name"
# 2 
a,b= 10,20
print(a+b)
# 3 
x, y = 5, 10
x, y = y, x

# 4
float_num=3.14

print(float_num)

# 5
is_active =True
print(is_active)

# 6
num = 10
num += 5
print(num)

# 7
PI =3.14159
PI =3 # python allows this but avoid modifying modifying constants

# 8 
value =None
value ="Now assigned"
print(value)

# 9
x = y = z =5

# 10
x, y, z =1,2,3

# 11
integer = 42
float_num = 3.14
string = "Text"
print(type (integer),type(float_num),type(string))

# 12
info= f"My name is {name}, and I am {25} year old."
print(info)
 
 # 13 
var =10
del var
#print(var) #will raise a NameError
  
# 14
name: str ="John"
age: int =30

# 15
a = b = 100
print(id(a), id (b))

# 16
expr_var =10*5

#17
#18
numbers= [1,2,3,4,5]
print(sum(numbers))

# 19
def my_function():
    local_var ="Hello"
#print(local_var) # will raise NameError

# 20 
global_var =10
def modify_global():
    global global_var
    global_var= 20 
modify_global()
print("global_var")


