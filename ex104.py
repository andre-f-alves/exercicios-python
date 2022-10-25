def linha():
    print('=-=' * 20)


def leiaInt(num):
    """
    -> Recebe um número inteiro digitado.
    :param num: Número digitado
    :return: Mostra o número digitado
    """
    correto = False
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            correto = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if correto:
            break
    return valor


linha()
print(f'{"Validação de Dados":^61}')
linha()
n = leiaInt('Digite um número: ')
print(f'O número digitado foi: {n}')
