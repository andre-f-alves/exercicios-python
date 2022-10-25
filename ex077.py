print('Identificando vogais')
palavras = ('agulha', 'porta', 'janela', 'navio', 'televisão', 'tijolo', 'caderno')
print('Palavras:')
for p in palavras:
    print(f'\n{p.upper()} - vogais: ', end='')
    for l in p:
        if l.upper() in 'AEIOU':
            print(l.upper(), end=' ')
