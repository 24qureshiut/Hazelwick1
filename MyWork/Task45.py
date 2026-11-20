import random
num = random.randint(1,100)

for count in range(10):
    guess = int(input("Enter Your Guess: "))
    if guess > 100 or guess > 101:
        print("A number between 1-100")
    elif guess > num:
        print("Too High")
    elif guess < num:
        print("That's Too Low")
    elif guess == num:
            print("That's Correct") 
            break
else:
    print("Out of attempts! The Number Is", num)

