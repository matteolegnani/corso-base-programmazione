Somma=0
N1= int(input("inserire il primo numero: "))
N2= int(input("inserire il secondo numero: "))
N3= int(input("inserire il terzo numero: "))
Somma= int((N1 + N2 + N3))
if (Somma > 10):
    if (N1 > N2 and N1 > N3):
        print("il numero più grande è il primo: ", N1)
    else:
        if (N2 > N1 and N2 > N3):
            print("il numero più grande è il secondo: ", N2)
        else:
            print("il numero più grande è il terzo: ", N3)
else:
    print("La somma dei tre numeri è ", Somma)