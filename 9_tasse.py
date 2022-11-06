guadagno=int(input("inserisci il guadagno"))
tasse=0
if(guadagno<10000):
    tasse=0
else:
    if(guadagno<30000):
        tasse=22/100*guadagno
    else:
        tasse:22/100*20000
        tasse=tasse=tasse+33/100*(guadagno-30000)
print("devi pagare le tasse:""tasse")

