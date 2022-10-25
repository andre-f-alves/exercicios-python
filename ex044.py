print('Gerenciador de pagamentos')
valor = float(input('Valor da compra: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO:
[1] à vista com dinheiro/cheque;
[2] à vista no cartão;
[3] 2x no cartão;
[4] 3x ou mais no cartão.
Opção de pagamento: '''))
if pagamento == 1:
    preço = valor - valor * 10 / 100
    print('Você ganhou 10% de desconto, o valor da compra é de R${:.2f}.'.format(preço))
elif pagamento == 2:
    preço = valor - valor * 5 / 100
    print('Você ganhou um desconto de 5%, o valor da compra é de R${:.2f}.'.format(preço))
elif pagamento == 3:
    total = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} mensais sem jurus'.format(total))
elif pagamento == 4:
    parcela = int(input('Quantas vezes no cartão? '))
    preço = valor + valor * 20 /100
    mensal = preço / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% de jurus. O total da compra é de R${:.2f}'.format(parcela, mensal, preço))
else:
    print('Opção inválida. Tente novemente')
