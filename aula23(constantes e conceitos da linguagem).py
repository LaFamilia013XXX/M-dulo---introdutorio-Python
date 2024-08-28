# Python não tem o conceito de constante, assim como no JavaScript tem.
# Convenção --> Todas as variáveis que tiverem letras maísculas, elas são conhecidas como constantes, assim não é para alterar o seu valor.
# Quanto mais indentado o seu código é pior.
# "\" você está dizendo pro compilador que o código tem continuação abaixo.

velocidade = 61
local_carro = 98

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

teste_01 = velocidade > RADAR_1
teste_02 = local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    velocidade > RADAR_1


if teste_01:
    print("Carro passou da velocidade máxima permitida no radar_1")
if teste_02:
    print("Multa aplicada")





