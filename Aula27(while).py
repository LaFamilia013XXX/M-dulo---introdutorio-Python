# Condição "Continue" neste caso quando ele achar uma condição que bate com o 'if', ele irá retornar para o ínicio do loop, não executando a ação seguinte.
# Cuidado ao usar a palavra "Continue".
contador = 0

while contador <= 100:
    contador+=1

    if contador == 6:
        print(f'Não vou exibir esse parça não {contador}')
        continue
    if contador >= 10 and contador <= 30:
        print(f'Não vou exibir esse parça não {contador}')
        continue

    print(contador)

    if contador == 10:
        break