print('Somando números pares')
soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma do(s) {} número(s) par(es) é {}'. format(cont, soma))
