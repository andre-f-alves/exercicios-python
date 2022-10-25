from ex115.Biblioteca.Interface import cor, linha, leiaInt


def verificador(arquivo):
    """
    -> Verifica se um arquivo existe ou não.
    :param arquivo: Recebe o nome e o tipo do arquivo.
    :return: Retorna "False" (falso) se o arquivo não existir ou não for encontrado.
    Retorna "True" se o arquivo for encontrado
    """
    try:
        arq = open(arquivo, 'r')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def abridor(arquivo):
    """
    -> Cria um arquivo.
    :param arquivo: Recebe o nome e o tipo do arquivo.
    :return: sem retorno.
    """
    try:
        arq = open(arquivo, 'x')
        arq.close()
    except:
        print(cor('vermelho'), 'ERRO: falha na criação do arquivo.', cor())
    else:
        print(cor('verde'), 'Arquivo criado com êxito.', cor())


def leitor(arquivo):
    """
    -> Abre um arquivo para leitura, ou visualização, em formato tabular.
    :param arquivo: Recebe o nome e o tipo do arquivo.
    :return: sem retorno.
    """
    try:
        arq = open(arquivo, 'r')
        for lin in arq:
            dados = lin.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>25} anos')
        arq.close()
        linha(cor_linha='vermelho')
    except:
        print(cor('vermelho'), f'ERRO: falha ao ler o arquivo.', cor())


def cadastrar(arquivo):
    """
    -> Cadastra o nome e a idade de uma pessoa e guarda as informações em um arquivo.
    :param arquivo: Recebe o nome do arquivo.
    :return: sem retorno.
    """
    while True:
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('idade: ')
        if nome in '':
            nome = '<desconhecido>'
        try:
            arq = open(arquivo, 'a')
            arq.write(f'{nome};{idade}\n')
            arq.close()
        except:
            print(cor('vermelho'), 'ERRO: falha ao registrar as informações.', cor())
        else:
            print(cor('verde'), 'Informações registradas com sucesso.', cor())
        while True:
            linha(10, 'magenta')
            resp = str(input('Quer continuar? (S/N) ')).strip().upper()
            linha(10, 'magenta')
            if resp in 'S' or resp in 'N':
                break
            print(cor('vermelho'), 'ERRO: digite apenas "S" para "sim" ou "N" para "não".', cor())
        if resp in 'N':
            break
