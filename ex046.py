print('Contegem regressiva')
início = str(input('Quer iniciar a contagem regressiva? s/n: '))
if início == 's':
    from time import sleep
    for r in range(10, 0, -1):
        print(r)
        sleep(1)
    print('Thunderbirds are go!')
else:
    print('Contegem regressiva cancelada.')
