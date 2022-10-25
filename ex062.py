print('-=-' * 14)
print('{:^43}'.format('Progressão Aritmética v3.0'))
print('-=-' * 14)
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = pt
c = 1
total = 0
mais = 10
while not mais == 0:
    total += mais
    while c <= total:
        print('{} --> '.format(termo), end='')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quer ver mais termos? Quantos: '))
print('Progressão finalizada com {} termos.'.format(total))
