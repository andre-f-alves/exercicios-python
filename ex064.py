n = c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(c, soma))
