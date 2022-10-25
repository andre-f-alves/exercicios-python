print('Classificação de atletas de natação')
from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print('De acordo com a data de nascimento, o atleta tem {} anos'.format(idade))
print('Sua classificação é:')
if idade <= 9:
    print('\033[1;32mMIRIM!\033[m')
elif idade <= 14:
    print('\033[1;36mINFANTIL!\033[m')
elif idade <= 19:
    print('\033[1;34mJUNIOR!\033[m')
elif idade <= 25:
    print('\033[1;35mSÊNIOR!\033[m')
else:
    print('\033[1;31mMASTER!\033[m')
print('Tenha um bom dia!')
