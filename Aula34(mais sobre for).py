for i in range(5):

    if i == 2:
        print('i é igual a 2')
        continue # aqui você continua o seu laço.

    if i == 8:
        print('i é igual a 8')
        break

    for j in range(1,3):
        print(i, j)

else:
    print('O for foi completado com sucesso.') # Aqui ele será executado pois nenhum dos IF's foi executado antes.



