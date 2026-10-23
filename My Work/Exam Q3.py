A=0
B=0
C=0
vote=-1

while vote!="End":
    vote=input("Enter Your Vote.A,B,C?:  ")
    if vote == "A":
        A=A+1
    elif vote == "B":
        B=B+1
    elif vote == "C":
        C=C+1

total=A+B+C
print("A=",A)
print("B=",B)
print("C=",C)
print("The Total Votes Are",total)