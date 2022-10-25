print('Calculando desconto')
preço = float(input('Quanto o produro custa? R$'))
np = preço - (preço * 5 / 100)
print('Com um desconto de 5% esse produto passa a valer R${:.2f}!'.format(np))
