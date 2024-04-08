class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.cor = combustivel
        self.ligado = False
        self.velocidade = 0
        pass

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado")
        else:
            print(f"{self.modelo} ligado.")
            self.ligado = True

    def desligar(self):
        if not self.ligado:
            print("Carro já está desligado")
        else:
            print("Carro desligado.")
            self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"Carro está acelerando a {self.velocidade} km/h.")
        else:
            print("Não é possivel acelerar, carro desligado.")

            self.ligado = True

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"Carro está acelerando a {self.velocidade} km/h.")
        else:
            print("Não é possivel frear, carro desligado.")

            self.ligado = True