# Iterável --> str, range etc (__iter__)
# (__iter__) --> ele te retorna o iterator ou seja  próprio objeto.
# por de baixo dos panos o "__iter__" já é chamado automáticamente, ou seja quando declaramos uma STR ele já vem junto, asism posbilitando o uso dos seus metódos.
# next --> ele é o responsável por iterar a memória do computador, assim entregando o valor desejado.

# metódos --> funções do objeto.

texto = iter('matheus')

print(texto.__next__())
print(next(texto));


texto_2 = 'matheus'
interador = iter(texto_2)

# while True:
#     try:
#         print(next(interador))
#     except StopIteration:
#         print('Deu erro menor')
#         break

# Literalmente o que você fez acima está basicamente fazendo um for.

for letra in texto_2:
    print(letra)

