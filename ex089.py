print('=-=' * 13)
print(f'{"Boletim v3.0":^40}')
print('=-=' * 13)
from time import sleep
boletim = list()
while True:
    nome = str(input('Nome do(a) aluno(a): ')).strip()
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    média = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], média])
    print('-=-' * 8)
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    print('-=-' * 8)
    if r in 'N':
        break
print('=' * 39)
print(f'{"Nº":<8}{"Nome":<18}{"Média":>13}')
for n, b in enumerate(boletim):
    print(f'{n + 1:<8}{b[0]:<18}{b[2]:>13.1f}')
print('-' * 39)
print('=-=' * 13)
while True:
    o = int(input('Deseja ver as notas de qual aluno? (999 interrompe) '))
    if o == 999:
        break
    else:
        if o <= len(boletim):
            print(f'{boletim[o - 1][0]} - Notas: {boletim[o - 1][1]}')
        else:
            print('Aluno não cadstrado. Tente novamente.')
    print('=-=' * 13)
print('=-=' * 13)
print('ENCERRANDO PROGRAMA...')
sleep(1)
print('PROGRAMA FINALIZADO. Volte sempre!')
