def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[1;31mERRO: \"{entrada}\" não é um valor válido!\033[m')
        else:
            válido = True
            return float(entrada)
