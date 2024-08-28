cpf = '111.111.111-11' \
    .replace('.', '') \
    .replace('-', '')


nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
contador_um = 10
contador_dois = 11
somador_um = 0
somador_dois = 0


validando = cpf[0] * len(cpf)

if cpf == validando:
     print('Não pode ser sequência de informações')
else:
    for digito in nove_digitos:
        somador_um += int(digito) * contador_um

        contador_um -= 1

    digito_um = (somador_um * 10) % 11

    digito_um = digito_um if digito_um <= 9 else 0

    resultado_digito_2 = 0

    for digito in dez_digitos:
        somador_dois += int(digito) * contador_dois
        contador_dois -= 1

    digito_dois = (somador_dois * 10) % 11

    digito_dois = digito_dois if digito_dois <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_um}{digito_dois}'

    if cpf_gerado == cpf:
        print('CPF válido')
    else:
        print('CPF inválido')