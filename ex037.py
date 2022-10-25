print('Conversor de bases numéricas')
num = int(input('Digite um número inteiro: '))
print('''Bases de conversão:
[1] para BINARIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opção = int(input('Base de conversão: '))
if opção == 1:
    print('{} convertido para BINARIO é equivalente a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL equivale a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
