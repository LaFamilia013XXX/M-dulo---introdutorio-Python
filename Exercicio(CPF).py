import random as teste
import os

cpf_matheus = ''


while True:
    print("[G]erar cpf")
    print("[V]alidar cpf")

    opc = input("Digite: ").lower()
    
    if opc == 'g':
        for i in range(9):
            valor = str(teste.randrange(0, 10))
            cpf_matheus += valor
    if opc == 'v':
        cpf_matheus = input('Digite o CPF, atenção somente números: ')

    lista_somente_numeros = []
    somando = 0

    digito_um = ''
    digito_dois = ''
    valor_range = 10

    while digito_um == '' or digito_dois == '':

        if digito_um == '':
            for item in cpf_matheus:
                try:
                    valor = int(item)
                    lista_somente_numeros.append(item)
                except:
                    continue
        
        if digito_um != '':
            valor_range = 11
            lista_somente_numeros.append(digito_um)

        dados = enumerate(lista_somente_numeros)

        for i in range(valor_range, 1, -1):
            valor_multiplicado = int(next(dados)[1]) * i
            somando += valor_multiplicado
            
        realizando_conta = (somando * 10) % 11

        if digito_um != '':
            digito_dois = realizando_conta if realizando_conta <= 9 else 0
        
        if digito_um == '':
            digito_um = realizando_conta if realizando_conta <= 9 else 0

        somando = 0

    if opc == 'g':
        print(f'CPF gerado: {cpf_matheus}-{digito_um}{digito_dois}')
        enter = input('pressione enter para continuar')
        os.system('cls')
    
    if opc == 'v':
        validando_um = int(cpf_matheus[-2])
        validando_dois = int(cpf_matheus[-1])

        if (validando_um != digito_um) or (validando_dois != digito_dois):
            print("CPF invalido")
        else:
            print('CPF válido')
        
        enter = input('pressione enter para continuar')
        os.system('cls')
    
    cpf_matheus = ''


# Explicação:

# range(10, 0, -1):
# 10 é o ponto inicial (inclusive).
# 0 é o ponto final (exclusivo).
# -1 é o passo, indicando que a contagem será feita de forma decrescente.
# Esse loop vai imprimir os números de 10 até 1, decrementando 1 a cada iteração.