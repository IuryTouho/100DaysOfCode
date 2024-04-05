num = 1
num2 = 4.5

#Funções para mostrar tipagem
print(type(num))
print(type(num2))

#Funções de conversão numerica
a = float(num)
print(a)

b = int(num2)
print(b)

# há uma dificuldade para se converter strings, elas devem ter o mesmo tipo do dado, se escrever int("5.2") é gerado erro.

print(num + num2) # adição
print(num - num2) # subtração
print(num * num2) # multiplicação
print(num / num2) # divisão
print(num ** num2) # Exponenciação
print(num % num2) # Mod
print(num // num2) # Divisão sem restos 5/2 dá 2 e não 2.5

print(abs(-15)) # Numero Absoluto, pesquisar sobre, mas retorna 15
print(pow(3,3)) # Exponenciação

print(min(2,5,7)) # Retorna o menor numero de um vetor
print(max(2,5,7)) # Retorna o maior numero de um vetor

print(round(2.3)) # Arredonda baseado no mais perdo de uma borda ou de outra, acima de 5 arredonda para cima

# ----------------------------------------------------------------------------------------------------------------

import math # biblioteca de matematica padrão do python

print(math.floor(9.9)) # Sempre arredonda para baixo

print(math.ceil(9.2)) # Sempre arredonda para cima

print(math.sqrt(9.0)) # square root ou seja raiz quadrada, sempre retorna float