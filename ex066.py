print('Somando números')
cont = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'{cont} números foram digitados e a soma entre eles equivale a {soma}.')
