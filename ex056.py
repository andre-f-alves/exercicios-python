print('Analisador de pessoas')
soma = 0
média = 0
velho = ''
menor = 0
maior = 0
for p in range(1, 5):
    print('------- {}ª Pessoa -------'.format(p))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    média = soma / 4
    if sexo == 'M' and idade > maior:
        maior = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        menor += 1
print('''A média das idades é {}.
O homem mais velho tem {} anos e se chama {}.
{} mulheres tem menos de 20 anos.'''.format(média, maior, velho, menor))
