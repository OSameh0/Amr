from simpleCalculator import *


def simplecalc(x, y, z, m):
    print('The result = {}'.format(add(x, y, z, m)))
    print('The result = {}'.format(multi(x, y, z, m)))
    print('The result = {}'.format(div(x, y, z, m)))
    print('The result = {}'.format(sub(x, y, z, m)))


y = simplecalc(50, 10, 3, 2)
print(y)
