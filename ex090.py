print('=-=' * 13)
print(f'{"Boletim v4.0":^40}')
print('=-=' * 13)
boletim = dict()
boletim['Nome'] = str(input('Nome do aluno: ')).strip()
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] < 5.0:
    boletim['Situação'] = 'REPROVADO'
elif boletim['Média'] < 7.0:
    boletim['Situação'] = 'RECUPERAÇÃO'
else:
    boletim['Situação'] = 'APROVADO'
print('=-=' * 13)
for c, v in boletim.items():
    print(f'  - {c} = {v}')
