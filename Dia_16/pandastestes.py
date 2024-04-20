import pandas as pd

#dataframe = pd.DataFrame()
"""
venda = {
    'data': ['15/02/2021','16/02/2021'],
    'valor': [500,300],
    'produto': ['feijão','arroz'],
    'qtde': [50,70],
        }
vendas_df = pd.DataFrame(venda)

print(vendas_df )
"""

vendas_df = pd.read_excel("Dia_16/Vendas.xlsx")
# mostra os 10 primeriros
print(vendas_df.head(10) )

# resume as planilhastrazendo quantidade de linhas, medias, minimo, maximo e etc
print(vendas_df.describe() )

print(vendas_df.shape)

produtos = vendas_df['Produto']

print(produtos)