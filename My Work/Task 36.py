total = 0
import random
number = random.randint(1,100)
Guess=-1


while Guess != number and total < 10:
    Guess = int(input("Enter Number From 1-100 Including:"))
    total +=1

    if Guess < 1 or Guess > 100:
             print("Enter A Number Between 1-100")

    elif Guess < number:
           print("Too Low")

    elif Guess > number:
           print("Too high")

    else:
           print("You Win Well Done")

if Guess != number:
       print("You Lost. The Number Was", number)




