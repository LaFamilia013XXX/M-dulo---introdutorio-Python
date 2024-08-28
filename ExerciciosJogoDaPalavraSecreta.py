
# import os

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# tentativas = 0
# palavra_formada = ''

# while palavra_formada != palavra_secreta:

#     letra_digitada = input('Digite uma letra: ')

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra')

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra in palavra_secreta:
#         if letra in letras_acertadas:
#             palavra_formada+=letra
#         else:
#             palavra_formada+='*'
    
#     tentativas+=1

#     print(palavra_formada)


# print(f'Você precisou de {tentativas} tentativas para acertas a palavra: {palavra_secreta}')

import os

palavra_secreta = 'jurema'
letra_acertadas = ''
deseja = ''
tentativa = 0

while deseja != 'n':

    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in letra_acertadas:
        print('Você já digitou está letra, por tanto não será contado essa tentativa.')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertadas+=letra_digitada


    palavra_mesclada = ''

    for letra in palavra_secreta:
        if letra in letra_acertadas:
            palavra_mesclada+=letra
        else:
            palavra_mesclada+='*'

    tentativa+=1

    if palavra_mesclada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!')
        

    print(f'Você está na sua {tentativa}, palavra secreta: {palavra_mesclada}')


    














































































