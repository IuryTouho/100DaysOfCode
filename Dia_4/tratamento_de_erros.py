try:
    numero = int(input("Digite sua idade: "))
    print(numero)

    10/0
except ValueError:
    print("Digite um valor numérico.")
except ZeroDivisionError:
    print("divisão por 0 não é possivel")
except:
    print("Erro Inesperado")
finally:
    print("Sempre executa")