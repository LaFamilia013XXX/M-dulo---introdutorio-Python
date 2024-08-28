nome = input('Digite o seu nome: ')
contador = 0
nova_variavel = ''

# 'm*a*t*h*e*u*s'

while contador <= len(nome):
    adicionando_asterico = f'{nome[contador-1:contador]}*'
    nova_variavel += adicionando_asterico
    contador+=1
    
print(nova_variavel)