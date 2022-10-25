print('=' * 40)
print(f'{"Bem Barato":^40}')
print('=' * 40)
cont = soma = menor = maior = quant = 0
barato = ''
while True:
    produto = str(input('Informe o produto: ')).strip()
    preço = float(input('Informe o preço: R$'))
    soma += preço
    quant += 1
    if preço > 1000:
        cont += 1
    if quant == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    print('-=-' * 14)
    if resp in 'Nn':
        break
print(f'''O total da compra é R${soma:.2f}.
{cont} produtos custam mais de R$1.000,00.
{barato} é o produto mais barato, custando R${menor:.2f}.''')
