print('Boletim ')
nota1 = float(input('Primeira nota do bimestre: '))
nota2 = float(input('Segunda nota do bimestre: '))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('\033[1;31mREPROVADO!\033[m\nSua média foi {} e você foi reprovado! Estude mais da próxima vez!'.format(média))
elif média <= 7.0:
    print('\033[1;34mRECUPERAÇÃO!\033[mSua média foi de {} e por isso ficará de recuperação'.format(média))
else:
    print('\033[1;32mAPROVADO!\033[m\nParabéns, sua média foi {} e você passou de ano, continue assim!'.format(média))
print('Tenha um bom dia e bons estudos!')
