print('Validação de dados')
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'MF':
        s = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Dados registrados com sucesso!')
