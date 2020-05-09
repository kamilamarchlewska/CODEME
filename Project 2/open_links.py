filename = 'AffiliateLink.txt'
with open(filename, 'r') as singleLink: # Read links from the file - AffiliateLink.txt 
    allLinks = singleLink.readlines()

    for line in allLinks: #displays links
        line = line.replace('\n', '')
        print('► ' + line)
