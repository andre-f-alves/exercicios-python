from ex108 import moeda
valor = float(input('Digite um valor monetário: R$'))
taxa1 = int(input('Taxa de aumento: '))
taxa2 = int(input('Taxa de desconto: '))
print(f'Com {taxa1}% de aumento esse valor será de {moeda.moeda(moeda.aumentar(valor, taxa1))};')
print(f'Com {taxa2}% de desconto esse valor será de {moeda.moeda(moeda.diminuir(valor, taxa2))};')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))};')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
