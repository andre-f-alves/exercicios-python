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
