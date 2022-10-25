print('\033[32m-=-\033[m' * 10)
print('\033[34mAnalisador de Triângulos v2.0')
print('\033[32m-=-\033[m' * 10)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Analisando os comprimentos, esses segmentos \033[32mPODEM\033[m formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Analisando os comprimentos, esses segmentos \033[31mNÃO PODEM\033[m formar um triângulo.')
