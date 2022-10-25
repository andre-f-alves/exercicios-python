print('Sorteando uma ordem na lista')
from random import shuffle
a1 = input('Primeiro(a) aluno(a): ')
a2 = input('Segundo(a) aluno(a): ')
a3 = input('Terceiro(a) aluno(a): ')
a4 = input('Quarto(a) aluno(a): ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de alunos para a apresentação do trabalho é:\n{}'.format(lista))
