# stack = []
# def push(val):
#     stack.append(val)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
#
# print(stack)

# class Stack:
#     def __init__(self):
#         self.__stackList = []  # __ pt a-l face privat
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# class AddingStack(Stack):  # mostenire
#     def __init__(self):
#         Stack.__init__(self)  # nu e obligatoriu
#         self.__sum = 0
#
#     def getSum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
#
# stackObject = AddingStack()
# for i in range(5):
#     stackObject.push(i)
#
# print(stackObject.getSum())
#
# for i in range(5):
#     print(stackObject.pop())
# stackObject1 = Stack()
# stackObject1.push(3)
# stackObject1.push(2)
# stackObject1.push(1)

# class ExampleClass:
#     def __init__(self, val=1):
#         self.__first =val
#
#     def setSecond(self, val):
#         self.__second = val
#
# obj1 = ExampleClass()
# obj2 = ExampleClass(2)
#
# obj2.setSecond(3)
#
# obj3 = ExampleClass(4)
# obj3.__third = 5
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)


# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         Example.__counter += 1
#
#
# obj1 = Example()
# obj2 = Example(3)
# obj3 = Example(4)
# print(obj1.__dict__, obj1._Example__counter)
# print(obj2.__dict__, obj2._Example__counter)
# print(obj3.__dict__, obj3._Example__counter)

# class Example:
#     attr = 1
#     def __init__(self):
#         pass
#
# print(hasattr(Example, 'attr'))
# print(hasattr(Example, 'prop2'))


# class Classy:
#     variabila = 2
#
#     def method(self):
#         print(self.variabila, self.var)
#
# obj = Classy()
# obj.var = 3
# obj.method()

# class SuperOne:
#     pass
#
# class SuperTwo:
#     pass
#
# class SuperThree(SuperOne, SuperTwo):
#     pass
#
# def printBases(cls):
#     for x in cls.__bases__:
#         print(x.__name__)
#
# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(SuperThree)

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):
#         return f'{self.nae} in {self.galaxy}'
#
# sun = Star('Sun', 'Milky Way')

# class Vehicule:
#     pass
#
# class VehiculeDeTractare(Vehicule):
#     pass
#
# class Tractoare(VehiculeDeTractare):
#     pass
#
#
# objVehicule = Vehicule()
# objVehiculeDeTractare = VehiculeDeTractare()
# objTractoare = Tractoare()
# for cls1 in [Vehicule, VehiculeDeTractare, Tractoare]:
#     for cls2 in [Vehicule, VehiculeDeTractare, Tractoare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()

# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
# obj1 = SampleClass(0)
# obj2 = SampleClass(2)
# obj3 = obj1
# obj3.val += 1
#
# print(obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)
# print(obj1.val, obj2.val, obj3.val)
# str1 = 'Maria are mere '
# str2 = 'Maria are mere galbene'
# str1 += 'galbene'
#
# print(str1 == str2, str1 is str2)

# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'My name is {self.name}'
#
# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)
#         super().__init__(name)  # acelasi lucru
#
# obj = Sub("Alexandra")
# print(obj)

# class Super:
#     a = 1
#
# class Sub(Super):
#     b = 2
#
# obj = Sub()
# print(obj.b)
# print(obj.a)

# class Super:
#     def __init__(self):
#         self.supVar = 11
#
# class Sub(Super):
#     def __init__(self):
#         super(Super).__init__()
#         self.subVar = 12
#
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# class Level1:
#     varia1 = 100
#     def __init__(self):
#         self.var1 = 101
#     def fun1(self):
#         return 102
#
# class Level2(Level1):
#     varia2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var2 = 201
#
#     def fun2(self):
#         return 202
#
# class Level3(Level2):
#     varia3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var3 = 301
#     def fun3(self):
#         return 302
#
# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())

# class Left:
#     var = 'L'
#     varLeft = 'LL'
#     def fun(self):
#         return 'Left'
#
# class Right:
#     var = "R"
#     varRight = 'RR'
#     def fun(self):
#         return 'Right'
#
# class Sub(Left, Right):
#     pass
#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())

class Calculator:
    def sum(self, *lista):
        suma = 0
        for elem in lista:
            suma += elem
        return suma
    def diferenta(self, a, b):
        return a - b
    def inmultire(self, a, b):
        return a * b
    def impartire(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Nu se poate"