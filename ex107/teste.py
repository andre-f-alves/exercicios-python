from ex107 import moeda
valor = float(input('Digite um valor monetário: R$'))
taxa1 = int(input('Taxa de aumento: '))
taxa2 = int(input('Taxa de desconto: '))
print(f'Com {taxa1}% de aumento esse valor será de R${moeda.aumentar(valor, taxa1)};')
print(f'Com {taxa2}% de desconto esse valor será de R${moeda.diminuir(valor, taxa2)};')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor)};')
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor)}.')
