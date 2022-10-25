print('Verificando as primeiras letras de um texto')
cidade = str(input('Em que cidade você mora? ')).strip()
c = cidade.title()
print('O nome da cidade começa com "Santo"? {}'.format('Santo' in c))
