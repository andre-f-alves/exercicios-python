print('=-=' * 13)
print(f'{"Gerador de Matriz v2.0":^40}')
print('=-=' * 13)
soma = soma_par = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
print('=-=' * 13)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        # if matriz[l][c] % 2 == 0:
        #     soma_par += matriz[l][c]
    print()
print('=-=' * 13)
for element in matriz:
    for num in element:
        if num % 2 == 0:
            soma_par += num
print(f'A soma dos números pares é {soma_par}')
for e in matriz:
    soma += e[2]
# for l in range(3):
#     soma += matriz[l][2]
print(f'A soma dos números da terceira coluna é {soma}')
# maior = 0
# for c in range(3):
#     if c == 0 or matriz[1][c] > maior:
#         maior = matriz[1][c]
print(f'O maior número da segunda linha é o {max(matriz[1])}')
