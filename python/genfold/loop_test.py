A=1
B=1
C=1
a=10
b=3
c=5
while A==1:
    while True:
        if a>20:
            A=0
            break
        else:
            a=int(str(input("please enter a number a bigger than 20: ")))

    #while A==0 and B==1:
    if A==0:# and B==1:       
        if b>30 and a<40:
            B=0
        else:
            a=int(str(input("please enter a number a bigger than 20 and less than 40: ")))
            b=int(str(input("please enter a number b bigger than 30: ")))
            A=1

    #while A==0 and B==0 and C==1:
    if A==0 and B==0:# and C==1:
        if b<60 and a>25 and c>6:
            C=0
        else:
            A=1
            B=1
            a=int(str(input("please enter a number a bigger than 25 and less than 40: ")))
            b=int(str(input("please enter a number b bigger than 30 and less than 60: ")))
            c=int(str(input("please enter a number c bigger than 6: ")))

print("a,b,c", a,b,c)
