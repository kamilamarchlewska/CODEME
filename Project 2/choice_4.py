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
        with open(filename, 'a+') as L: #saving links in common file
            L.write('\n' + linkAffiliate)

else:
    print('Invalid link provided.')
    print(54 * '-')
    print('')