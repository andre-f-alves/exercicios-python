from ex115.Biblioteca.Interface import *
from ex115.Biblioteca.Arquivo import *
a = 'Arquivo de Cadastros.txt'
if not verificador(a):
    abridor(a)
cabeçalho('Sistema de Cadastros', cor_txt='azul', cor_linha_cabeçalho='magenta')
while True:
    resp = menu(['Cadastrar uma pessoa', 'Mostrar pessoas cadastradas', 'Sair do programa'])
    if resp == 1:
        cabeçalho('Novo Cadastro', cor_txt='ciano', cor_linha_cabeçalho='vermelho')
        cadastrar(a)
    elif resp == 2:
        cabeçalho('Pessoas Cadastradas', cor_txt='ciano', cor_linha_cabeçalho='vermelho')
        leitor(a)
    else:
        break
sair(cor_msg1='ciano', cor_msg2='vermelho', cor_linha_msg2='magenta')
