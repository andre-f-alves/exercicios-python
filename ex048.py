print('Somando ímpares múltiplos de 3')
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print('A soma dos {} valores solicitados é {}.'.format(cont, soma))
