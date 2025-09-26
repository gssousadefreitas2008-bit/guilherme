class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")

    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - "
                f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")
moto1 = Moto("Yamaha", "MT-07", 2022, "Azul")
moto2 = Moto("Honda", "CB 500F", 2021, "Vermelha")

print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(80)
moto2.acelerar(70)
moto1.acelerar(20)   
moto2.acelerar(40)   

print("\n--- Resultado da Corrida ---")
print(moto1.detalhes())
print(moto2.detalhes())

if moto1.velocidade > moto2.velocidade:
    print(f" {moto1.modelo} venceu a corrida!")
elif moto2.velocidade > moto1.velocidade:
    print(f" {moto2.modelo} venceu a corrida!")
else:
    print("Empate! Ambas chegaram com a mesma velocidade.")