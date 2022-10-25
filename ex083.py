print('=-=' * 18)
print(f'{"Analisador de Expressões Matemáticas":^55}')
print('=-=' * 18)
expr = str(input('Digite uma expressão: '))
parent = list()
for p in expr:
    if p == '(':
        parent.append('(')
    elif p == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break
if len(parent) == 0:
    print('Sua expressão é \033[32mVÁLIDA\033[m!')
else:
    print('Sua expressão está \033[31mINVÁLIDA\033[m!')
