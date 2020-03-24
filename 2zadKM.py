quote = ('Honesty is the first chapter in the book of wisdom ')

#Policz wszystkie znaki w napisie
długość = len(quote)
print('Długość ciągu to: ', długość)

#lub zapis
print(len(quote))

#Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])

#Wyświetl tylko pierwszą połowę tekstu
middle = len(quote) // 2
print(quote[0:middle])

#Wyświetl tylko kropkę
print(quote[-1])

#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[middle::3])

#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[middle::2])

#Wyświetl cały cytat odwrotnie
print(quote[::-1])

#Zamień wisdom na słowo friendship
print(quote.replace('wisdom', 'friendship'))

#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

palindrom = 'Kobyła ma mały bok'
palindrom = palindrom.replace("","")
palindrom == palindrom.lower()
print(palindrom)
print(palindrom == palindrom[::-1])


#Wyświetl cały cytat odwrotnie

#Zamień wisdom na słowo friendship

#Przekopiuj zawartość import this do zmiennej.
