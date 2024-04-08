"""
open("caminho","r")
'r' - read
'a' - append Adiciona o que você escreve ao arquivo
'w' - write Escreve como se fosse novo, se você usar ele vai apagar o arquivo e vai escrever o solicitado, pode criar arquivos tbm
'x' - create só cria arquivos novos, não reescreve
'r+' = read + write
"""
"""
try:
    arquivo = open("Dia_5/texte2.txt","x")

    #Verifica se o arquivo pode ser lido
    
    if arquivo.readable():
        # read() lê todo o arquivo, ja o readline le uma linha, se executado varias vezes le as linhas em sequencia
        #print(arquivo.readline())   
        lista = arquivo.readlines()
        print(lista[2])
    
    arquivo.write("\nSQL")
finally:
    arquivo.close


"""

import os
"""
if os.path.exists("Dia_5/texte2.txt"):
    os.remove("Dia_5/texte2.txt")
else:
    print("Arquivo não existe")


"""
# Só apaga pastas vazias
os.rmdir("Dia_5/NovaPasta")