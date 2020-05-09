def header():
    print('-' * 23)
    print('CATEGORIES'.center(23))
    print('1. HOME'.center(23))
    print('2. PRODUCT WEBSITE'.center(23))
    print('3. PROMOTION WEBSITE'.center(23))
    print('4. CATEGORY LINK'.center(23))
    print('-' * 23)
def typeLink():
        choice = input('For which category do you want to generate link? Provide number: ')

        if choice == '1':
            link = input('Provide link: ')

            verification = 'https://helion.pl'
            link = link[:17]
            if verification in link:
                idClient = input('Provide customer number: ')
                viewElement = '/view/'
                linkAffiliate = link + viewElement + idClient
                print(f'Generated link is: {linkAffiliate}')
                print('')

                linkRecord = input('Do you want to save the link in common file? YES/NO: ')
                linkRecord = linkRecord.upper()
                if linkRecord == 'YES':
                    filename = 'AffiliateLink.txt'
                    with open(filename, 'a+') as L:
                        L.write('\n' + linkAffiliate)
            else:
                print('Invalid link provided.')
                print(54 * '-')
                print('')

        elif choice == '2':
            link = input('Provide link: ')

            verification = 'https://helion.pl/ksiazki/'
            if verification in link:
                idClient = input('Provide customer number: ')
                viewElement = 'view/'
                partFirst = link[:18]
                partSecond = link[25:]

                linkAffiliate = partFirst + viewElement + idClient + partSecond
                print(f'Generated link is: {linkAffiliate}')
                print('')

                linkRecord = input('Do you want to save the link in common file? YES/NO: ')
                linkRecord = linkRecord.upper()
                if linkRecord == 'YES':
                    filename = 'AffiliateLink.txt'
                    with open(filename, 'a+') as L:
                        L.write('\n' + linkAffiliate)


            else:
                print('Invalid link provided.')
                print(54 * '-')
                print('')

        elif choice == '3':
            link = input('Provide link: ')

            verification = 'https://helion.pl/kategorie/promocja'
            if verification in link:
                idClient = input('Provide customer number: ')
                viewElement = '/page/'
                partFirst = link[:17]
                partSecond = link[27:]

                linkAffiliate = partFirst + viewElement + idClient + partSecond
                print(f'Generated link is: {linkAffiliate}')
                print('')

                linkRecord = input('Do you want to save the link in common file? YES/NO: ')
                linkRecord = linkRecord.upper()
                if linkRecord == 'YES':
                    filename = 'AffiliateLink.txt'
                    with open(filename, 'a+') as L:
                        L.write('\n' + linkAffiliate)


            else:
                print('Invalid link provided.')
                print(54 * '-')
                print('')


        elif choice == '4':
            link = input('Provide link: ')

            verification = 'https://helion.pl/kategorie'
            if verification in link:
                idClient = input('Provide customer number: ')
                viewElement = '/page/'
                partFirst = link[:17]
                partSecond = link[27:]

                linkAffiliate = partFirst + viewElement + idClient + partSecond
                print(f'Generated link is: {linkAffiliate}')
                print('')

                linkRecord = input('Do you want to save the link in common file? YES/NO: ')
                linkRecord = linkRecord.upper()
                if linkRecord == 'YES':
                    filename = 'AffiliateLink.txt'
                    with open(filename, 'a+') as L:
                        L.write('\n' + linkAffiliate)

            else:
                print('Invalid link provided.')
                print(54 * '-')
                print('')

        else:
            print('Invalid category number provided.')

header()
while True:
    typeLink()
    decision = input('Do you want to re-enter the link? YES/NO: ')
    print('-' * 57)
    decision = decision.upper()
    if decision == 'NO':
        summary = input('Do you want to display the contents of common files? YES/NO: ')
        summary = summary.upper()
        if summary == 'YES':
            try:
                filename = 'AffiliateLink.txt'
                with open(filename, 'r') as singleLink:
                    allLinks = singleLink.readlines()


                    for L in allLinks:
                        L = L.replace('\n', '')
                        print('► ' + L )
            except FileNotFoundError:
                print('No common files.')
            break