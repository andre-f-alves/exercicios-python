print('=-=' * 14)
print(f'{"Aproveitamento de Jogadores v1.0":^42}')
print('=-=' * 14)
jogador = dict()
gols = list()
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for p in range(jogos):
    gols.append(int(input(f' - Gols na {p + 1}ª partida: ')))
jogador['Gols'] = gols[:]
jogador['Gols feitos'] = sum(gols)
print('=-=' * 19)
print(jogador)
print('=-=' * 19)
print(f'Dados do jogador:')
for k, v in jogador.items():
    print(f' - {k}: {v}')
print('=-=' * 13)
print(f'{jogador["Nome"]} jogou {jogos} partidas: ')
for i, v in enumerate(gols):
    print(f' --> Na {i + 1}ª partida, fez {v} gols;')
print(f'Totalizando {jogador["Gols feitos"]} gols feitos.')
