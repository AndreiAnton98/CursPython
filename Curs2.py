cuvant = 'abcde'
print(cuvant[6])  # daca nu exista 6 da eroare, daca folosesc slicing: nu mai da eroare
print(cuvant[-1])  # pt a lua ultimu index

for letter in cuvant:
    print(letter)

cuvant.replace('d', 'f')  # schimb d in f    trebuie salvat in cuvant

# variante de gasit un caract in cuvant
if 'b' in cuvant:
    pass

print("".join(cuvant.split('c')))

# tupluri
tuplu = (1,)  # aici type este int, trebuie sa aiba macar o , ca sa isi dea seama ca e tuplu
tuplu = tuplu + (2, 3, 5)  # concatenare
# tuplul are indexare, merge concatenarea
# valorile din tupluri nu se pot schimba, immutable
