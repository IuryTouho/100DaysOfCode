"""
def big_mac():
    print("sanduiche big mac")
print("inicio")
big_mac()
print("fim")
"""

def fazer_big_mac(nome: str):
    print(f"Um big mac para {nome}")


# fazer_big_mac("Iury")
# fazer_big_mac("Igor")

def fazer_batata(tamanho: str):
    print(f"Uma batata {tamanho}.")

def preparar_refrigerante(tipo : str, tamanho : str):
    print(f"Refigerante {tipo} de tamanho {tamanho}")

def fazer_combo(nome : str,tamanho_batata : str,tipo_refri : str,tamanho_refri : str):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)


fazer_combo("Iury","Grande","Fanta","Grande")

def retornar_soma(num1:int,num2:int):
    return num1 + num2

soma = retornar_soma(5,3)

print(soma)