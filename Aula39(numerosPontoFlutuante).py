# solução do problema --> Double-precision floating-point format IEEE 754;

# importante para pegar valores extremamentes especificos.

import decimal as teste

numero_1 = teste.Decimal(0.1)
numero_2 = teste.Decimal(0.7)

print(numero_1)
print(numero_2)

numero_3 = numero_1 + numero_2

# Como contornar a situação, essa é a primeira.
print(f'{numero_3:.2f}')

# round() recebe dois argumentos, ele recebe o valor para ser formatado, e após isso você escolhe as casas deciamsis.
print(type(round(numero_3, 2)))


