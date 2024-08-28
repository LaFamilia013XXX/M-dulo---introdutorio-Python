# While Else --> Quando o laço for completado sem interrupções(flags, break etc...), ele exibe o 'Else'


texto = input('Digite uma frase/palavra: ')
i = 0

while i < len(texto):
    
    # if texto[i] == ' ':
    #     print('É uma frase.')
    #     break
    # i+=1

    if ' ' in texto:
        print('É uma frase.')
        break

    i+=1

else:
    print('É uma palavra.')