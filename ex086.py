print('=-=' * 13)
print(f'{"Gerador de Matriz v1.0":^40}')
print('=-=' * 13)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
print('=-=' * 13)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
