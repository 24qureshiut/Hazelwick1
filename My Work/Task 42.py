import random
number = random.randint(1,100)

while True:
    guess = int(input("Enter Your Number Guess: "))
    if guess == number:
        break
if guess > number:
    print("That's Higher Than The Number")
elif guess < number:
    print("That's Too Low")
elif guess > 100 or guess < 0:
    print("Only Between 1-100 Including")
else:
    print("That's Correct")