print('Detector de palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[:: - 1]
'''inverso = ''
for l in range(len(junto) - 1, - 1, - 1):
    inverso += junto[l]'''
print('O invreso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Essa frase \033[32mé um palíndromo\033[m.')
else:
    print('Essa frase \033[31mnão é um palíndromo\033[m.')
