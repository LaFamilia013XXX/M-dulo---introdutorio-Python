# 'not in' ("Não está entre")
# 'in' não está.
# Strings em python são interáveis;

nome = 'matheus'

print(nome[0]) # Aqui você está acessando a primeira letra, onde você pode usar tanto valores positivos como negativos. 
print(nome[-1]) # independente do tamamho do nome, você sempre estará pegando o último valor.

print('ath' in nome) # verificando se a letra 'a' está entre as letras do nome, podendo ver tambem ver sequências de letras.

nomePerson = input("Digite um nome: ")
encontrar = input("Digite o que deseja encontrar: ")

print(encontrar not in nomePerson) # Aqui você está verificando se a letra digitada nãoi está, se sim a resposta sewrá "False".
print(encontrar in nomePerson) # Aqui você está verificando se a letra digitada está na palavra, se sim ele irá retornar um "True".





 
