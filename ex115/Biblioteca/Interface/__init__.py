def cor(c='sem cor'):
    """
    -> Função para cores no terminal (utiliza o padrão ANSI).
    :param c: Parâmetro de indicação da cor (opcional).
    :return: Retorna o valor indicado.
    """
    cores = {'sem cor': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
             'azul': '\033[34m', 'magenta': '\033[35m', 'ciano': '\033[36m', 'branco': '\033[97m'}
    return cores[c]


def linha(tam=20, cor_linha='sem cor'):
    """
    -> Mostra uma linha na tela (=-=).
    :param tam: Recebe o tamanho da linha (padrão = 20) (opcional).
    :param cor_linha: Recebe a cor da linha (opcional).
    :return: sem retorno.
    """
    print(f'{cor(cor_linha)}=-=' * tam, cor())


def cabeçalho(txt, centralizar_txt=58, tam_linha=20, cor_linha_cabeçalho='sem cor', cor_txt='sem cor'):
    """
    -> Cria um texto personalizado (cabeçalho).
    :param txt: Recebe o texto que será exibido.
    :param centralizar_txt: Recebe o número de caracteres para a centralização do texto (padrão = 60) (opcional).
    :param tam_linha: Recebe o tamanho da linha (padrão = 20) (opcional).
    :param cor_linha_cabeçalho: Recebe a cor da linha do cabeçalho (opcional).
    :param cor_txt: Recebe a cor do texto (opcional).
    :return: sem retorno.
    """
    linha(tam_linha, cor_linha_cabeçalho)
    print(cor(cor_txt), txt.center(centralizar_txt), cor())
    linha(tam_linha, cor_linha_cabeçalho)


def leiaInt(num):
    """
    -> Analisa se o número digitado é inteiro ou não.
    :param num: Parâmetro de recepção do número digitado.
    :return: Retorna o número inteiro digitado.
    """
    while True:
        try:
            valor = int(input(num))
        except:
            print(cor('vermelho'), 'ERRO: por favor. digite um número inteiro válido.', cor())
        else:
            return valor


def menu(lista_opções):
    """
    -> Mostra um menu de opções na tela.
    :param lista_opções: Recebe uma lista com as opções.
    :return: sem retorno.
    """
    print(f'{cor("ciano")}Menu de Opções:', cor())
    c = 1
    for opc in lista_opções:
        print(f'    {cor("amarelo")}>-+-> {cor("verde")}[{c}] Opção {c} {cor("ciano")}- {opc}', cor())
        c += 1
    while True:
        opção = leiaInt(f'{cor("amarelo")}>> {cor()}')
        if opção <= 3:
            break
        print(cor('vermelho'), 'ERRO: digite um número equivalente às opções mostradas acima.', cor())
    cabeçalho(f'Opção {opção} - {lista_opções[opção - 1]}', cor_txt='verde', cor_linha_cabeçalho='azul')
    return opção


def sair(msg1='ENCERRANDO', símbolo='.', msg2='<+>--<PROGRAMA ENCERRADO>--<+>', cor_msg1='sem cor', cor_msg2='sem cor',
         cor_linha_msg2='sem cor'):
    """
    -> Gera o encerramento do programa.
    :param msg1: Recebe a primeira mensagem a ser exibida (opcional).
    :param símbolo: Recebe o símbolo de carregamento, que é exibido junto com "msg1" (opcional).
    :param msg2: Recebe a última mensagem a ser exibida (opcional).
    :param cor_msg1: Cor do "msg1" e do "símbolo" (opcional).
    :param cor_msg2: Cor do "msg2" (opcional).
    :param cor_linha_msg2: Cor das linhas exibidas antes e depois de "msg2" (opcional).
    :return: sem retorno.
    """
    from time import sleep
    print(cor(cor_msg1), msg1, end='')
    sleep(0.5)
    for p in range(3):
        print(símbolo, end='')
        sleep(0.5)
    print(cor())
    cabeçalho(msg2, cor_txt=cor_msg2, cor_linha_cabeçalho=cor_linha_msg2)
