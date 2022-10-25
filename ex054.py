print('Grupo da maioridade')
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for p in range(1, 8):
    dn = int(input('data de nascimento da {}ª pessoa: '.format(p)))
    maioridade = atual - dn
    if maioridade >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são menores de idade enquanto {} já atingiram a maioridade.'.format(menores, maiores))
