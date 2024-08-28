testo = 1
valor = 1

variavel = 'Carlos' if testo == valor else 'Cesar'
# <valor> if <condição> else <outro coisa>

print(variavel)

digito = 10
# validando o valor

# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)

novo_digito_zero = 0 if digito > 9 else digito

print(novo_digito_zero)
