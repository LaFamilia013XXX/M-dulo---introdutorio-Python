# frase = 'caqrloss cesaraasaaaqsaaas'

# letras_alphabeto = 'abcdefghijklmnopqrstuzwxyzçãé'

# i_um = 0
# letra_mais_vezes = 0
# letra_interando = 0
# letra_maior_ocorrencia = ''
# letra_verificada = ''

# while i_um < len(letras_alphabeto):
#     letra_verificada = letras_alphabeto[i_um]
#     letra_interando=frase.count(letra_verificada)

#     if letra_interando > letra_mais_vezes:
#         letra_mais_vezes = letra_interando
#         letra_maior_ocorrencia = letras_alphabeto[i_um]
#     i_um+=1

# print(f'A letra {letra_maior_ocorrencia.upper()} aparece {letra_mais_vezes} vezes na frase')


palavra_escolhida = 'matheuss'

letras_alfabeto = 'abcdefghijklmnopqrstuvwxyz'

qtd_letras_total = 0
qtd_letra_contando = 0

letra = 'a'

i = 0

while i < len(letras_alfabeto):
    letra_analisada = letras_alfabeto[i]

    qtd_letra_contando = palavra_escolhida.count(letra_analisada)

    if qtd_letra_contando > qtd_letras_total:
        qtd_letras_total = qtd_letra_contando
        letra = letra_analisada

    i=i+1

print(f'A letra com maior ocorrência é {letra} com {qtd_letras_total}.')

    
























