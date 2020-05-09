import json
import random

def hangman(text):
    secret = text

    characters = list(secret)
    for i in range(len(secret)):
        characters[i] = '_'

    life = len(secret) + 2
    print('')
    lista = []

    while life > 0:
        print(f'You have {life} trial.')
        print(' '.join(characters))

        print(f'Given letters | {lista} |')
        letter = input('Enter the letter:')
        letter.lower()
        letterGood = letter.isalpha()
        if letterGood == True:
            if letter in lista:
                print('Given identical letter.')
                print('-' * 23)
            else:
                lista.append(letter)
                if letter in secret:
                    for i in range(len(secret)):
                        if secret[i] == letter:
                            characters[i] = letter
                            life -= 1
                            a = characters.count('_')

                            if a == 0:
                                print(f'Password: {secret}. ')
                                print('Victory!')
                                life -= 100

                            elif characters[i] == secret:
                                print('Victory!')
                                break

                    if letter == secret:
                        print('Victory!')
                        break

                else:
                    life -= 1
        else:
            print('Invalid letter given.')
            print('-' * 22)
    if life == 0:
        print('Defeat!')
        import module_rita
        print(f'\u001b[30mPassword: {secret}. ')

def choice_category():
    if int(category) == 1:
        flowerChoice = random.choice(data['1. FLOWERS'])
        hangman(flowerChoice)

    elif int(category) == 2:
        fruitChoice = random.choice(data['2. FRUITS'])
        hangman(fruitChoice)

    elif int(category) == 3:
        vegetableChoice = random.choice(data['3. VEGETABLES'])
        hangman(vegetableChoice)

    elif int(category) == 4:
        animalChoice = random.choice(data['4. ANIMALS'])
        hangman(animalChoice)

    else:
        print('Wrong choice')

def header_hangman():
    width = 24
    print('|      CATEGORIES:    |')
    print('.' * width)
    for i in dict_categories:
        print(i.center(width))

    print('.' * width)
    print('')

filename = 'hangman.json'
with open(filename, 'r') as f:
  data = json.loads(f.read())

dict_categories = data.keys()

header_hangman()

category = input('Provide category number: ')
categoryGood = category.isdigit()
if categoryGood == True:
    choice_category()
else:
    print('Invalid category number provided.')
