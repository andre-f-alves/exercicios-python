def linha():
    print('=-=' * 16)


def fatorial(n=0, show=False):
    """
    -> Função para cálculo do Fatorial.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: Resultado do cálculo do Fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show is True:
        c = n
        while c > 0:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            c -= 1
    return f
        # if show:
            #     print(f'{c}', end='')
            #     print(' x ' if c > 1 else ' = ', end='')
            # f *= c
    # return f


linha()
print(f'{"Cálculo do Fatorial v2.0":^48}')
linha()
print(fatorial(int(input('Digite um número: ')), True))
linha()
help(fatorial)
