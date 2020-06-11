# import operator
# class Prajitura:
#     lista = []
#     def __init__(self, nume: str, pret: int, gramaj: int):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#         Prajitura.lista.append(self)
#
#     def __repr__(self):
#         return f'{self.nume} costa {self.pret} lei si cantareste {self.gramaj} grame'
#
#     @classmethod
#     def afiseaza_dupa_gramaj(cls):
#         cls.lista.sort(key=operator.attrgetter('gramaj'))
#         print("Sortat dupa gramaj")
#         for prajitura in cls.lista:
#             print(prajitura)
#
#     @classmethod
#     def afiseaza_dupa_pret(cls):
#         cls.lista.sort(key=operator.attrgetter('pret'))
#         print('Sortat dupa pret')
#         for prajitura in cls.lista:
#             print(prajitura)
#
#
# class Tort(Prajitura):
#     def __init__(self, nume: str, pret: int, gramaj: int):
#         super().__init__(nume, pret, gramaj)
#         self.etajat = False
#         self.glazura = 'ciocolata'
#
#     def set_etajat(self, etajat: bool):
#         self.etajat = etajat
#
#     def is_etajat(self):
#         return self.etajat
#
#     def set_glazura(self, glazura: str):
#         self.glazura = glazura
#
#     def get_glazura(self):
#         return self.glazura
#
#
# class Fursec(Prajitura):
#     def __init__(self, nume: str, pret: int, gramaj: int):
#         super().__init__(nume, pret, gramaj)
#
#
# t1 = Tort('t1', 1, 100)
# t2 = Tort('t2', 12, 50)
# t3 = Tort('t3', 10, 110)
# f1 = Fursec('f1', 5, 75)
# f2 = Fursec('f2', 20, 150)
# f3 = Fursec('f3', 1, 10)
#
#
# Prajitura.afiseaza_dupa_gramaj()
# Prajitura.afiseaza_dupa_pret()
#
# t1.set_etajat(True)
# t1.set_glazura('cacao')
# print(t1.is_etajat())
# print(t1.get_glazura())


class Student:
    def __init__(self, nume:str, prenume:str):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f'{self.nume} {self.prenume} are {self.absente} absente'

    def adauga_absenta(self):
        self.absente += 1

    def sterge_absente(self, numar):
        if numar <= self.absente:
            self.absente -= numar


class Materii(Student):
    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)

    def adauga_materie(self, materie:str, note:list):
        self.materii[materie] = note

    def afiseaza_materii(self):
        str = ''
        for materie in self.materii:
            str += materie + " "
        print(f'{self.nume}: {str}')

    def afiseaza_materii_medii(self):
        str = ''
        for materie in self.materii:
            suma = 0
            nr = 0
            for nota in self.materii[materie]:
                if isinstance(nota, int) and 1 <= nota <= 10:
                    suma += nota
                    nr += 1
            str += f'{materie}: {round(suma/nr, 1)} '
        print(f'{self.nume} {str}')


ion = Materii('Ion', 'Roata')
ion.adauga_absenta()
ion.adauga_absenta()
ion.adauga_absenta()
ion.sterge_absente(2)
george = Materii('George', 'Cerc')
george.adauga_absenta()
george.adauga_absenta()
george.adauga_absenta()
george.adauga_absenta()
george.sterge_absente(2)
print(ion)
print(george)
ion.adauga_materie('Python', ['a', 'sdfd0', 7])
george.adauga_materie('Python', [8, 6, 5])
george.adauga_materie('Matematica', [4, 'a', 8])
ion.adauga_materie('Romana', [10, 2, 7])
ion.afiseaza_materii()
george.afiseaza_materii()
ion.afiseaza_materii_medii()
george.afiseaza_materii_medii()



