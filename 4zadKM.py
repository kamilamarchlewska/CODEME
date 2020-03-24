#Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki a oraz nieparzystych elementów z drugiej.

tuple_1 = ('a', 'b', 'c', 'd')
tuple_2 = (1, 2, 3, 4, 5, 6, 1, 1, 1, 1)

result = list(tuple_1[::2] + tuple_2[1::2])
result = set(result)
print(result)

#Utwórz listę lists_to_dict zawierającą listy 2 elementowe.
# Przekształć ją w słownik dict_from_list.

list_one = [('lion', 'giraffe')]
list_two = [('cat', 'dog')]

lists_to_dict = list_one + list_two
print(lists_to_dict)

dict_from_list = dict(lists_to_dict )
print(dict_from_list)

#Inny sposób
lista_par = [
    ['anna', 'wojtek'],
    ['iwona', 'stefan'],
    ['natalia', 'stanislaw']
]

lista_ost = dict(lista_par)
print(lista_ost)

for k, v in lista_ost.items():
    print(f'{k} - osoba towarzysząca: {v}')