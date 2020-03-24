#Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

#C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

#Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

#dopóki fahr będą mniejsze niż 200 będzie działać
fahr = 0
while fahr <= 200:
    celc = 5 / 9 * (fahr - 32)
    celc = round(celc, 2)
    print(f'Temp {fahr} F to {celc}stC')
    fahr += 20
    #(aktualizujemy fahr co 20 stopni)
