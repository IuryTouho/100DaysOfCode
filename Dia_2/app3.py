familia =["Iury","Vitor","cameron"]
idades = [10, 15, 21]

print(familia)

print(familia[1])
print(familia[1:])
print(familia[-2:])

familia[2]= "Terry"
print(familia)
#Adiciona lista
familia.extend(["Alfred","Joana"])

print(familia)
#Adiciona valor
familia.append("Spock")
familia.insert(2,"kirk")
print(familia)

#remove o ultimo
familia.pop()
print(familia)

#Remove o que é citado, dá erro caso não exista
familia.remove("kirk")
print(familia)