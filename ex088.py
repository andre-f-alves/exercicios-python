print('=-=' * 14)
print(f'{"Gerador de Cadeias Numéricas":^43}')
print('=-=' * 14)
from time import sleep
from random import randint
valor = list()
cadeia = list()
ask = int(input('Quer ver quantas cadeias de números sorteados? '))
total = 1
while total <= ask:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in valor:
            valor.append(num)
            cont += 1
        if cont >= 6:
            break
    cadeia.append(valor[:])
    valor.clear()
    total += 1
print('-=' * 3, f'Gerando Cadeias Numéricas', '=-' * 3)
for p, c in enumerate(cadeia):
    print(f'Cadeia numérica {p + 1}: {c}')
    sleep(1)
print('-<<= FIM DO PROGRAMA =>>-')
