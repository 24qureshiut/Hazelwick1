hours=-1
total=0

while hours != 0:
    hours = int(input("Enter How Many Hours Did You Park Your Car?  "))
    choice = input("Is Your Car Electric, Yes Or No?  ")
    if choice == "yes":
        total = hours*2
    elif choice == "no":
        total = hours*4
    print("Your Price Is",total) 