link = input('Provide link: ')

verification = 'https://helion.pl'
link = link[:17] # guaranteed use only https://helion.pl

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
        with open(filename, 'a+') as L: #saving links in common file
            L.write('\n' + linkAffiliate)

else:
    print('Invalid link provided.')
    print(54 * '-')
    print('')