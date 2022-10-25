print('-=-' * 14)
print('{:^43}'.format('Progressão Aritmética v1.0'))
print('-=-' * 14)
pt = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
Nésimo = pt + (10 - 1) * razão
for pa in range(pt, Nésimo + razão, razão):
    print(pa, end=' --> ')
print('FIM')
