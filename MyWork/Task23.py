qadd = input("63+37=")
score=0
if qadd =="100":
    print("Correct")
    score = score +1
else:
    print("Wrong")
qsub = input("38-37=")
if qsub =="1":
    print("Correct")
    score = score +1
else:
    print("Wrong")
qmult = input("3*4=")
if qmult =="12":
    print("Correct")
    score = score +1
else:
    print("Wrong")
qdiv = input("55/5=")
if qdiv =="11":
    print("Correct")
    score= score +1
else:
    print("Wrong")

print("Your score is",score,"out of 4")

