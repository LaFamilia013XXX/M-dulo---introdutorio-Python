lista = ['Matheus', 'Helena', 'Luiz']

indice = range(len(lista))

# lista.append('cesar')
lista.insert(1, 'Agenor')
lista.pop()


for numero in indice:
    print(f'Indice: {numero}, valor: {lista[numero]}')
