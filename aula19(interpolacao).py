nome = 'Luis'
preco = 1000.95121
preco_1 = 102948756739021124312
variavel_texto = '%s, o preço total da compra deu R$%.2f' % (nome, preco) # interpolacao (Lembra muito a linguagem C)

print(variavel_texto)
print('O hexadecimal de %d é %x' % (10, 10) )

# """
# String ---> '%s'
# int ---> '%d' ou '%i'
# float --> '%f'
# Hexadecimal --> x e X  // Não funciona em números Float

# """

varial_texto = '%s %f %017X' % (nome, preco, preco_1) # aqui você definiu para preencher 17 zeros a frente do número hexadecimal.

print(varial_texto)