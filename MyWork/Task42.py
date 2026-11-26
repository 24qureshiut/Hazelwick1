import random
number = random.randint(1,100)
count = 0

while True:
    guess = int(input("Enter Your Number Guess: "))
    if guess == number:
        print("Correct, The Number Was", number)
        break
    elif guess > 100 or guess < 0:
        print("A Number Between 1 And 100")
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")

