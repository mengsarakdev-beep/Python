data=input("Enter a Number")
z1=3+2j
z2=3+2j
this=z1+z2
print(data,this)
def company():
    data1=int(input("Enter a Number1:"))
    data2=str(input("Enter a Numver2:"))
    total=data1+data2
    print("Result",total)
company() 
x1=2
x2=3
x3=4
x4=5
x5=6  
z1=complex(x1,x2) 
z2=complex(x3,x2)
z3=complex(x5,x1)
print(z1)
print(z2)
print(z3)

y=2+5j
print(y.imag)
print(y.real)
print(type(y))

a=2+5j
b=5+4j
print(a+b)

i=10
print(type(i))
i=input()
print(i)

#Us print statemetn to print words Hello, world 
print("\Hello world!")
print()#==\n

name = "Sopheap"
age=45
height=1.55
is_student=False

#print value tht story in those variable on the screen
print ("\nprint values that store within those variables")
print('name:',name)
print("Age :",age)
print("Height:",height)
print("IS student ",is_student)
print()

listt=[1,23,4,5]
listt[0]=5
print(listt)

y=5
y+=4
y+=3
y-=1
y*=2
print(y)
#basic operaction
#Assignment Operations
# == , += ,-= ,!= ,<= ,>= ,< ,>

#Amticment Operactions 
# -  + * / // = **

#logical operactions
# and or not

#memershop operaction 
# in not in

#string
name='hello'
del name[-1]
print(name)#error ,don't delete because it's string
#add update delect
#string manipulation
n='hello'
h=30
print(f"{n}{h}")
print(n,h)

#len ()
#upper() convert wrodest.
#lower() delete space
#replace()
#split()

word="hello world"
update=len(word)
print(update)

word=('hello world')#convert to uppercase
repare=word.upper()
print(repare)

#if statement
x=-5
if x>0:
    print("X is positive.")
else:
    print("X is non-positive.")

word="Hello world"
if 'H'==word[0]:
    print(word[1:])

x=int(input("INput value x="))
if x>0:
    print("X is positive")
elif x==0:
    print("X is Zero")
else:
    print("X is negative")
     
x=int(input("input x"))
y=int(input("input y"))
if x>0:
    print("X is positive") 
    if y>0:
        print("y is also positive")
    else:
        print("y is no positive")
else:
    print("X is not postive")

#Nested Conditional Statement
x=int(input("input x"))
y=int(input("input y"))
if x > 0:
    print("X is positive")
    if y>0:
        print("Y is also positive")
    else:
        print("Y is not positive")
        if y==0:
            print("Y is zoro")
        else:
            print("Y is negative")
else:
    print("X is not positive")
    if x==0:
        print("X is Zero")
    else:
        print('''X is
              negative''')

# 






    





















