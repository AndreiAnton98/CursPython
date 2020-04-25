# #Ex1
# nume = input("Introduceti numele:")
# while True:
#     text = input("Introduceti text:")
#     if text == 'exit':
#         print("iesire din program")
#         break
#     elif text.isdigit():
#         print("Sirul de numere a fost gasit de", nume)
#     else:
#         print("Sirul de caractere a fost gasit de", nume)



# #Ex2:
# while True:
#     numar = input("Introduceti numarul: ")
#     if numar == 'exit':
#         print("Iesire din program")
#         break
#     elif len(numar) == 0:
#         continue
#     elif numar.isdigit() or numar[1:].isdigit():
#         numar = int(numar)
#         if numar % 2 == 0:
#             print("Numar par")
#         else:
#             print("Numar impar")
#     else:
#         print("Numar incorect")

# #Ex3
# while True:
#     an = input("Introduceti anul: ")
#     if an.isdigit():
#         an = int (an)
#         if an % 4 == 0:
#             print("An bisect")
#         else:
#             print("An nu este bisect")
#     elif an == "exit":
#         break
#     elif len(an) == 0:
#         continue
#     else:
#         print("Incorect")

#Ex4
# while True:
#     negativ = False
#     numar = input("Introduceti numarul: ")
#     if numar[0] == "-":
#         numar = numar[1:]
#         negativ = True
#     if numar.isdigit() or '.' in numar and len(a := numar.split(".")) == 2 and a[0].isdigit() and a[1].isdigit():
#         numar = float(numar)
#     elif numar == 'exit':
#         print("iesire din program")
#         break
#     else:
#         print("Numar incorect")
#         continue
#
#     if negativ:
#         print(numar, "a fost negativ")
#     elif numar == 0:
#         print("numar = 0")
#     elif numar < 10:
#         print("0<numar<10")
#     else:
#         print("numar>=10")

# #Ex5
# comenzi = ('1','2','3','4','5')
# print("""1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi """)
# while True:
#     comanda = input("Introduceti comanda")
#     if comanda in comenzi:
#         if comanda == '1':
#             print("Afisare lista de cumparaturi")
#         elif comanda == '2':
#             print("Adaugare element")
#         elif comanda == '3':
#             print('Stergere element')
#         elif comanda == '4':
#             print('Stergere lista cumparaturi')
#         else:
#             print('Cautare in lista cumparaturi')
#     else:
#         print('Alegerea nu exista. Reincercati')








