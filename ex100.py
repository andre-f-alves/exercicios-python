def linha():
    print('=-=' * 14)


def sorteio(lista):
    from random import randint
    from time import sleep
    for n in range(5):
        lista.append(randint(1, 10))
    print(f'Os números sorteados foram:', end=' ')
    for n in lista:
        print(f'{n}', end=' ')
        sleep(0.5)
    print()


def somapar(lista):
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n
    print(f'A soma dos números pares é {par}')


linha()
print(f'{"Sorteio Numérico":^42}')
linha()
números = []
sorteio(números)
somapar(números)
