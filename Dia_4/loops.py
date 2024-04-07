"""
i = 1

while i < 10:
    print(i)
    i += 1

print(i)
print("Terminou")

"""
"""
criancas = ["a","g","k"]


for item in criancas:
    print(item)

"""
"""
frase = "você sabia que string é um vetor?"

for letra in frase:
    print(letra)

# esse range cria um vetor de até 20
for index in range(20):
    print(index)

# Se pode controlar o inicio do vetor
for index in range(7,10):
    print(index)
# Se pode passar de quantos em quantos valores o for vai pulando 
for index  in range(2,20,2):
    print(index)

"""
"""
criancas = ["april","may","Karen"]

for index  in range(len(criancas)):
    print(criancas[index])
    print(index)
"""

matriz_bingo = [
    [1,2,4],
    [9,5,7],
    [0,2,7]
]

for linha in matriz_bingo:
    for item in linha:
        print(item)