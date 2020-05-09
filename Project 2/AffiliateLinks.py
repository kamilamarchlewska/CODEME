
def typeLink():
        choice = input('For which category do you want to generate link? Provide number: ')

        if choice == '1':
            import choice_1 #there is a script - choice_1 module

        elif choice == '2':
            import choice_2 #there is a script - choice_2 module

        elif choice == '3':
            import choice_3 #there is a script - choice_3 module


        elif choice == '4':
            import choice_4 #there is a script - choice_4 module

        else:
            print('Invalid category number provided.')

import categories #there is a script - user selection menu

while True:
    typeLink() #generator mechanics

    decision = input('Do you want to re-enter the link? YES/NO: ')
    print('-' * 57)
    decision = decision.upper()
    if decision == 'NO':
        summary = input('Do you want to display the contents of common files? YES/NO: ')
        summary = summary.upper()
        if summary == 'YES':
            try:
                import open_links #the module opens common files
                break

            except FileNotFoundError:
                print('No common files.')

        else:
            break