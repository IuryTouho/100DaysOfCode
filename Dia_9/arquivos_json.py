import json
"""
json_data = '{"nome": "João", "idade": 30, "email": "joao@email.com"}'

data = json.loads(json_data)

print(data)
"""

"""
data = {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
}

# transformando o arquivo em json
json_data = json.dumps(data)

# escrevendo os dados em um arquivo
with open("Dia_9/teste.json", "w") as f:
    f.write(json_data)
"""
"""
# Lendo arquivos Json
with open("Dia_9/teste.json", "r") as f:
    data = json.load(f)

print(data)
print(data["nome"])
"""


with open("Dia_9/teste.json", "r") as f:
    data = json.load(f)
#Caso um valor ja citado seja mencionado ele é alterado
data["endereco"] = "Rua qualquer coisa"

print(data)

with open("Dia_9/teste.json", "w") as f:
    json.dump(data, f)


