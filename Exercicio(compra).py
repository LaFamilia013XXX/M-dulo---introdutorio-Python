
# import os

# opc = ''
# lista = ['matheus', 'cesar']

# while True:
#     print('[i] inserir')
#     print('[a] apagar')
#     print('[l] listar')

#     opc = input('Digite a inicial da ação que deseja realizar: ')

#     os.system('cls')

#     if opc == 'i':
#         produto = input('Digite o nome do produto: ')
#         lista.append(produto)
#         continue

#     if opc == 'l':

#         enumerador = enumerate(lista)

#         for indice, valor in enumerador:
#             print(indice, valor)
        
#         continue

#     if opc == 'a':

#         try:
#             indice = int(input('Digite o valor o qual deseja apagar: '))

#             del lista[indice]
#         except:
#             print('Por favor, digite um valor/indice válido.')
#             continue


import os
import time


lista_compras = []

while True:

    lista_opcoes = ['[1] - Inserir', '[2] - Apagar', '[3] - listar valores']
    print("Escolha a sua opção: ")
    for item in lista_opcoes:
        print(item)
    opc = int(input(": "))
    
    if opc == 1:
        valor_insert = input("Digite o valor para ser adicionado na lista de compras: ")
        try:
            lista_compras.append(valor_insert)
            print(f"{valor_insert} adicionado com sucesso!")
        except:
            print(f"Erro ao adicionar {valor_insert} na lista, favor informar o desenvolvedor.")
        
        time.sleep(2)
        os.system("cls")
    if opc == 2:
        if(len(lista_compras) == 0):
            print("Você ainda não adicionou nenhum item a lista")
            time.sleep(2)
            os.system("cls")
        else:

            for indice, item in list(enumerate(lista_compras)):
                print(f'Indice: {indice} / Produto: {item}')

            try:
                valor_delete = int(input("Digite o indice a ser excluido: "))
            except TypeError:
                print('Digite um valor inteiro!')
                continue

            del lista_compras[valor_delete]

            print(f'Valor deletado com sucesso: {valor_delete}')
            time.sleep(1)
            os.system("cls")
    
    if opc == 3:

        if len(lista_compras) == 0:
            print('Você ainda não adicionou nenhum item a lista')
            time.sleep(1)
            os.system("cls")
            continue
        else:
            for indice, valor in list(enumerate(lista_compras)):
                print(f'Indice: {indice}, produto: {valor}')

            press = input("Pressione enter para sair!")
            os.system("cls")
            continue
            


    
