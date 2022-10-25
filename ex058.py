print('\033[32m=\033[m' * 47)
print('\033[34m{:^46}\033[m'.format('Adivinhe o número v2.0'))
print('\033[32m=\033[m' * 47)
from random import randint
from time import sleep
print('\033[31m=-=\033[m' * 20)
print('\033[35mEstou pensando em um número entre 0 e 10. Tente adivinhar!\033[m')
print('\033[31m=-=\033[m' * 20)
pc = randint(0, 10)
jogador = 0
tentativa = 0
while jogador != pc:
    jogador = int(input('Em que número você acha que eu estou pensando? '))
    print('\033[34mANALISANDO...\033[m')
    sleep(0.5)
    tentativa += 1
    if jogador != pc:
        if jogador < pc:
            print('Mais...', end=' ')
        else:
            print('Menos...', end=' ')
        print('Tente novamente')
    else:
        print('\033[32mParabéns, você acertou!\033[m')
        print('No total foram {} tentaivas.'.format(tentativa))
print('\033[31m-=FIM DA PARTIDA=-\033[m')
