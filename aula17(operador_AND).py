
sair = 'n'

while(True):
    sair = input("deseja sair [S/N]: ")
    
    if(sair == 's'):
        break
    if(not sair):
        print("Você não digitou nada!")

    senha = int(input("Digite um valor: "))

    if(senha >= 10 and senha <= 12):
        print(f'Tudo fino papai {senha}')
    else:
        print(f'Não tá dando tudo certo papai {senha}')

    
    


