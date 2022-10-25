print('Procurando uma string dentro de outra')
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.title()
print('Tem "Silva" no nome? {}'.format('Silva' in n))
