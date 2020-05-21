import random
lista  = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
cuvant = random.choice(lista)
lives = 8
winner = False
while lives > 0:
    input_ = input("Introduceti cuvantul ")
    if input_ == cuvant:
        print('You won')
        winner = True
        break
    else:
        lives -= 1
        print(f'Wrong! {lives} remaining')
if not winner:
    print('You lost')

