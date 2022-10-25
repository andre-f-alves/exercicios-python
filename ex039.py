print('Alistamento militar')
fm = int(input('''[1] para MASCULINO
[2] para FEMININO
Informe seu sexo: '''))
if fm == 2:
    print('Você não precisa se alistar.')
elif fm == 1:
    from datetime import date
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você deve se alistar este ano.')
    elif idade < 18:
        alistamento = 18 - idade
        print('Ainda faltam {} anos para seu alistamento.'.format(alistamento))
        tempo = atual + alistamento
        print('Seu alistemento será no ano de {}.'.format(tempo))
    else:
        alistamento = idade - 18
        print('Seu alistamento deveria ser feito há {} anos.'.format(alistamento))
        tempo = atual - alistamento
        print('Seu alistamento foi em {}.'.format(tempo))
    print('Se você for Testemunha de Jeová, faça o pedido de eximição.')
else:
    print('Opção inválida. Tente novamente.')
