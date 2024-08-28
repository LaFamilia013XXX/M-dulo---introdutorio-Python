lista = [
  ['cesar', 'carlo', 'miguel'],
  ['abulquerque', 'criolo', 'miguel', 'arrudeia'],
  ['matheus', 'carlos', 'cesar']
 ]

for i, valor in enumerate(lista):
    print(f'Número sala: {i}, Alunos: {valor}')
    for i, value in enumerate(valor):
        print(f'Numero chamada: {i+1}, Nome do aluno: {value}')