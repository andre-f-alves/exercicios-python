print('Analisando pesos')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''O maior pesso lido é {}Kg
O menor peso lido é {}Kg'''.format(maior, menor))
