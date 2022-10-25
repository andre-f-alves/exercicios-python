def linha():
    print('=-=' * 18)


def contador(início, fim, passo):
    from time import sleep
    linha()
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {início} a {fim} de {passo} em {passo}')
    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont} -> ', end='')
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} -> ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM')


linha()
print(f'{"Gerador de Contagens":^55}')
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez! Crie uma contagem personalizada:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
linha()
