nomes = ['matheus', 'cesar', 'helena', 'Luiz']

n1, n2, n3, n4 = nomes # Neste caso só irá funcionar se você digitar o número de variáveis de acordo com o tamanho da lista.
# n1, *_ = nomes # neste caso você já está pegando todos os valores restantes.
_, _, _, n10 = nomes # Pegando os valores mais centralizados.

# nome1, *_ = nomes
*_, nome1 = nomes

print(nome1) # contrário funciona tbm.

# Variável '_' significa que é uma convenção dos programadores, que essa variável está ali, porém você não está usando ela.

