Days = int(input("Enter How Many Days You Have Your Weather Reading's For: "))
total = 0
highest = 0
frostydays = 0

for i in range(1,Days+1):
    print("Day", i)
    tmped = float(input("Enter Temperature: "))
    total += tmped
    if tmped > highest:
        highest = tmped
    elif tmped < 0:
        frostydays += 1

average = total/Days
print("Your Average Temperature Is", average)
print("You Had", frostydays," frostydays")
print("Your Highest Temperature Is", highest)