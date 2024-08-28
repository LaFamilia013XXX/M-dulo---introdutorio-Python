# build-in Types ---> Tipo embutido.
# Dados imutáveis --> String, Int, Float, Bool ( Todos são objetos que tem Metódos)

variavel_um = 'matheus nascimento'
variavel_dois = f'ABC{variavel_um[3:]}'

print(variavel_dois)
print(variavel_um.capitalize()) # Primeira letra maiúscula.
print(variavel_um.count('a')) # quantas vezes determinada string aparece no na palavra.
print(variavel_um.find('t')) # Encontra uma palavra.
print(variavel_um.zfill(100)) # Caso a string não atenda ao tamanho informado dentro do parâmetro, ele irá preencher com zeros a esquerda ou a direita.

# variavel_um[0] = 'M' # não é possível porque este tipo ele é imutável.
