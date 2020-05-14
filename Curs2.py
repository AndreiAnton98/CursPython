# cuvant = 'abcde'
# print(cuvant[6])  # daca nu exista 6 da eroare, daca folosesc slicing: nu mai da eroare
# print(cuvant[-1])  # pt a lua ultimu index
#
# for letter in cuvant:
#     print(letter)
#
# cuvant.replace('d', 'f')  # schimb d in f    trebuie salvat in cuvant
#
# # variante de gasit un caract in cuvant
# if 'b' in cuvant:
#     pass
#
# print("".join(cuvant.split('c')))
#
# # tupluri
# tuplu = (1,)  # aici type este int, trebuie sa aiba macar o , ca sa isi dea seama ca e tuplu
# tuplu = tuplu + (2, 3, 5)  # concatenare
# # tuplul are indexare, merge concatenarea
# # valorile din tupluri nu se pot schimba, immutable


# exemplu = "abcde"
# print(exemplu.find('c'))  # returneaza indexul


# liste  este un tuplu doar ca se poate modifica
x = [True, 1, '4']
x[1] = 'a'
x.append(5)
x = [1, 2, [3, 4, 5]]
print(x[::-1])  # pt a printa lista invers

# setul nu are elemente duple
# elementele sunt ordonate
# nu ai index
# se adauga cu add

# dictionar
a = {1: '35', 2: '123'}
# se sterge cu del