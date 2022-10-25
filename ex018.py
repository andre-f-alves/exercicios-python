print('Seno, Cosseno e Tangente')
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
print('O valor do seno de {}° é {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O cosseno de {}° é {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('E a tangente de {}° é {:.2f}'.format(ângulo, tangente))
