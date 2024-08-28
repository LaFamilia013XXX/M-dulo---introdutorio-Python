valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite um segundo valor: "))

if(valor_1 > valor_2):
    print('O valor_1: {teste01} é maior que o valor_2: {teste02}'.format(teste01=valor_1,teste02=valor_2))
else:
    print('O valor_2: {} é maior que o valor_1: {}'.format(valor_2,valor_1))

print(f'O valor {valor_1}') #Usando variaveis no meio do codigo;
