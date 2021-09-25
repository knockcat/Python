import random

target = random.randrange(10,20)

guess = int(input("Guess the number : "))

if( target == guess):
    print("Number : ",target)
    print("Better You Win")

else:
    print("Number : ",target)
    print("Better Luck Next Time")
