print('Índice de Massa Corporal')
peso = float(input('Informe seu peso: (Kg) '))
altura = float(input('Informe sua altura: (m) '))
IMC = peso / (altura ** 2)
print('Seu IMC é de {:.1f}.'.format(IMC))
if IMC <= 18.5:
    print('Seu peso está ABAIXO DO IDEAL.')
elif IMC <= 25:
    print('Você está com o PESO IDEAL.')
elif IMC <= 30:
    print('Você está com SOBREPESO.')
elif IMC <= 40:
    print('Você está com OBESIDADE.')
else:
    print('Você já está com OBESIDADE MÓRBIDA.')
