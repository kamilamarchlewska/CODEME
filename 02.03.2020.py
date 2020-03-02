waga=int(input('Ile wynosi twoja waga (kg)?'))
wzrost=float(input('Ile wynosi Twój wzrost (m)?'))

wynik = waga / (wzrost ** 2)

print('Twoje BMI wynosi:', round(wynik))