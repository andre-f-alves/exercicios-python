print('=-=' * 12)
print(f'{"Cadastro":^37}')
print('=-=' * 12)
soma = mulheres = 0
pessoas = []
dados = {}
while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dados['Sexo'] not in 'MF':
        print('ERRO! Digite apenas M ou F.')
        dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if dados['Sexo'] in 'F':
        mulheres += 1
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    pessoas.append(dados.copy())
    print('-=' * 11)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        print('ERRO! Digite apenas S ou N.')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    print('-=' * 11)
    if r in 'N':
        break
média = soma / len(pessoas)
print('=-=' * 12)
print(f'''{len(pessoas)} pessoas foram cadastradas;
A média de idade das pessoas cadastradas é {média:.0f} anos;
{mulheres} mulheres foram cadastradas: ''', end='')
for p in pessoas:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}; ', end='')
print('\nAs pessoas com idade acima da média são:')
for p in pessoas:
    print(' ', end='')
    for c, v in p.items():
        if p['Idade'] > média:
            print(f'{c} = {v};', end=' ')
    print()
