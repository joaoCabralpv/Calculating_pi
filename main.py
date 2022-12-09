from math import gcd,sqrt
from random import randint

Cmethods = ["'1 - 1/3 + 1/5'", "co-prime"]

#1 - 1/3 + 1/5
def piOver4(p):
    pi = 0
    for i in range(p):
        j = i+1
        "plus or minus"
        por =  1 if j % 2 == 1 else -1
        pi += por/((2*j)-1)
    return 4*pi

# This function uses the euclids algorithm to find the greatest comon devisor.
#It is used on the co-prime method.


def coprime(pressision):
    total = presision
    coprime = 0
    for i in range(pressision):
        if gcd(randint(1,9999), randint(1,9999)) == 1:
            coprime +=1
    return  sqrt((6*total)/coprime)


for i in range(len(Cmethods)):
    iD = (str(i+1)+".")
    print(iD, Cmethods[i])
choise = int(input("Chose an option: "))
presision = int(input("Chose the number of iterations "))
if choise == 1:
    print(piOver4(presision))
elif choise == 2:
    print(coprime(presision))
else:
    print("invalid option")

