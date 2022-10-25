print('Analisando números')
r = 'Ss'
cont = soma = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]: ')).strip()[0]
média = soma / cont
print('O maior número é {} e o menor é {}.'.format(maior, menor))
print('A média entre os números digitados é {:.1f}.'.format(média))
