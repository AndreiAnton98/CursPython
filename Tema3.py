import random
lista  = ['laptop', 'calculator', 'pix', 'mouse', 'tastatura', 'monitor', 'telefon', 'tableta', 'televizor']
cuvant = random.choice(lista)
vieti = 8
gasite = []
gasite.append(cuvant[0])
gasite.append(cuvant[len(cuvant) - 1])
output = ''
for litera in cuvant:
    if litera in gasite:
        output += litera
    else:
        output += '_'
winner = False
while vieti > 0:
    print(output)

    litera = input('Introduceti litera: ')
    if litera not in cuvant:
        vieti -= 1
    gasite.append(litera)
    output = ''
    for litera in cuvant:
        if litera in gasite:
            output += litera
        else:
            output += '_'

    print(f'{vieti} vieti ramase')
    if output == cuvant:
        print('You won')
        winner = True
        break
if not winner:
    print('You lost')


