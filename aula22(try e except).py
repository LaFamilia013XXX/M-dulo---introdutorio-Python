numero = input('Digite um valor: ')

# Fail-fast: é o conceito de quando o queremos errar o mais rápido possível.

try:
    numero = int(numero)
    print(f'{numero*10}')
except:
    print("Aqui não reconheceu o número")
    print(numero.isalpha())