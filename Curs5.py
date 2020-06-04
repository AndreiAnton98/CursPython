# def prima_functie():
#     pass

# def message():
#     print("enter a value: ")
# message()

# def hello(name):
#     print('Hello', name)
# name = input("Enter your name: ")
# hello(name)

# de cautat diferenta parametru si argument
# def message(what, number='2'):  # param default la final
#     """
#     :param what:
#     :param number:
#     :return:
#     """
#     print('Enter', what, 'a number', number)
#
# message('telephone', 11)


# def suma(a, b, c):
#     print(f'{a} + {b} + {c} = {a + b + c}')
#
# suma(3, a=1, b=2)  # atribuie in ordine   ASA NU E OK suma(3, a=1, b=2)

# def HappyNewYear(wishes=True):
#     print('3')
#     print('2')
#     print('1')
#     if not wishes:
#         return
#     print("Happy new year!")
#
# print(HappyNewYear(False))

# def name():
#     return 123
#
# print(name())

# def sum_of_list(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
# a = sum_of_list([5, 4, 3])
# print(a)

# import datetime
#
# def validare_nr_zile(zi, luna, an) -> bool:
#     try:
#         a = datetime.datetime.strptime(f'{zi}.{luna}.{an}', "%d.%m.%Y")
#         return True
#     except ValueError:
#         return False


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))