print('\033[34m-=-\033[m' * 8)
print('\033[32mPedra, papel e tesoura!\033[m')
print('\033[34m-=-\033[m' * 8)
jogador = int(input('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Sua jogada: '''))
if jogador == 0 or jogador == 1 or jogador == 2:
    from time import sleep
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    itens = ('Pedra', 'Papel', 'Tesoura')
    from random import randint
    pc = randint(0, 2)
    print('\033[32m-=-\033[m' * 9)
    print('''O Computador jogou {}\nO Jogador escolheu {}'''.format(itens[pc], itens[jogador]))
    print('\033[32m-=-\033[m' * 9)
    # Jogador perde
    if jogador == 0 and pc == 1:
        print('Papel embrulha Pedra.\n\033[31mVocê perdeu!\033[m')
    elif jogador == 1 and pc == 2:
        print('Tesoura corta Papel.\n\033[31mVocê perdeu!\033[m')
    elif jogador == 2 and pc == 0:
        print('Pedra quebra Tesoura.\n\033[31mVocê perdeu!\033[m')
    # Jogador ganha
    elif jogador == 1 and pc == 0:
        print('Papel embrulha Pedra.\n\033[32mParabéns, você ganhou!\033[m')
    elif jogador == 2 and pc == 1:
        print('Tesoura corta Papel.\n\033[32mParabéns, você ganhou!\033[m')
    elif jogador == 0 and pc == 2:
        print('Pedra quebra Tesoura.\n\033[32mparabéns, você ganhou!\033[m')
    # Empate
    else:
        print('\033[34mEmpate!\033[m')
    print('\033[31m-= FIM DA RODADA =-\033[m')
else:
    print('Jogada inválida. Tente novamente')
