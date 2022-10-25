print('-=-' * 4)
print('Tabuada v2.0')
print('-=-' * 4)
n = int(input('Digite um número e veja sua tabuada: '))
print('=' * 11)
for t in range(1, 11):
    print('{} x {:2} = {}'. format(n, t, n * t))
print('=' * 11)
