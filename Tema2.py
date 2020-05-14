import datetime


def format_check():
    global cnp
    cnp = cnp.lstrip()
    cnp = cnp.rstrip()
    if len(cnp) != 13 or not cnp.isdigit():
        print('Problema la format')
        return False
    else:
        return True


def date_check(cnp):
    an = 0
    s = int(cnp[0])
    aa = int(cnp[1:3])
    ll = int(cnp[3:5])
    zz = int(cnp[5:7])
    if s == 0:
        print('Prima cifra nu poate sa fie 0')
        return False
    elif s == 1 or s == 2:
        an += 1900 + aa
    elif s == 3 or s == 4:
        an += 1800 + aa
    elif s == 5 or s == 6:
        an += 2000 + aa
    else:
        an += aa
    try:
        new_date = datetime.datetime(an, ll, zz)
        return True
    except ValueError:
        print('Problema la data')
        return False


def judet_check(cnp):
    jj = int(cnp[7:9])
    if 1 <= jj <= 46 or jj == 51 or jj == 52:
        return True
    else:
        print('Problema la judet')
        return False


def number_check(cnp):
    nnn = int(cnp[9:12])
    if nnn == 0:
        print('Problema la numarul unic')
        return False
    else:
        return True


def control_check(cnp):
    cod = '279146358279'
    c = 0
    index = 0
    for char in cod:
        c += int(char) * int(cnp[index])
        index += 1
    c = c % 11
    if c == 10:
        c = 1
    if c != int(cnp[-1]):
        print(c)
        print('Problema la cifra de control')
        return False
    else:
        return True


while True:
    cnp = input("Introduceti CNP: ")
    if format_check() and date_check(cnp) and judet_check(cnp) and number_check(cnp) and control_check(cnp):
        print('CNP ok')
    if cnp == 'exit':
        break
