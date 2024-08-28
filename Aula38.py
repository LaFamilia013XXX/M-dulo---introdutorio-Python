# # Tuplas --> É exatamente igual a uma lista como outra qualquer. porém imutavel.
# # Ela é mais eficiente que uma list.

# tupla = ('matheus', 'helena', 10)
# print(tupla[0])


# lista = [1,2,3,4]
# lista = tuple(lista)

# print(lista) # Você transformou uma lista em uma tupla.

# # tupla[0] = '10' # você não pode substituir os valores de dentro de uma tupla.
# print(tupla)














# tupla

nomes = ['matheus', 'cesar', 'carlos'] # tipo de dado imutável

# conversão

print(type(nomes))


nomes = tuple(nomes)

print(type(nomes))

nomes = list(nomes)

print(type(nomes))

# nomes.pop() # não funciona porque tuplas são um tipo de dado mutável.

print(nomes)



