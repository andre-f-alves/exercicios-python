print('Catetos e Hipotenusa')
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
