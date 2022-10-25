print('\033[34m<-=->\033[m' * 9)
print(f'\033[35m{"Par ou Ímpar":^46}\033[m')
print('\033[34m<-=->\033[m' * 9)
from random import randint
from time import sleep
acerto = 0
while True:
    jogador = int(input('Digite um número: '))
    opção = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    while opção not in 'PpIi':
        opção = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    pc = randint(1, 10)
    soma = jogador + pc
    if soma % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'ÍMPAR'
    print('PROCESSANDO...')
    sleep(0.5)
    print('\033[33m=-=\033[m' * 12)
    print(f'''Você jogou {jogador} e o computador jogou {pc}
{jogador} + {pc} = {soma} - O resultado foi \033[34m{pi}\033[m''')
    print('\033[33m=-=\033[m' * 12)
    if soma % 2 == 0:
        if opção in 'Pp':
            acerto += 1
            print('\033[32mParabéns, você acertou!\033[m')
        else:
            print('\033[31mVocê errou!\033[m')
            break
    else:
        if opção in 'Ii':
            acerto += 1
            print('\033[32mParabéns, você acertou!\033[m')
        else:
            print('\033[31mVocê errou!\033[m')
            break
    print('Vamos jogar novamente...')
    sleep(1)
print(f'\033[31mGAME OVER!\033[m Você teve {acerto} acerto(s)')
