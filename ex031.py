print('Valor da passagem')
km = float(input('Qual é a distância de sua viagem? '))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
'''valor = km * 0.50 if km <= 200 else km * 0.45'''
print('O valor da pssagem será de R${}. Faça uma boa viagem!'. format(valor))
