score = 0
import random
number1 = random.randint(0,100)
number2 = random.randint(0,100)
number3 = random.randint(0,100)
number4 = random.randint(0,100)
number5 = random.randint(0,100)
GenNumber = int(input("My Game Is Pretty Simple, There Are 5 Numbers Randomized From 1-100 Including Them. You Have To Guess Them. Enter Your First Number: "))
if GenNumber == number1:
    print("That Was Correct")
    score = score + 10
elif abs(GenNumber-number1) <= 5:
    print("Close")
    score = score+5
elif abs(GenNumber-number1) <= 10:
    print("Away")
    score = score + 3
elif abs(GenNumber-number1) <= 20:
    print("Far")
    score = score + 2
elif abs(GenNumber-number1) <= 50:
    print("Way Off")
    score = score + 1
print("The Number Was", number1 )

GenNumber2 = int(input("Round 2, Enter Your Second Number:"))
if GenNumber2 == number1:
    print("That Was Correct")
    score = score + 10
elif abs(GenNumber2-number2) <= 5:
    print("Close")
    score = score+5
elif abs(GenNumber2-number2) <= 10:
    print("Away")
    score = score + 3
elif abs(GenNumber2-number2) <= 20:
    print("Far")
    score = score + 2
elif abs(GenNumber2-number2) <= 50:
    print("Way Off")
    score = score + 1
print("The Number Was", number2 )

GenNumber3 = int(input("Round 3, Enter Your Guess:"))
if GenNumber3 == number3:
    print("That Was Correct")
    score = score + 10
elif abs(GenNumber3-number3) <= 5:
    print("Close")
    score = score+5
elif abs(GenNumber3-number3) <= 10:
    print("Away")
    score = score + 3
elif abs(GenNumber3-number3) <= 20:
    print("Far")
    score = score + 2
elif abs(GenNumber3-number3) <= 50:
    print("Way Off")
    score = score + 1
print("The Number Was", number3 )

GenNumber4 = int(input("Round 4, Enter Your Second To Final Guess:"))
if GenNumber4 == number4:
    print("That Was Correct")
    score = score + 10
elif abs(GenNumber4-number4) <= 5:
    print("Close")
    score = score+5
elif abs(GenNumber4-number4) <= 10:
    print("Away")
    score = score + 3
elif abs(GenNumber4-number4) <= 20:
    print("Far")
    score = score + 2
elif abs(GenNumber4-number4) <= 50:
    print("Way Off")
    score = score + 1
print("The Number Was", number4 )

GenNumber5 = int(input("Enter Your Final Number:"))
if GenNumber5 == number5:
    print("That Was Correct")
    score = score + 10
elif abs(GenNumber5-number5) <= 5:
    print("Close")
    score = score+5
elif abs(GenNumber5-number5) <= 10:
    print("Away")
    score = score + 3
elif abs(GenNumber5-number5) <= 20:
    print("Far")
    score = score + 2
elif abs(GenNumber5-number5) <= 50:
    print("Way Off")
    score = score + 1
print("The Number Was", number5 )

print("Your Score Is", score)




