def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
        except:
            print(f'\033[1;31mERRO: digite um número inteiro válido.\033[m')
        else:
            return valor


def leiaFloat(numr):
    while True:
        try:
            valor = float(input(numr))
        except:
            print(f'\033[1;31mERRO: digite um número real válido.\033[m')
        else:
            return valor


ni = leiaInt('Digite um número inteiro: ')
nr = leiaFloat('Digite um número real: ')
print(f'Número inteiro digitado: {ni}')
print(f'Número real digitado: {nr}')
