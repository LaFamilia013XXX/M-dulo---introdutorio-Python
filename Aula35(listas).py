'''
Listas em python
Tipo list - mutável !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis - índices e fatiamento.
Metódos úteis: append, insert, pop, del, clear, extend +


falsy - é quando você tem um tipo dado como falso nativamente, por exemplo: variáveis vázias.

Create Read Update Delete - (Conhecido como CRUD, todo esse processo é possível com listas.)

No processo de exclusão, evite ao máximo a troca de indices.
O principal objetivo da lista é adicionar e trocar valores, onde adiciona sempre no fim dela.

'''


string = 'ABCDE'

lista = list('matheus')
lista_02 = ['m','a','t','h','e','u','s']
lista_03 = []

lista_04_multiple_types = [1, 'matheus', 1.4, True] # mesclando vários tipos de valores.

indice = lista_04_multiple_types[1][1] # Acessando um item da lista, e descadeado uma única string.

lista_04_multiple_types[0] = 'velho senhor'



print(indice)

print(lista)
print(lista_02)

print(bool(lista_03))

print(lista_04_multiple_types)

del lista_04_multiple_types[0]

lista_04_multiple_types.append('Velho chico') # adicionando valores.

print(lista_04_multiple_types)

valor_removido = lista_04_multiple_types.pop() # remove o último valor da lista, sendo possível colocar o indice que você deseja remover no pop(2);

print(lista_04_multiple_types, f'valor removido: {valor_removido}')

lista_04_multiple_types.insert(0, 'teste') # adicionando valor no meio da lista, (altera a ordem da lista)
# Caso você indicar um indice muito grande, ele irá adicionar sempre no final da lista.
# lista_04_multiple_types.clear() # Zera toda a lista

try:
    indice_01 = int(input(('Digite um valor: ')))

    print(lista_04_multiple_types[indice_01])

except:
    print('Error: Este indice não existe.')


print(lista_04_multiple_types)


lista_01 = ['matheus', 'cesar']
lista_04 = ['Cesar', 'marcela']

print(lista_01+lista_02) # Literalmente você apenas juntou os dois, realizando a contacatenação, porém você não está salvando.
print(lista_01)

lista_01.extend(lista_02) # neste caso além de concatenar você está salvando na lista_01, ou seja, ela passa a ter esse novo formato.
