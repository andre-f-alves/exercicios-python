print('Adivinhe o Número v1.0')
from random import randint
from time import sleep
print('\033[31m-=-\033[m' * 20)
print('\033[34mEu estou pensando em um número entre 0 e 5. Tente adivinhar!')
print('\033[31m-=-\033[m' * 20)
player = int(input('Em que número você acha que estou pensando? '))
pc = randint(0, 5)
print('Analisando...')
sleep(1)
if player == pc:
    print('\033[32mParabéns, você acertou!\033[m')
else:
    print('\033[35mQue pena, você errou! Eu estava pensando no número {}.\033[m'.format(pc))
print('\033[31m-=-FIM DA PARTIDA-=-\033[m')
