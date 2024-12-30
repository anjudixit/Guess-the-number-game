import random

target=random.randint(1,100)
n=5
while n>0:
    userChoice= input("Enter a number between 1 to 100 or Quit(Q): ")
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice== target) :
        print("Congratulations !, You guessed the correct number.")
        break
    elif(userChoice <target) :
        print("Your number is too small, take a bigger one.")
        n-=1
    else:
        print("Your number is too large, take a smaller one.")
        n-=1
if(n==0) :
        print("Sorry:( try again!")
print("<-----Game Over----->")