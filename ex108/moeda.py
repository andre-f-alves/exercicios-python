def aumentar(p=0 , t=0):
    r = p + (p * t / 100)
    return r


def diminuir(p=0, t=0):
    r = p - (p * t / 100)
    return r


def dobro(p=0):
    r = p * 2
    return r


def metade(p=0):
    r = p / 2
    return r


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
