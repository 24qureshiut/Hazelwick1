count=0
while count < 8:
    height = int(input("Enter Your Height:"))
if height >= "140":
    print("You Can Ride")
    count= count+1
elif height < "140" and height >= "120":
    mk = input("Are You With An Adult. Yes Or No")
    if mk == "yes":
        print("Have a nice ride")
        count = count + 2
    else:
        print("You're not allowed to ride")
    count=count
    

    
