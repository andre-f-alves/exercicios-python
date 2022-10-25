def escreva(frase):
    print('-' * (len(frase) + 4))
    print(f'{frase:^{len(frase) + 4}}')
    print('-' * (len(frase) + 4))


escreva('Olá, Mundo!')
escreva('Estou aprendendo a programar em python!!!')
