print('\033[34mRadar eletrônico\033[m')
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[4;1;31mMULTADO!\033[m\nVocê excedeu o limite de velocidade de 80km/h e recebeu uma multa de \033[31mR${:.2f}.\033[m'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
