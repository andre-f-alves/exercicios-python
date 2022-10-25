print('Analisando maior e menor número na lista')
num = list()
maior = menor = 0
for n in range(5):
    num.append(int(input(f'Digite um número para a posição {n}: ')))
    """if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]
print('-=-' * 15)
print(f'Os números digitados foram: {num}')
print(f'O maior número é o {maior} e está nas posições:', end=' ')
for pos, e in enumerate(num):
    if e == maior:
        print(f'{pos}', end=' ')
print(f'\nO menor número é o {menor} e está nas posições:', end=' ')
for ind, v in enumerate(num):
    if v == menor:
        print(f'{ind}', end=' ')"""
print('-=-' * 15)
print(f'Os números digitados foram: {num}')
print(f'O maior número é o {max(num)} e está nas posições', end=' ')
for pos, e in enumerate(num):
    if e == max(num):
        print(f'{pos}', end=' ')
print(f'\nO menor número é o {min(num)} e está nas posições', end=' ')
for ind, v in enumerate(num):
    if v == min(num):
        print(f'{ind}', end=' ')
