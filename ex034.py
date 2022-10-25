print('Reajuste salarial')
salário = float(input('Atual salário do funcionário: R$'))
if salário <= 1250.00:
    aumento1 = salário + (salário * 15 / 100)
    print('Este funcionário receberá um salário de \033[32mR${:.2f}\033[m com um aumento de \033[32m15%\033[m.'.format(aumento1))
else:
    aumento2 = salário + (salário * 10 / 100)
    print('Com um aumento de \033[32m10%\033[m, este funcionário terá um salário de \033[32mR${:.2f}\033[m.'.format(aumento2))
