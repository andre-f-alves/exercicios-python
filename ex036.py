print('Empréstimo')
from time import sleep
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
print('Analisando dados...')
sleep(1)
prestação = casa / (ano * 12)
porcentagem = salário * 30 / 100
if prestação >= porcentagem:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m\nO valor da casa excede 30% do seu salário de {:.2f}'.format(salário))
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[mA prestação será de {:.2f}'.format(prestação))
print('Tenha um bom dia!')
