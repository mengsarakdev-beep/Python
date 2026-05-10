count=0
while count < 5:
    print(count)
    count+=1
#1 prompt theuser for a umber ,then print all number form 1 up to tht number :
number =int(input ("input number :"))  
count=1
while count<=number:
    print(count) 
    count+=1
#2 create a progream that simulates a guessing game;
secret_number=570
guess = int (input ("Guess a number:"))
while guess != secret_number:
    if guess <secret_number:
        print("Too low!! Try again.")
    else:
        print("Too high! Try again.")
    guess = int (input ("Guess a number:"))
print("You guessed it!")