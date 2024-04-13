import pandas as pd
nome = {'nome':['Fabiana', 'Diana', 'Amanda'],
'idade':['14', '42', '31']}
dataframe = pd.DataFrame(nome)
dataframe.to_excel('Dia_9/excel1.xlsx')