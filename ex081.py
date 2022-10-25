print('Análise numérica')
num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r in 'N':
        break
print('=-=' * 20)
print(f'{len(num)} números foram digitados.')
num.sort(reverse=True)
print(f'A ordem decrescete dos números digitados é: {num}')
if 5 in num:
    for pos, n in enumerate(num):
        print(f'O número 5 apareceu nas posições {pos}', end=' ')
else:
    print('O número 5 não foi encontrado nesta lista.')
