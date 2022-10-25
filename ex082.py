print('Listas numéricas')
num = list()
par = list()
impar = list()
while True:
    # num.append(int(input('Digite um número: ')))
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r in 'N':
        break
"""for ind, val in enumerate(num):
    if val % 2 == 0:
        par.append(val)
    else:
        impar.append(val)
print('-=-' * 15)
print(f'''A lsta de números digitados é: {num}
A lista com números pares é: {par}
A lista com números ímpares é: {impar}''')"""
print('-=-' * 15)
print(f'A lista de números digitados é: {num}')
if n in par:
    print(f'A lista com os números pares é: {par}')
else:
    print('Números pares não foram digitados.')
if n in impar:
    print(f'A lista com os números ímpares é: {impar}')
else:
    print('Números ímpares não foram digitados.')
