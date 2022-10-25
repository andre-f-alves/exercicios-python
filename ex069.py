print('=' * 43)
print(f'{"Cadastro":^43}')
print('=' * 43)
cont = maiores = homens = mulheres = 0
while True:
    idade = int(input('Idade da pessoa: '))
    s = str(input('Sexo [M/F]: ')).strip()[0]
    while s not in 'MmFf':
        s = str(input('Sexo [M/F]: ')).strip()[0]
    cont += 1
    if idade >= 18:
        maiores += 1
    if s in 'Mm':
        homens += 1
    if s in 'Ff' and idade < 20:
        mulheres += 1
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    print('=' * 25)
    if resp in 'Nn':
        break
print(f'''No total, {cont} pessoas foram cadastradas. Desses {cont}:
{maiores} tem mais de 18 anos;
{homens} homens foram cadastrados;
{mulheres} mulheres têm menos de 20 anos.''')
