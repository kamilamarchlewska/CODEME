names = ['Ada', 'Julia', 'Ruby']

for step in range(3):
    print(step, ' : ' + names[step])
    #lub zamiast przecinka rzutowanie int(step)

pa = ''
magic = 'hokuspokus'
for num in range (2, 10, 2) :
    pa = pa + str(num) + magic[num]
    print(pa)