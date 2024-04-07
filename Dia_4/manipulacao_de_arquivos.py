"""
open("caminho","r")
'r' - read
'a' - append
'w' - write
'x' - create
'r+' = read + write
"""
try:
    arquivo = open("Dia_4/texte.txt","r")

    #Verifica se o arquivo pode ser lido
    if arquivo.readable():
        # read() lê todo o arquivo, ja o readline le uma linha, se executado varias vezes le as linhas em sequencia
        #print(arquivo.readline())   
        lista = arquivo.readlines()
        
finally:
    arquivo.close
