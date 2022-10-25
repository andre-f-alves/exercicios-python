print('Menu de opções')
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
o = 0
while o != 5:
    o = int(input('''Opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
--> Qual sua opção: '''))
    if o == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1, n2, s))
    elif o == 2:
        multi = n1 * n2
        print('{} x {} = {}'.format(n1, n2, multi))
    elif o == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print('{} é maior do que {}.'.format(maior, menor))
        elif n1 < n2:
            maior = n2
            menor = n1
            print('{} é maior do que {}.'.format(maior, menor))
        else:
            print('Não há um número maior, os dois são iguais.')
    elif o == 4:
        print('informe os novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif o == 5:
        print('ENCERRANDO...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 9)
print('FIM DO PROGRAMA.')
