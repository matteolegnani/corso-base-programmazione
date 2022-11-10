n=0
n_finale=0
while True:
    n=int(input("inserire un numero: "))
    if(n%2 == 0):
        print("il numero è pari")
    else:
        print("il numero è dispari")
    if(n==n_finale*2):
        break
    else:
        n_finale = n