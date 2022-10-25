def linha():
    print('=-=' * 9)


def área(larg, comp):
    tam = larg * comp
    print(f'Um terreno de dimensão {larg:.2f}m x {comp:.2f}m tem a área de {tam:.2f}m²')


linha()
print(f'{"Cálculo de Área":^28}')
linha()
l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
área(l, c)
