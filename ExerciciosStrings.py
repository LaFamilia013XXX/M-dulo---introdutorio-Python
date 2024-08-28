nome = input("Digite o seu nome por gentileza: ")
idade = int(input("Digite a sua idade por gentileza: "))

if(nome and idade):
    print('Seu nome é: %s ' % nome)
    print(f'Seu nome invertido é: {nome[::-1]}')
    if(' ' in nome):
        print('Seu nome contém espaços')
    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print("Seguinte irmão, faz o favor de digitar os dois valores por obséquio")
