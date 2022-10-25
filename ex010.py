print('Convertendo dinheiro')
reais = float(input('Quanto você tem na carteira? R$'))
dólar = reais / 5.36
euro = reais / 6.45
libra = reais / 7.36
print(f'Isso é equivalente a:\nUS${dólar:.2f}\n{euro:.2f} euros\n{libra:.2f} libras')
