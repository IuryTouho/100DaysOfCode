import pandas as pd

tabela = pd.read_excel("Dia_8/testes.xlsx")
# é possivel passar numero das linhas ou parametros das colunas como abaixo
tabela.loc[tabela["idades"]==11,"cores"] = "verde"

tabela.loc[tabela["cores"]=="vermelho","idades"] = 22

print(tabela)

tabela.to_excel("Dia_8/resultados.xlsx")

