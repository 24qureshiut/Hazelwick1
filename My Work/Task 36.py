total = 0
import random
number = random.randint(1,100)

Guess = int(input("Enter Number From 1-100 Including:"))

while Guess != number:
    if number > Guess:
             print("Too Low")
    else:
           print("Too High")
    count =+ 1
    Guess = int(input("Enter Number From 1-100 Including:"))
    print("You guessed correct")




