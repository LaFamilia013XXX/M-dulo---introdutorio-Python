lista_teste = [1,2,3,4,5,6,7,8,9,10]

a, b, c, *_, d, f, g, h, i, j = lista_teste

print(a)
print(_)
print(h)

# isso daqui, você usa o end, onde a cada fim do elemento ele irá retornar esse valor.
for valor in lista_teste:
    print(valor, end=',')

# aqui você está fazendo exatamente a mesma coisa, porém usando o sep=""(ele só funciona quando tem vários itens de uma lista em um mesmo print())
print(*lista_teste, sep=',')

# ambos fazem a mesma coisa.
# * ( descompacta a lista, assim permitindo que o operador sep='' funcione. )
