#Variaveis em python não precisão de tipagem, porem é uma boa pratica tipar assim como no typescript
#Normalmente é usado snake case para variaveis ou seja nomes em minusculo separados por underscore "_"

#Todo Procurar biblioteca para tipar o python
nome = "Iury" #String
idade = 13 #int
altura = 0.5 #float
masculino = True #bool
gosto = "Tudo" 

idade = "oi"
# Duas maneiras de concatenação de strings

# A primeira é a tradicional
print('Meu Nome é '+ nome + '.')

# A segunda se chama f string e é usada a partir do python 3.6, parece ser a mais performatica.
print(f'Meu nome é {nome}.')

