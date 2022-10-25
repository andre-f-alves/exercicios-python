print('=-=' * 14)
print('{:^43}'.format('Sequência de Fibonacci v1.0'))
print('=-=' * 14)
n = int(input('Quantos termos quer ver? '))
t1 = 0
t2 = 1
print('{} --> {} --> '.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print('{} --> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
