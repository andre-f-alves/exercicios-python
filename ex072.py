print('Número por extenso')
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
       'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze/Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Número incorreto. Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número {num} escrito por extenso é: {ext[num]}')
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
