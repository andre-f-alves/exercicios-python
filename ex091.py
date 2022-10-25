print('=-=' * 13)
print(f'{"Jogando Dado":^39}')
print('=-=' * 13)
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = list()
print('Jogadores e números tirados:')
for k, v in jogadores.items():
    print(f' --> O {k} tirou o número: {v}')
    sleep(1)
print('=-=' * 13)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for p, e in enumerate(ranking):
    print(f'  --> {p + 1}º lugar: {e[0]} com {e[1]}')
    sleep(1)
print('-<=-<< FIM DE JOGO >>->=-')
