n1 = int(input("Inserisci il primo numero "))
n2 = int(input("Inserisci il secondo numero "))
operazione = int(input("Inserisci 1 per effettuare la somma, 2 per la sottrazzione, 3 per la divisione o 4 per la moltiplicazione: "))
if(operazione == 1):
    risultato = n1 + n2
if(operazione == 2):
    risultato = n1 - n2
if(operazione == 3):
    if(n2 == 0):
       risultato = str("Non puoi dividere per 0!")
    else:
        risultato = n1 / n2
if(operazione == 4):
    risultato = n1 * n2
if(operazione > 4):
    risultato = n1 + n2
print(risultato)