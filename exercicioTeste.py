numero = input("Digite um valor: ")

try:
    numero = int(numero)
    tipo_numero = "par"
    validando_numero = (numero % 2) == 0

    if( validando_numero is False): tipo_numero = "ímpar"

    print(f'O número digitado é um valor {tipo_numero}')
except:
    print("O valor digitado não e um número inteiro")










10






















# numero = input("Digite um valor inteiro: ")

# try:
#     numero_inteiro = int(numero)
#     validando_numero_par = (numero_inteiro % 2) == 0

#     numero_tipo = 'par'
#     if( numero_tipo is False): numero_inteiro = 'impar'

#     print(f'O valor digitado: {numero_inteiro} é do tipo ')

# except:
#     print("Não é um número inteiro.")