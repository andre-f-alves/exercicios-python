print('-=-' * 14)
print('{:^43}'.format('Progressão Aritmética v2.0'))
print('-=-' * 14)
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = pt
c = 1
while c <= 10:
    print('{} --> '.format(termo), end='')
    termo += razão
    c += 1
print('FIM')
