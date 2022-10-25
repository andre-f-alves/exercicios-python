from ex109 import moeda
valor = float(input('Digite um valor monetário: R$'))
taxa1 = int(input('Taxa de aumento: '))
taxa2 = int(input('Taxa de desconto: '))
print(f'Com {taxa1}% de aumento esse valor será de {moeda.aumentar(valor, taxa1, True)};')
print(f'Com {taxa2}% de desconto esse valor será de {moeda.diminuir(valor, taxa2, True)};')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)};')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.')
