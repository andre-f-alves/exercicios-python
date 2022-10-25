def aumentar(p=0, t=0, form=False):
    """
    -> Calcula o aumento de um valor de acordo com a taxa.
    :param p: Recebe o valor.
    :param t: Recebe a taxa de aumento.
    :param form: (opcional) Formata o valor como monetário.
    :return: Retorna o valor do cálculo.
    """
    r = p + (p * t / 100)
    if form:
        return moeda(r)
    else:
        return r


def diminuir(p=0, t=0, form=False):
    """
    -> Calcula o desconto de um valor de acordo com a taxa.
    :param p: Recebe o valor.
    :param t: Recebe a taxa de desconto.
    :param form: (opcional) Formata o valor como monétario.
    :return: Retorna o valor do cálculo.
    """
    r = p - (p * t / 100)
    if form:
        return moeda(r)
    else:
        return r


def dobro(p=0, form=False):
    """
    -> Calcula o dobro de um valor.
    :param p: Recebe o valor.
    :param form: (opcional) Formata o valor como monetário.
    :return: Retorna o valor do cálculo.
    """
    r = p * 2
    if form:
        return moeda(r)
    else:
        return r


def metade(p=0, form=False):
    """
    -> Calcula a metade de um valor.
    :param p: Recebe o valor.
    :param form: (opcional) Formata o valor em monetário.
    :return: Retorna o valor do cálculo.
    """
    r = p / 2
    if form:
        return moeda(r)
    else:
        return r


def moeda(p=0, moeda='R$'):
    """
    -> Formata um valor em valor monetário.
    :param p: Recebe o valor.
    :param moeda: Recebe a moeda.
    :return: Retorna o valor formatado.
    """
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, taxaa=0, taxad=0):
    """
    -> Mostra um resumo dos cálculos formatados.
    :param p: Recebe o valor
    :param taxaa: Taxa de aumento
    :param taxad: Taxa de desconto
    :return: <sem retorno>
    """
    print('=' * 34)
    print(f'{"Resumo Monetário":^35}')
    print('-' * 34)
    valores = {'Valor analisado:': moeda(p), f'{taxaa}% de aumento:': aumentar(p, taxaa, True),
               f'{taxad}% de desconto:': diminuir(p, taxad, True), 'Dobro do valor:': dobro(p, True),
               'Metade do valor:': metade(p, True)}
    for k, v in valores.items():
        print(f'{k:<20}{v:>14}')
    # print(f'Valor analizado: \t\t{moeda(p)}')
    # print(f'Aumento de {taxaa}%: \t\t{aumentar(p, taxaa, True)}')
    # print(f'Desconto de {taxad}%: \t\t{diminuir(p, taxad, True)}')
    # print(f'O dobro do valor: \t\t{dobro(p, True)}')
    # print(f'A metade do valor: \t\t{metade(p, True)}')
    print('=' * 34)
