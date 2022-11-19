n1=0
n2=0
operazione=0
n1=int(input("inserisci 2 numeri: "))
n2=int(input("inserisci 2 numeri: "))
operazione=int(input("inserisci l'operazione da svolgere: "))
if(operazione==1):
    print(n1+n2)
if(operazione==2):
    print(n1-n2)
if(operazione==3):
    if(n2==0):
        print("non puoi dividere per zero")
    else:
        print(n1/n2)
if(operazione==4):
    print(n1*n2)
    