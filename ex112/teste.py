from ex112.utilidadesCeV.moeda import moeda
from ex112.utilidadesCeV.dado import dado
valor = dado.leiaDinheiro('Digite um valor monetário: R$')
taxa1 = int(input('Taxa de aumento: '))
taxa2 = int(input('Taxa de desconto: '))
moeda.resumo(valor, taxa1, taxa2)
