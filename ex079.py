print('Registro numérico')
num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número registrado com sucesso...')
    else:
        print('Esse número já foi registrado...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'N':
        break
print('-=-' * 15)
num.sort()
print(f'Os números registrados foram: {num}')
