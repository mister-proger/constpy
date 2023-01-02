import decimal
import math

def pi(*imp):
    if not imp:
        return round(pi(int(1000000)), 10)
    else:
        imp = imp[0]
        return_pi = int(0)
        int_set_pi = int(1)
        for i in range(imp):
            return_pi = return_pi + 1 / int_set_pi
            int_set_pi = (abs(int_set_pi) + 2) * check_int_set_pi(int_set_pi)
        return decimal.Decimal(return_pi * 4)

def check_int_set_pi(imp_int_set_pi):
    if imp_int_set_pi > 0:
        return int(-1)
    elif imp_int_set_pi < 0:
        return int(1)
    else:
        print('ОШИБКА: интегральное значение не может быть равно 0')

def tay(*imp):
    if not imp:
        return decimal.Decimal(2 * pi())
    else:
        return decimal.Decimal(2 * pi(int(imp)))

def e(*imp):
    if not imp:
        return e(50)
    else:
        imp = imp[0]
        return_e = int(0)
        for n in range(imp):
            return_e = return_e + 1 / math.factorial(n)
        return decimal.Decimal(return_e)
