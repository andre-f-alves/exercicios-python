print('=' * 40)
print(f'{"Campeonato Brasileirão":^40}')
print('=' * 40)
time = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Atlético-PR', 'Bragantino',
        'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print('Times do brasileirão:')
for t in time:
    print(t, end=' - ')
print('\n', '=-=' * 20)
print('Os 5 primeiros colocados na tabela do brasileirão são:')
for prim in time[0:5]:
    print(prim, end=' - ')
print('\n', '=-=' * 20)
print('Os 4 últimos colocados na tabela são:')
for ult in time[-4:]:
    print(ult, end=' - ')
print('\n', '=-=' * 20)
print('Times em ordem alfabética:')
for ord in sorted(time):
    print(ord, end=' - ')
print('\n', '=-=' * 20)
print(f'O Flamengo aparece na {time.index("Flamengo") + 1}ª posição da tabela.')
