def linha():
    print('=-=' * 20)


def ficha(nome='<não informado>', gols=0):
    """
    -> Mostra o nome e os gols de um jogador.
    :param nome: (opcional) Nome do jogador.
    :param gols: (opcional) Gols marcados pelo jogador.
    :return: <sem retorno>
    """
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


linha()
print(f'{"Ficha do Jogador":^60}')
linha()
jogador = str(input('Nome do jogador: '))
gol = str(input('Total de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
