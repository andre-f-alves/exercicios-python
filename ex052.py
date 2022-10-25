print('Números primos')
tot = 0
num = int(input('Digite um número: '))
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(n), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso o número {} é \033[32mPRIMO\033[m.'.format(num))
else:
    print('E por isso o número {} \033[31mNÃO É PRIMO\033[m.'.format(num))
