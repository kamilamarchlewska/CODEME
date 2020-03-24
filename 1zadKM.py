#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# #Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

a = float(input("Proszę o podanie dystansu który zostanie pokonany ( km ) : "))
b = int(input("Proszę o podanie wartości spalania na 100k ( l ): "))
c = int(input("Proszę o podanie ceny litra benzyny ( PLN ): "))

print("Dziękuję. Podane dane to: ", a, 'km ', b, 'l ', c, 'PLN ')

burning_car = c * a/100 * b

print('Koszt wyprawy wyniesie: ', round(burning_car, 2), 'PLN')
