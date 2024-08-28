# lista = ['matheus', 'lucas', 'cesar', 'Maycon']

# '''
# O que o Enumarate faz?

# - Ele enumera cada item da sua lista?
# - Você pode definir de onde ele irá começar a enumerar os valores de onde você deseja que ele comece a contar Enumerate(lista, start=10)
# - 

# '''

# lista_enumerada = enumerate(lista) # Aqui você criou o Enumerate da sua lista.

# # enumerate_to_list = list(lista_enumerada) # Neste ponto você transformou o seu enumerate em uma lista.

# # print(enumerate_to_list)

# # enumerate_to_list[0] = '10'

# # print(enumerate_to_list) # Como você transformou o enumerate em list, agora você pode alterar os seus valores.

# # enumerate_to_list = tuple(enumerate_to_list)

# # print(enumerate_to_list) # Aqui você transformou ela em tuple, portanto você não consegue mais alterar os valores dela.

# # for indice, valor in lista_enumerada:
# #     print(f'Indice: {indice}, valor: {valor}')

# for item in lista_enumerada:
#     print('For da Tupla: ')
#     for indice in item:
#         print(f'\t{indice}')

# # O iterator é consumível, ou seja após o seu uso, ele zera novamente.

# # for item in lista_enumerada:
# #     print(item)


# # for item in enumerate(lista):
# #     print(item)

# # print('Neste caso você está criando dinamicamente inúmeros Enumarate(iterator)')

# # for item in enumerate(lista):
# #     print(item)




lista = ['Matheus', 'Helena', 'Luiz']

# lista.append('cesar')

lista_enumerada = enumerate(lista) # exibe o endereço de memória da lista.
print(lista_enumerada)

# for i in lista_enumerada:
#     print(i)

# não acontece nada, pois o ponteiro já andou e não tem mais para onde ir.
# for i in lista_enumerada:
#     print(i)

# agora aqui você já consegue usar repetidas vezes o enumerate, porque o ponteiro toda vez é reiniciado.
# for i in enumerate(lista):
#     print(i)

# print(lista_enumerada) # esse tipo de objetivo é um interator.

# Você pode realizar a conversão do ENUMERATE para uma lista tbm, sendo assim você pode acessar os dados.

for i in list(enumerate(lista)):
    print(i)

# Aqui ele cria um tupla com o indice, já que praticamente não iremos alterar os indices, por isso ele cria uma tupla.
lista_pegando_indice = list(enumerate(lista))

for indice, nome in lista_pegando_indice:
    # a, i = item # aqui ele já faz naturalmente no próprio for.
    print(f'\tIndice do valor: {indice}, Valor da lista: {nome}')

# \t é considerado um TAB
 
