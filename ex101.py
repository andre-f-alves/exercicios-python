def linha():
    print('=-=' * 9)


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    s = ''
    if idade < 16:
        return f'{idade} anos = VOTO NEGADO'
    elif idade < 18 or idade > 65:
        return f'{idade} anos = VOTO OPCIONAL'
    else:
        return f'{idade} anos = VOTO OBRIGATÓRIO'


linha()
print(voto(int(input('Ano de nascimento: '))))
