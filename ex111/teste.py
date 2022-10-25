from ex111.utilidadesCeV.moeda import moeda
valor = float(input('Digite um valor monetário: R$'))
taxa1 = int(input('Taxa de aumento: '))
taxa2 = int(input('Taxa de desconto: '))
moeda.resumo(valor, taxa1, taxa2)
