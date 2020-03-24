#Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

variable = ('ala ma kota a iwona psa')
print(variable)

length = len(variable)
print('Ilość znaków wynosi:', length)

if length >=5:
    print('Wprowadzone zdanie jest dłuższe niż 5 znaków')
else:
    print('Wprowadzone zdanie jest krótsze niż 5 znaków')


szukanea = variable.count('a')

if szukanea >= 1:
    substitution = variable.replace('a', 'z')
    print(substitution)
else:
    print('Nie wystąpił znak a')
