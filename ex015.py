print('Aluguel de carros')
dias = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km percorridos? '))
valor = dias * 60 + Km * 0.15
print('O valor de aluguel do carro é R${:.2f}'.format(valor))
