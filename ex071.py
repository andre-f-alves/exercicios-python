print('=-=' * 14)
print(f'{"Banco 24hs":^40}')
print('=-=' * 14)
valor = int(input('Qual o valor a ser sacado? R$'))
c = 200
cont = 0
print('Total de cédulas a ser retiradas:')
while True:
    if valor >= c:
        valor -= c
        cont += 1
    else:
        if cont > 0:
            print(f'{cont} cédulas de R${c:.2f}.')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        if valor == 0:
            break
