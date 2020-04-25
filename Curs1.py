# print('Primul meu string' * 2)

# print(2+2*2-2/1)
# ** pt putere
# // pt rest

# a = 'String'
# a += 'String1'
# print(type(a))

# concatenare
# a = 'string1'
# b = 'string2'
# c = "{1} {0} {1}".format(a,b)
# c = a + " " + b
# c = f"{a} {b}"
# print (c)

# a = "1"
# b = "2"
# c = int(a) + int(b)
# print(c)
# daca avem str si int trebuie sa convertim neaparat

# a = input("Introdu a:")
# print(a)

# if conditie:
#     executie
# elif conditie2:
#     executie2
# else:
#     executie3

# a = 2
# b = 3
# #a = None  doar il declar dar nu ii dau nicio val
# if a == b: #True == 1
#     print("egale")
# elif a > b:
#     print("a este mai mare")
# else:
#     print("a este mai mic")


# while conditie:
#     executie

# x = 10
# while x > 1:
#     print("x este" , x)
#     break #pass
#     x -= 1

# while True:
#     euro = input("Valoare euro pt conversie")
#     if euro.isdigit():
#         pass
#     elif len(euro.split('.')) == 2:
#         a = euro.split('.')[0]
#         b = euro.split('.')[1]
#
#
#     if type(euro) == float: #verific daca e int
#         euro = float(euro)
#         print("Valoarea convertita este:", euro * 4.87, "RON")
#     else:
#         print("Valoarea nu este numar")

# while True:
#     euro = input("val euro:")
#     if len(euro) == 0:
#         floatSign = 1
#         if euro[0] == "-":
#             floatSign = -1
#             euro = euro[1:]
#         a = None
#         if (euro.isdigit()):
#             euro = int(euro)
#         elif "." in euro and len(a := euro.split(".")) == 2 and a[0].isdigit() and a[1].isdigit():
#             euro = float(euro)
#         else:
#             print("val gresita")
#             continue
#         print("val conv este:", floatSign * euro * 4.87, " RON")

# a = 2
# b = 2 if a == 2 else 3

str = "abecedar"
str = str[-1] #pt a lua ultima valoare
print(str)

for poz,char in enumerate(str):
    print(poz,char)

for x in range(-1,6,2):
    print(x)

lista = [x for x in range(10)]
