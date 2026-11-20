tmp = int(input("Enter The Temperature:"))

if tmp <0:
    print("Thats freezing")
elif 0 <= tmp <= 20:
    print("Thats Cold")
elif 21 <= tmp <= 30:
    print("That's Warm")
else:
    print("That's Hot")
