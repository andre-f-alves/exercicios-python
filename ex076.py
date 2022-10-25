print('=' * 50)
print(f'{"Lista de compras":^50}')
print('=' * 50)
compras = ('Arroz', 20.00, 'Feijão', 7.00, 'Ovos', 6.00, 'Chocolate', 9.00, 'Café', 7.00, 'Farinha de Trigo', 4.00, 'Leite', 3.40,
           'Fermento', 2.00, 'Pães', 2.00, 'Presunto', 3.50, 'Queijo', 4.00, 'Manteiga', 7.00, 'Alface', 3.50, 'Tomate', 7.00, 'Cenoura', 2.00)
for lista in range(len(compras)):
    if type(compras[lista]) is str:
        print(f'{compras[lista]:.<41}', end='')
    else:
        print(f'R${compras[lista]:.>7.2f}')
print('=' * 50)
