print('Aumento no salário')
salário = float(input('Quanto é o salário do fincionário? R$'))
ns = salário + (salário * 15 / 100)
print('Com um aumento de 15%, o salário desse funcionário passa a ser de R${:.2f}!'.format(ns))
