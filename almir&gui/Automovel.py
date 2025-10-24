class Automovel:
    def __init__(self, nome=None, marca=None, modelo=None):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        if self.nome is None:
            print(f"Automóvel acelerou para {self.velocidade + 10} km/h.")
        else:
            print(f"{self.nome} acelerou para {self.velocidade + 10} km/h.")
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
        if self.nome is None:
            print(f"Automóvel freou para {self.velocidade} km/h.")
        else:
            print(f"{self.nome} freou para {self.velocidade} km/h.")

class Carro(Automovel):
    def ligar_ar(self):
        if self.nome is None:
            print("O carro ligou o ar-condicionado.")
        else:
            print(f"{self.nome} ligou o ar-condicionado.")


class Moto(Automovel):
    def empinar(self):
        if self.nome is None:
            print("A moto está empinando! ")
        else:
            print(f"{self.nome} está empinando! ")


carro1 = Carro(nome="Carro do Almir", marca="Fiat", modelo="Uno")
moto1 = Moto(nome="Moto do Guilherme", marca="Honda", modelo="CG 160")

carro1.acelerar()
carro1.ligar_ar()
carro1.frear()

moto1.acelerar()
moto1.empinar()
moto1.frear()


carro2 = Carro()
carro2.acelerar()
carro2.frear()


