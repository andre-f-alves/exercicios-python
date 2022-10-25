print('=-=' * 10)
print(f'{"Tabuada v3.0":^30}')
print('=-=' * 10)
c = 0
while True:
    num = int(input('Digite um número e veja sua tabuada: '))
    if num < 0:
        break
    print('=' * 12)
    for t in range(1, 11):
        print(f'{num} x {t:2} = {num * t}')
    print('=' * 12)
print('PROGRAMA FINALIZADO.')
