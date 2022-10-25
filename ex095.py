print('=-=' * 14)
print(f'{"Aproveitamento de Jogadores v2.0":^42}')
print('=-=' * 14)
from time import sleep
jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for p in range(jogos):
        gols.append(int(input(f' - Gols na {p + 1}ª partida: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    print('-=' * 13)
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    print('-=' * 13)
    if r in 'N':
        break
print('=' * 40)
# Cabeçalho
# print('Cód. ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
print(f'{"Cód. "}{"Nome":<15}{"Gols":<15}{"Total":<15}')
for p, j in enumerate(jogadores):
    print(f'{p + 1:<5}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    opc = int(input('Quer ver o aproveitamento de qual jogador? (0 para parar) '))
    if opc <= 0:
        break
    else:
        if opc <= len(jogadores):
            print(f'Levantamento do jogador {jogadores[opc - 1]["Nome"]}:')
            for i, v in enumerate(jogadores[opc - 1]['Gols']):
                print(f' --> Na {i + 1}ª partida, fez {v} gols;')
        else:
            print('Jogador não cadastrado. Tente novamente.')
    print('=-=' * 14)
print('=-=' * 14)
print('ENCERRANDO PROGRAMA...')
sleep(1)
print('=-<< FIM DO PROGRAMA >>-=')
