print('\033[33m-=-\033[m' * 10)
print('\033[34mAnalisador de Triângulos v1.0\033[m')
print('\033[33m-=-\033[m' * 10)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segunda segmento: '))
reta3 = float(input('Terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo.')
