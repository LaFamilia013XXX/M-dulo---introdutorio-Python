import tabula
import pandas as pd

lista_tabelas = tabula.read_pdf("\\Users\\matheus.nascimento\\Desktop\\Curso Python\\PDF\\ResultadoVale.pdf", pages="10")
print(len(lista_tabelas))

for tabela in lista_tabelas:
    print(tabela.to_string())
    