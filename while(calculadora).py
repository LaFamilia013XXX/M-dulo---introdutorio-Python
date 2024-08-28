sair = True

while sair is True:
    numero_um = input('Digite um valor: ')
    numero_dois = input('Digite um segundo valor: ')

    try:
        numero_um = int(numero_um)
        numero_dois = int(numero_dois)
    except:
        print('Um ou ambos os valores são invalidos.')

    operacoes_permitidas = '+-/*'

    operacao = input(f'Digite uma operação, dentre essas ( {operacoes_permitidas} ): ')

    if operacao not in operacoes_permitidas:
        print('Por favor digite uma oepração dentre as escolhidas.')
    if len(operacao) > 1:
        print('Digite apenas um operador.')

    ... # toda aquela parte chata de calculadora que você já



    

    # sair = input('Deseja sair do calculadora? [S/N]: ').lower().startswith('s')

