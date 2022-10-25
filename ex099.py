def linha():
    print('=-=' * 19)


def maior(* num):
    from time import sleep
    cont = maior = 0
    linha()
    print('Analisando números...')
    for n in num:
        print(f'{n}', end='  ')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print()
    print(f'{len(num)} valores foram informados.', end=' ')
    print(f'Desses, o maior valor é o {maior}.')
    # print(f'Desses, o maior valor é o {max(num)}.')


linha()
print(f'{"Analisador de Números":^58}')
maior(2, 9, 4, 5, 7, 1)
linha()
