# 1 -5 
print(type (42),type(3.14),type("Hello"),type(True),type(None))

# 6
print(float(42))

# 7
print(int(3.99))

# 8 
print(int(42))

# 9
print(list("text"))

# 10 
print(type({"key":"value"}))

# 11 - 13
print(type([1,2,3]),type((1,2,3)),type({1,2,3}))

# 14 
a = 5 
a = "text"

# 15
print(isinstance(42,int))

# 16
complex_num =3 + 4j
print(complex_num.real,complex_num.imag)

# 17
print(int (True))

# 18
mixed_list = [1,"text",3.14]

# 19
print(isinstance(42,int))

# 20
try:
    user_input = int (input ("Enter a number: "))
    print("It is a number!")
except ValueError:
    print("Not a number")