Cmethods = ["'1 - 1/3 + 1/5'"]

#1 - 1/3! + 1/5!
def one(p):
    pi = 0
    for i in range(p):
        j = i+1
        "plus or minus"
        por =  1 if j % 2 == 1 else -1
        pi += por/((2*j)-1)
    return 4*pi

for i in range(len(Cmethods)):
    iD = (str(i+1)+".")
    print(iD, Cmethods[i])
choise = int(input("Chose an option: "))
presision = int(input("Chose the number of iterations "))
if choise == 1:
    print(one(presision))
else:
    print("invalid option")

