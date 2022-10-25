print('Analisando números aleatórios')
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Números sorteados: {num}')
print(f'O maior número é {max(num)} e o menor é {min(num)}.')
