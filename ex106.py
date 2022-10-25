from time import sleep
cores = {'sem cor': '\033[m',
         'texto azul': '\033[34m',
         'texto vermelho': '\033[31m',
         'texto verde': '\033[32m',
         'fundo branco': '\033[7m'}


def título(msg, cor1='sem cor', cor2='sem cor'):
    print(cores[cor2], '=' * (len(msg) + 8), cores['sem cor'])
    print(f'{cores[cor1]}{msg:^{len(msg) + 8}}{cores["sem cor"]}')
    print(cores[cor2], '=' * (len(msg) + 8), cores['sem cor'])


def ajuda(comando):
    print('ACESSANDO MANUAL', end='')
    sleep(0.4)
    for p in range(3):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(0.4)
    print(f'Manual do comando \'{comando}\' encontrado:')
    sleep(1)
    print(cores['fundo branco'], end='')
    help(comando)
    print(cores['sem cor'])


def encerramento():
    print('ENCERRANDO', end='')
    sleep(0.4)
    for p in range(3):
        print('.', end='')
        sleep(0.4)
    print()
    sleep(0.4)
    título('<<+-<PROGRAMA FINALIZADO>-+>>', 'texto vermelho')


título('Sistema de Ajuda Interativa - Py-Help', 'texto azul', 'texto azul')
while True:
    fb = str(input('Função ou Biblioteca > ')).strip()
    if fb.upper() == 'FIM':
        break
    else:
        ajuda(fb)
encerramento()
