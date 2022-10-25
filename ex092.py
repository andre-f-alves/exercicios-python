print('=-=' * 13)
print(f'{"Cadastro CTPS":^40}')
print('=-=' * 13)
from datetime import date
carteira = dict()
carteira['Nome'] = str(input('Nome: ')).strip().title()
ano_nascimento = int(input('Ano de nascimento: '))
carteira['Idade'] = date.today().year - ano_nascimento
carteira['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
if carteira['CTPS'] != 0:
    carteira['Contratação'] = int(input('Ano de contratação: '))
    carteira['Salário'] = float(input('Salário: R$'))
    carteira['Aposentadoria'] = carteira['Idade'] + ((carteira['contratação'] + 35) - date.today().year)
print('=-=' * 13)
for k, v in carteira.items():
    print(f' - {k}: {v}')
