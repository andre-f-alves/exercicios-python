pessoas = list()
dados = list()
pesados = leves = ''
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print('=-=' * 8)
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    print('=-=' * 8)
    if r in 'N':
        break
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso é {maior}, sendo as pessoas:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso é {menor}, sendo as pessoas:', end=' ')
for i in pessoas:
    if i[1] == menor:
        print(i[0], end=' ')
