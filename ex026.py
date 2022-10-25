print('Primeira e última ocorrência de uma strig')
frase = str(input('Digite uma frase: ')).strip().upper()
print(f"""A letra "A" aparece {frase.count('A')} vezes na frase
A letra "A" aparece a primeira vez na posição {frase.find('A') + 1}
A letra "A" aparece a última vez na posição {frase.rfind('A') + 1}""")
