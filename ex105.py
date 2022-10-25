def linha():
    print('=-=' * 20)


def notas(*n, situação=False):
    """
    -> Organiza um Dicionário com as notas dos alunos(as).
    :param n: Notas dos alunos(as).
    :param situação: (ocpional) Indica a situação dos alunos(as).
    :return: Dicionário organizado.
    """
    boletim = dict()
    boletim['Total de notas'] = len(n)
    cont = maior = menor = 0
    for nota in n:
        if cont == 0 or cont == 1:
            maior = menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        cont += 1
    boletim['Maior'] = maior
    boletim['Menor'] = menor
    boletim['Média'] = sum(n) / len(n)
    if situação:
        if boletim['Média'] < 5:
            boletim['Situação'] = 'REPROVADO!'
        elif boletim['Média'] <= 6:
            boletim['Situação'] = 'RECUPERAÇÃO!'
        else:
            boletim['Situação'] = 'APROVADO!'
    return boletim


linha()
print(f'{"Boletim v5.0":^60}')
linha()
resp = notas(5.2, 2.5, 9, 8.5, situação=True)
print(resp)
linha()
help(notas)
