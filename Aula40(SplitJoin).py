frase = '  teste  , testando    '
lista_frases_vazia = frase.split(',')

# você splita a frase de acordo com o espaço, caso o parâmetro for null, caso você especificar, você irá splitar de acordo o valor abaixo.
# print(frase.split(','))
lista_palavras = []

# aqui ele gera um indice para cada elemento da da lista
for i, frase in enumerate(lista_frases_vazia):
    # neste caso você está apenas desestruturando.
    lista_palavras.append(lista_frases_vazia[i].strip())
    # corta os espações do começo e fim da string

# for frase in lista_palavras:
#     print(frase)

# O primeiro loop é mais complexo, mas permite acesso ao índice i além do valor frase.

# aqui você consertou esse B.O
print(lista_palavras)

# strip() --> corta os espaços do começo e fim da string.
# lstrip() --> corta os espaços da esquerda.
# rstrip() --> corta os espaços da direita.

# Evite de alterar o valor mutável de um código.

# '-', aqui você define como você gostaria de escolher a forma que ele irá juntar os valores.
frases_unidas = '-'.join(lista_palavras) # aqui poderia ser qualquer valor, sendo lista ou não.
print(frases_unidas)