valores = list()
par = list()
impar = list()
# valores = [[], []]
for n in range(7):
    num = int(input(f'Digite o {n + 1}º número: '))
    """if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)"""
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
valores.append(par[:])
par.clear()
impar.sort()
valores.append(impar[:])
impar.clear()
# valores[0].sort()
# valores[1].sort()
print('=-=' * 15)
print(f'{len(valores[0])} números pares foram digitados, sua lista é: {valores[0]}')
print(f'{len(valores[1])} números ímpares foram digitados, sua lista é: {valores[1]}')
