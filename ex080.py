print('Ordem numérica')
listnum = []
for num in range(0, 5):
    n = int(input(f'Digite o {num + 1}º número: '))
    if num == 0 or n > listnum[-1]:
        listnum.append(n)
        print('Número adicionado no final da lista...')
    else:
        for pos in range(len(listnum)):
            if n <= listnum[pos]:
                listnum.insert(pos, n)
                if pos == 0:
                    print(f'Número adicionado na posição {pos} da lista...')
                else:
                    print(f'Número adicionado na {pos}ª posição da lista...')
                break
print('-=-' * 15)
print(f'A ordem dos números digitados é: {listnum}')
