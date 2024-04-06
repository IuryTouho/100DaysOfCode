"""
tenho_sede = True
esta_frio = False
if tenho_sede:
    print("Tenho que beber agua")
elif esta_frio:
    print("Vestir blusa")
else:
    print("To de boa")

"""

"""
tenho_sede = True
tenho_fome = False

# Operadores and,or,not, ^(xor)
if not (tenho_sede or tenho_fome):
    print("Tenho que ir na cozinha")
elif tenho_sede ^ tenho_fome :
    print("tenho que comer ou beber algo")
else:
    print("Continuar estudando")
"""

num1 = 5
num2 = 4
#comparação de numeros e strings
if num1 == num2:
    print("Numeros iguais")
elif num1 > num2:
    print("Numero 1 maior que numero 2")
elif num1 != num2:
    print("Numeros diferentes")